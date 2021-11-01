# quiz version two
# bryn

# import libraries
from appJar import gui

#functions

# class definitions

class Question:
    # initilise class
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer      
    # returns True if correct answer is selected
    def check_correct(self, selected_answer):
        _correct = True
        return _correct
    # returns array of all possible answers
    def get_answer_array(self):
        _answer_array = self.answers
        _answer_array.append(self.correct_answer)
        return _answer_array
    # returns the answer text
    def get_question_text(self):
        return self.question
    

questions = [] 
quiz_progress = 0

# main routine       

quiz = Gui()