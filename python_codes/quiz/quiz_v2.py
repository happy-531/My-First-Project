import random,time
questions = [
    # Science
    {"category": "Science", "question": "What planet is known as the Red Planet?", "answer": "Mars"},
    {"category": "Science", "question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
    {"category": "Science", "question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"category": "Science", "question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"category": "Science", "question": "What part of the cell contains DNA?", "answer": "Nucleus"},
    {"category": "Science", "question": "What force keeps us on the ground?", "answer": "Gravity"},
    {"category": "Science", "question": "What is H2O commonly called?", "answer": "Water"},
    {"category": "Science", "question": "What organ pumps blood around the body?", "answer": "Heart"},

    # Maths
    {"category": "Maths", "question": "What is 15 × 12?", "answer": "180"},
    {"category": "Maths", "question": "What is 100 ÷ 4?", "answer": "25"},
    {"category": "Maths", "question": "What is the square root of 144?", "answer": "12"},
    {"category": "Maths", "question": "What is 25% of 200?", "answer": "50"},
    {"category": "Maths", "question": "What is 9 × 9?", "answer": "81"},
    {"category": "Maths", "question": "What is 17 + 18?", "answer": "35"},
    {"category": "Maths", "question": "What is the value of pi to two decimal places?", "answer": "3.14"},
    {"category": "Maths", "question": "What is 8³?", "answer": "512"},

    # History
    {"category": "History", "question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"category": "History", "question": "In which year did World War II end?", "answer": "1945"},
    {"category": "History", "question": "Who built the pyramids of Giza?", "answer": "Egyptians"},
    {"category": "History", "question": "Who was known as the Iron Lady?", "answer": "Margaret Thatcher"},
    {"category": "History", "question": "Which empire was ruled by Julius Caesar?", "answer": "Roman Empire"},
    {"category": "History", "question": "Who discovered America in 1492?", "answer": "Christopher Columbus"},
    {"category": "History", "question": "Who was the first Emperor of India?", "answer": "Chandragupta Maurya"},
    {"category": "History", "question": "Which wall divided Berlin?", "answer": "Berlin Wall"},

    # Geography
    {"category": "Geography", "question": "What is the capital of Australia?", "answer": "Canberra"},
    {"category": "Geography", "question": "Which desert covers most of northern Africa?", "answer": "Sahara"},
    {"category": "Geography", "question": "Mount Everest is located in which country?", "answer": "Nepal"},
    {"category": "Geography", "question": "What river runs through Egypt?", "answer": "Nile"},
    {"category": "Geography", "question": "What is the largest ocean?", "answer": "Pacific Ocean"},
    {"category": "Geography", "question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"category": "Geography", "question": "Which continent is Brazil in?", "answer": "South America"},
    {"category": "Geography", "question": "What is the largest country by area?", "answer": "Russia"},

    # Literature
    {"category": "Literature", "question": "Who wrote 'The Hobbit'?", "answer": "J.R.R. Tolkien"},
    {"category": "Literature", "question": "Who wrote 'Pride and Prejudice'?", "answer": "Jane Austen"},
    {"category": "Literature", "question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"category": "Literature", "question": "Who wrote the Harry Potter series?", "answer": "J.K. Rowling"},
    {"category": "Literature", "question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"category": "Literature", "question": "Who wrote 'The Odyssey'?", "answer": "Homer"},
    {"category": "Literature", "question": "Who created Sherlock Holmes?", "answer": "Arthur Conan Doyle"},
    {"category": "Literature", "question": "Who wrote 'The Alchemist'?", "answer": "Paulo Coelho"},
]

def current_time():
    return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

def get_username():
 while True:
  username=input("👤 Enter your username: ").strip()
  if not username.strip():
   print("\nplease enter valid username!\n")
  else:
   return username

def reset():
 with open("highscore.txt","w") as f:
   f.write(f"None|0|{current_time()}")
 with open("highscore.txt","r") as f:
  content=f.read().strip()
 return content

def generate_options(q,questions,difficulty):
 correct_answer=q["answer"]
 wrong_answers=[ans["answer"] for ans in questions if ans["answer"]!= correct_answer]

 if difficulty==1:
  options=random.sample(wrong_answers,2)
  options.append(correct_answer)
  random.shuffle(options)
  return options

 elif difficulty==2:
  options=random.sample(wrong_answers,3)
  options.append(correct_answer)
  random.shuffle(options)
  return options
 elif difficulty==3:
    return []

def get_highscore():
 try:
  with open("highscore.txt","r") as f:
   content=f.read().strip()
 except FileNotFoundError:
   content=reset()

 if content:
  data=content.split("|")
  if len(data) >=3:
   user=data[0]
   highscore=data[1]
   highscore_time=data[2]
  else:
   content=reset()
   data=content.split("|")
   user=data[0]
   highscore=data[1]
   highscore_time=data[2]

 else:
  content=reset()
  data=content.split("|")
  user=data[0]
  highscore=data[1]
  highscore_time=data[2]

 return {"user":user,"score":highscore,"time":highscore_time}

def choose_category():

 highscore=get_highscore()

 selected_questions=[]
 while not selected_questions:
  print(f"\n\n🏆 High Score: {highscore['score']}\n👤 By: {highscore['user']}\n📅 Date: {highscore['time']}\n\n")
  user_category=input(
"\n🎮 ===== QUIZ GAME ===== 🎮\n"
"1. 🔬 Science\n"
"2. ➗ Maths\n"
"3. 📜 History\n"
"4. 🌍 Geography\n"
"5. 📚 Literature\n"
"6. 🎲 Mixed\n\n"
"Choose a category:\n>"
).strip()
  match user_category:
   case "1":
    selected_questions=[q for q in questions if q["category"]=="Science"]
    print("🔬 Science questions list created!\n")
   case "2":
    selected_questions=[q for q in questions if q["category"]=="Maths"]
    print("➗ Maths questions list created!\n")
   case "3":
    selected_questions=[q for q in questions if q["category"]=="History"]
    print("📜 History questions list created!\n")
   case "4":
    selected_questions=[q for q in questions if q["category"]=="Geography"]
    print("🌍 Geography questions list created!\n")
   case "5":
    selected_questions=[q for q in questions if q["category"]=="Literature"]
    print("📚 Literature questions list created!\n")
   case "6":
    selected_questions=questions
    print("🎲 Mixed questions list created!\n")
   case _:
    print("❌ Invalid input")

 return selected_questions

def choose_difficulty():
 while True:
  difficulty=input(
"\n🎯 Select Difficulty\n"
"1. 😌 Easy\n"
"2. 😎 Medium\n"
"3. 🔥 Hard\n>").strip()
  if difficulty in ("1", "2", "3"):
    return difficulty
  print("❌ Invalid choice")

def choose_question_count(selected_questions):
 while True:
  number_of_questions=input(f"❓ How many questions would you like to answer? (1-{len(selected_questions)})\n>").strip()

  if number_of_questions.isdigit() and 0 < int(number_of_questions) <= len(selected_questions):
   quiz_questions=random.sample(selected_questions,int(number_of_questions))
   return quiz_questions
  else:
   print(f"invalid number choose number between 1 to {len(selected_questions)}.")

def check_answer(q,score,streak,best_streak,answered_questions,wrong_questions,user_answer,options,difficulty):
 if q["answer"].strip().lower() == user_answer.strip().lower():
  print("✅ Correct!\n")
  if difficulty=="1":
   score+=1
   answered_questions+=1
  elif difficulty=="2":
   score+=2
   answered_questions+=2
  elif difficulty=="3":
   score+=3
   answered_questions+=3
  streak+=1
  if streak>best_streak:
   best_streak=streak
  print(f"🔥 Streak: {streak}")
 else:
  print(f"❌ Wrong! Correct answer: {q['answer']}")
  if streak>0:
   print("💔 Streak Broken!")
  streak=0
  answered_questions+=1

  wrong_questions.append({
    "question": q["question"],
    "correct": q["answer"],
    "your_answer": user_answer
})
 return (score,streak,wrong_questions,best_streak,answered_questions)

def playquiz(quiz_questions,selected_questions,difficulty):
 score=0
 streak=0
 best_streak=0
 answered_questions=0
 wrong_questions=[]
 check_answer_result=(0,0,[],0,0)

 for opt_num,q in enumerate(quiz_questions):

  options=generate_options(q,selected_questions,difficulty)
  if difficulty==3:
    quiz=q["question"]+"\n>"
  else:
   ui_options=[f"{i+1}. {option}" for i,option in enumerate(options)]
   quiz=q["question"]+"\n"+"\n".join(ui_options)+"\n>"

  print(f"\n📝 Question: {opt_num+1}/{len(quiz_questions)}")
  user_answer=input(quiz).strip()

  if difficulty==3:
   check_answer_result=score,streak,wrong_questions,best_streak,answered_questions=check_answer(q,score,streak,best_streak,answered_questions,wrong_questions,user_answer,options,difficulty="3")
  elif user_answer.isdigit() and int(user_answer) <= len(options) and int(user_answer)>=1:
   user_answer=options[int(user_answer)-1]
   check_answer_result=score,streak,wrong_questions,best_streak,answered_questions=check_answer(q,score,streak,best_streak,answered_questions,wrong_questions,user_answer,options,str(difficulty))

  elif "exit" in user_answer.lower():
   print("🚪 EXITING ...")
   break
  else:
   print(f"⚠️ Please choose an option between 1 and {len(options)}.")
   continue

 return check_answer_result

def show_result(score,wrong_questions,best_streak,time_taken,answered_questions):
 current_score=f"{score}/{answered_questions}"
 if answered_questions == 0:
    print("No questions answered.")
    return
 percentage=round((score/answered_questions)*100)
 print("🎉 Quiz Finished!\n")
 if difficulty=="1":
  print(f"✅ Correct Answers: {score}")
  print(f"❌ Wrong Answers: {answered_questions-score}\n")
 elif difficulty=="2":
  print(f"✅ Correct Answers: {int(score/2)}")
  print(f"❌ Wrong Answers: {int((answered_questions/2)-(score/2))}\n")
 elif difficulty=="3":
  print(f"✅ Correct Answers: {int(score/3)}")
  print(f"❌ Wrong Answers: {int((answered_questions/3)-(score/3))}\n")
 print(f"🏆 Your Score: {current_score}\n📊 Percentage: {percentage}%\n")
 print(f"🔥 Best Streak: {best_streak}\n⏱️ Time Taken: {time_taken} seconds\n")

 if percentage>=90:
  print("🌟 Grade: A+\n")
 elif percentage>=80:
  print("🥇 Grade: A\n")
 elif percentage>=70:
  print("🥈 Grade: B\n")
 elif percentage>=60:
  print("🥉 Grade: C\n")
 elif percentage>=40:
  print("📘 Grade: D\n")
 else:
  print("📕 Grade: F\n")
 review=input(
"📚 Select if you want to review your mistakes:\n"
"1. Yes\n"
"Type anything = No\n>"
)
 if review=="1":
  review_mistakes(wrong_questions)
 else:
  return

def review_mistakes(wrong_questions):

    if not wrong_questions:
        print("\n🎉 Perfect score! No mistakes to review.\n")
        return

    print("\n📚 REVIEW MISTAKES\n")

    for num, item in enumerate(wrong_questions, start=1):
        print(f"{num}. {item['question']}")
        print(f"   Your answer: {item['your_answer']}")
        print(f"   Correct answer: {item['correct']}\n")


def handle_highscore(username,score):

 highscore=get_highscore()

 if highscore["score"].isdigit() and int(highscore["score"]) < score:
  with open("highscore.txt","w") as f:
   f.write(f"{username}|{score}|{current_time()}")
   print("\n🎉🏆 NEW HIGH SCORE! 🏆🎉\n")
 elif not str(highscore['score']).isdigit():
  reset()


username=get_username()
while True:

 selected_questions=choose_category()

 difficulty=choose_difficulty()
 difficulty_name = {
    "1":"😌 Easy",
    "2":"😎 Medium",
    "3":"🔥 Hard"
}

 print(f"\n🎯 Difficulty: {difficulty_name[difficulty]}\n")

 quiz_questions=choose_question_count(selected_questions)

 start_time=time.time()

 score,streak,wrong_questions,best_streak,answered_questions=playquiz(quiz_questions,selected_questions,int(difficulty))

 end_time=time.time()
 time_taken=round(end_time-start_time)

 show_result(score,wrong_questions,best_streak,time_taken,answered_questions)

 handle_highscore(username,score)

 play_again=input(
    "\n🔄 Would you like to play again?\n"
    "1. Yes\n"
    "Type anything else to exit.\n>"
).strip()

 if play_again=="1":
  print("🔄 Restarting game ...")
 else:
  print("🙏 Thanks for playing our quiz game!\n🎉 Have a great day!")
  break
