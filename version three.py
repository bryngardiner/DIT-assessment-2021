# quiz version three
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

    
class Gui:
    

    def __init__(self):
        # window setup
        app = gui("Single Question Quiz", "600x300")
        self._app = app
        
        app.setBg("white")
        app.setFont(18)
        app.addLabel("question_text",colspan=2)
        app.setLabelBg("question_text","black")
        app.setLabelFg("question_text","white")
        app.setLabel("question_text",questions[0].get_question_text())
        
        with app.frame("options"):
            for answer in questions[0].get_answer_array():
                app.addRadioButton("ans",answer)
            app.setRadioButtonChangeFunction("ans",self.push)
        
        app.addLabel("result",colspan=2)
        app.addButton("next",self.next_question)
        app.hideButton("next")
        app.go()
        

questions = [] 
quiz_progress = 0

# main routine       

quiz = Gui()