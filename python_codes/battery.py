import os
import json

# This calls the Termux system command and gets the battery info
stream = os.popen('termux-battery-status')
output = stream.read()
data = json.loads(output)

percentage = data['percentage']
status = data['status']

print(f"Battery is at {percentage}% and currently {status}.")

if percentage < 35 and status != "CHARGING":
    print("Warning: Low battery!")

    os.system('termux-tts-speak "Please charge your phone Master"')
