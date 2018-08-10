import numpy as np
import math
import random

class questions:

    def __init__(self, title=''):
        self.title = title
        self.addTerms = []
        self.addTermsAK = []
        self.subTerms = []
        self.subTermsAK = []
        self.AllQuestions = []
        self.AllQuestionsAK = []
        self.number_of_adds = 0
        self.number_of_subs = 0
        self.n = 0



    def setup(self):

        self.number_of_adds = int(input('number of additions? '))
        self.number_of_subs = int(input('number of subtractions? '))
        self.n = int(input('number of terms? '))

        for j in range(0, self.number_of_adds):
            random_terms = []
            for i in range(0, self.n):
                random_terms.append(random.randint(1, 20))
            self.addTerms.append(random_terms)
            self.addTermsAK.append(np.sum(random_terms))

        for j in range(0, self.number_of_subs):
            random_terms = []
            for i in range(0, self.n):
                random_terms.append(random.randint(-20, -1))
            self.subTerms.append(random_terms)
            self.subTermsAK.append(np.sum(random_terms))

        self.AllQuestions = self.addTerms + self.subTerms
        self.AllQuestionsAK = self.addTermsAK + self.subTermsAK

    def showTerms(self, question_number):
        print(self.terms[question_number-1])

    def showAllTerms(self):
        print(self.addTerms)
        print(self.subTerms)

    def makeQuestion(self, question_number):
        if self.addTerms:
            for i in range(0, len(self.addTerms)):
                question = ' + '.join(map(str, self.addTerms[i]))
                print('question ' + str(i+1) +  ': ' + question + ' = ')
        if self.subTerms:
            for i in range(0, len(self.subTerms)):
                question = ' '.join(map(str, self.subTerms[i]))
                print('question ' + str(i+len(self.addTerms)+1) +  ': ' + question  + ' = ')

    def showAnswer(self):
        num = 1
        for q in self.AllQuestionsAK:
            print('Solution ' + str(num) +  ': ' + str(q))
            num = num + 1


a = questions()

a.setup()

print(a.AllQuestions)

# a.showAllTerms()

a.makeQuestion(1)

a.showAnswer()
