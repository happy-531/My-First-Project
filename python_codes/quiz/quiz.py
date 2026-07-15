import random
questions = [
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"question": "What river runs through Egypt?", "answer": "Nile"},
    {"question": "What is 15 times 12?", "answer": "180"},
    {"question": "Who wrote 'Pride and Prejudice'?", "answer": "Jane Austen"},
    {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "In which year did World War II end?", "answer": "1945"},
    {"question": "What is the value of pi (to two decimal places)?", "answer": "3.14"},
    {"question": "Who wrote 'The Hobbit'?", "answer": "J.R.R. Tolkien"},
    {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
    {"question": "Mount Everest is located in which country?", "answer": "Nepal"},
    {"question": "What is 100 divided by 4?", "answer": "25"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "answer": "Amelia Earhart"},
    {"question": "What is the main function of red blood cells?", "answer": "Transport Oxygen"},
    {"question": "Which desert covers most of northern Africa?", "answer": "Sahara"},
    {"question": "What is the perimeter of a square with side length 5 units?", "answer": "20"},
    {"question": "Who is the author of the Harry Potter series?", "answer": "J.K. Rowling"},
    {"question": "What ancient civilization built the pyramids of Giza?", "answer": "Egyptians"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"}
]

random.shuffle(questions)
score=0

def generate_options(q,questions):
 correct_answer=q["answer"]
 wrong_answers=[ans["answer"] for ans in questions if ans["answer"]!= correct_answer]

 options=random.sample(wrong_answers,3)
 options.append(correct_answer)
 random.shuffle(options)
 return options

for i,q in enumerate(questions):

 options= generate_options(q,questions)
 #ui
 ui_options=[f"{i+1}. {option}" for i,option in enumerate(options)]
 quiz=q["question"]+"\n"+"\n".join(ui_options)+"\n>"
 print(f"\nQuestion: {i+1}/{len(questions)} ")
 user_answer=input(quiz).strip()

 if user_answer.isdigit() and int(user_answer)<=4 and int(user_answer)>=1:
  if q["answer"]==options[int(user_answer)-1]:
    print("✅ Correct!\n")
    score+=1
  else:
   print(f"❌ Wrong! Correct answer: {q['answer']}\n")
 elif "exit" in user_answer.lower():
  print("EXITING ...")
  break
 else:
  print("please choose the option between 1 to 4.")


current_score=f"{score}/{len(questions)}"
percentage=round((score/len(questions))*100)
print(f"Quiz Finished!")
print(f"Your Score: {current_score}\nPercentage: {percentage}%")

if percentage>=90:
 print("Grade: A+")
elif percentage>=80:
 print("Grade: A")
elif percentage>=70:
 print("Grade: B")
elif percentage>=60:
 print("Grade: C")
elif percentage>=40:
 print("Grade: D")
else:
 print("Grade: F")


