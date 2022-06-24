import random
class Card:
    def __init__(self):
        self.number = 0
    def randomCard(self):
        self.number = random.randint(1,13)
        
