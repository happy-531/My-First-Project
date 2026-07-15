import os
import json
import time

def is_charging():
    stream = os.popen('termux-battery-status')
    output = stream.read()
    data = json.loads(output)
    print("Checking the battery info...")
    status = data['status']
    if status == "CHARGING":
        return True
    return False

def main():
    print("🔋 Mobile Charger Monitor Started... Keep Termux open.")
    last_status = is_charging()
    print("detecting any change...")
    while True:
        current_status = is_charging()
        print("checking current status...")
        if last_status != current_status:
            if current_status:
                print("Charging the phone")
                os.system("termux-tts-speak 'charging the phone'")
            else:
                print("disconnected")
                os.system("termux-tts-speak 'disconnected'")
            last_status = current_status
        time.sleep(2)

if __name__ == "__main__":
    main()
