import time 
import random 
 
# Define ANSI color codes for printing colored messages 
RED = "\033[1;31m" 
GREEN = "\033[1;32m" 
YELLOW = "\033[1;33m" 
RESET = "\033[0m" 
 
# Define a function to print a colored message 
def print_color(text, color): 
    print(f"{color}{text}{RESET}") 
 
# Print a colored welcoming message 
print_color("**********************************************", YELLOW) 
print_color("*                                            *", GREEN) 
print_color("*              WELCOME TO PUBG RPG           *", GREEN) 
print_color("*                                            *", GREEN) 
print_color("**********************************************", YELLOW) 
print_color("\nSurvive the battle and become the last player standing!\n", GREEN) 
time.sleep(1) 

class Lion: 
    def __init__(self, name): 
        self.name=name 
        self.health = 100
         
    def roar(self): 
        print(f"{self.name} roars loudly!") 
         
    def attack(self, target): 
        print(f"{self.name} attacks with its sharp claws! ")
        target.health -= 30

class Tiger: 
    def __init__(self, name): 
        self.name=name 
        self.health = 100
         
    def roar(self): 
        print(f"{self.name} roars ferociously!") 
         
    def attack(self, target): 
        print(f"{self.name} pounces on its prey! ")
        target.health -= 25

# Define the game loop 
def game_loop(): 
    print("The battle begins...") 
 
    # Create the enemies 
    lion = Lion("Lion")
    tiger = Tiger("Tiger")
 
    # Game loop 
    while lion.health > 0 and tiger.health > 0: 
        print(f"\n{lion.name} has {lion.health} health left.") 
        print(f"{tiger.name} has {tiger.health} health left.") 

        # Lion's turn 
        lion.attack(tiger)
        if tiger.health <= 0: 
            print(f"\n{tiger.name} has been defeated!") 
            break 

        # Tiger's turn 
        tiger.attack(lion)
        if lion.health <= 0: 
            print(f"\n{lion.name} has been defeated!") 
            break 
 
# Call the game loop 
game_loop()
