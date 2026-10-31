question1 = {
    "question": "What is the capital of Ethiopia?",
    "options": ["A", "B", "C", "D"],
    "display_options": "A. Addis Ababa  B. Jimma  C. Dessie  D. Nairobi",
    "answer": "A"
}
question2={
    "question":"What is the language that has the extension .py",
    "options":["A","B","C","D"],
    "display_options":"A.cpp   B.java C.GO D.python",
    "answer":"D"
}
question3 = {
    "question": "Which river is the longest in the world?",
    "options": ["A", "B", "C", "D"],
    "display_options": "A. Amazon River  B. Nile River  C. Yangtze River  D. Mississippi River",
    "answer": "B"
}

question4 = {
    "question": "What is the square root of 64?",
    "options": ["A", "B", "C", "D"],
    "display_options": "A. 6  B. 7  C. 8  D. 9",
    "answer": "C"
}

question5 = {
    "question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
    "options": ["A", "B", "C", "D"],
    "display_options": "A. Oxygen  B. Hydrogen  C. Nitrogen  D. Carbon Dioxide",
    "answer": "D"
}
questions=[question1,question2,question3,question4,question5]

def display_question(q_data):
  return  f'{q_data["question"]}\n{q_data["display_options"]}'

def getValid_answer(q_data):
  while True:
    userInput=input("enter ur choice:").upper()
    if userInput in q_data['options']:
      return userInput
    print("invalid option")
# print(getValid_answer(question5))    
def check_answer(user_input,answer):
  if user_input==answer:
    return True
  else:
    return False

correct_point=0
for question in questions:
  print(display_question(question))
user_choice=getValid_answer(question)
if check_answer(user_choice,question['answer']):
  print("correct!")
  correct_point+=1
else:
  print("wrong")
print(f"final sore:{correct_point}/{len(questions)}")


      
      





    
