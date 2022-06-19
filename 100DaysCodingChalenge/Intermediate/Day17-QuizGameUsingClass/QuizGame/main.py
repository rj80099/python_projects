from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))


#print(question_bank)
game=QuizBrain(question_bank)
while not game.still_has_question():
    game.next_question()

game.final_score()