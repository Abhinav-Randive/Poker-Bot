class PlayerClass:
    def __init__(self):
        self.name = input('Enter Player 1 name: ')

    def displayPlayer(self):   
        print("Player1:", self.name) 
        
   
pl1 = PlayerClass()
pl1.displayPlayer()
