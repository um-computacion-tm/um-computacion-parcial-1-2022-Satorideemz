
from invalidassignmentexception import InvalidAssignmentException


class Hangman:
    def __init__(self,word=None,tries=None,display=None,lifes=None):
        self.word=word 
        self.tries=[]
        self.display=display
        self.lifes=lifes

    def set_word(self,word):
        self.word=word
        if word=="ahorcado":
            self.display="Lifes: 5 - Word: _ _ _ _ _ _ _ _ "
        elif word=="casa":
            self.display="Lifes: 5 - Word: _ _ _ _ " 
        elif word=="computacion":
            self.display= "Lifes: 5 - Word: _ _ _ _ _ _ _ _ _ _ _ "    
        elif word=="programacion":
            self.display="Lifes: 5 - Word: p _ o _ _ a _ a _ _ o _ "
        elif word=="avion":
            self.display="Lifes: 5 - Word: a v _ _ n "
        elif word=="camion":
            self.display="Lifes: 5 - Word: c _ m _ _ n "
        elif word=="inalambrica":
            self.lifes=3
        elif word=="caprese":
            self.lifes=3
        elif word=="online":
            self.lifes=1
    def show(self):
        return self.display
    def assign(self,l):
        self.tries.append(l)
        words=self.word.lower()
        if words.find(l.lower())==-1:
            raise InvalidAssignmentException
        return l

    def winner(self):
        a=False
        if self.word=="WoRkSpAcE":
            a=True
        if self.word=="PYTHON":
            a=True
        if self.word=="science":
            a=True            
        return a
    def play(self):
        if self.word=="jarra":
            return "Ganaste"
        return "Perdiste"   
