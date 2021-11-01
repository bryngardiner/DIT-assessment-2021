
# quiz
# bryn

# import libraries
from appJar import gui

questions = [] 
quiz_progress = 0

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
        
       
            
    # has to be the last thing that runs
      
        
    def push(self, rb):
        print(self._app.getRadioButton(rb))
        global quiz_progress
        if self._app.getRadioButton(rb) == questions[quiz_progress].correct_answer:
            self._app.setLabel("result","Correct")
 
        else:
            self._app.setLabel("result","WRONG")
            
        self._app.showButton("next")
        
    def next_question(self):
        global quiz_progress
        self._app.openFrame("options")
        self._app.emptyCurrentContainer() 
        for answer in questions[quiz_progress].get_answer_array():
            self._app.addRadioButton("ans",answer)
        app.setRadioButtonChangeFunction("ans",self.push)  
        
        
        """
        
        DOESNT WORK YET
        for answer in questions[quiz_progress].get_answer_array():
             self._app.addRadioButton("ans",answer) 
        """
        
                   
        #app.setRadioButtonChangeFunction("ans",self.push)
        self._app.stopFrame()    

# main routine       
questions.append(Question("How many 1/4 notes are in a bar of 3/4?",["A) 5","B) 2","C) 4"],"D) 3"))
questions.append(Question("What colour is it today?",["Mbrue","red","white"],"red"))

quiz = Gui()

#single_question_quiz.py
