from random import randint

from data import data
from question import Question

questionNumber = 0

class QuizzBrain:
    def __init__(self, questionNumber, questionList):
        self.questionNumber = questionNumber
        self.questionList = questionList
        self.totalNumberOfQuestions = len(questionList)
        self.totalPoints = 0
    def askQuestion(self):
        print(self.questionList[self.questionNumber].text)
        answer = input('')
        if(answer == self.questionList[self.questionNumber].answer):
            print('Right answer! you gain 1 point')
            self.totalPoints += 1
        else:
            print('Wrong answer')
        self.questionNumber +=1
        
questions = []
for question in data:
    questions.append(Question(question['text'],question['answer']))

print(questions)
quizzBrain = QuizzBrain(0,questionList=questions)

for index in range(0,len(questions)):
    quizzBrain.askQuestion()
print(f'you made {quizzBrain.totalPoints} points in total')

