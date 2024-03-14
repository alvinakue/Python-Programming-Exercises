import time 
import random 
 
# Define ANSI color codes for printing colored messages 
RED = "\033[1;31m" 
BLUE = "\033[1;34m" 
PINK = "\033[1;35m" 
YELLOW = "\033[1;33m"
RESET = "\033[0m" 
 
# Define a function to print a colored message 
def print_color(text, color): 
    print(f"{color}{text}{RESET}") 
 
# Print a colored welcoming message 
print_color("**********************************************", RED) 
print_color("*                                            *", RED) 
print_color("*              WELCOME TO ANIMAL FIGHTS           *", BLUE) 
print_color("*                                            *", RED) 
print_color("**********************************************", RED) 
print_color("\nSurvive the battle and become the last player standing!\n", YELLOW) 
time.sleep(1) 
 
class Character: 
    def __init__(self, name, health, damage): 
        self.name = name 
        self.health = health 
        self.damage = damage 
 
    def attack(self, target): 
        target.health -= self.damage 
        print(f"{self.name} attacks {target.name} for {self.damage} damage!") 
 
    def heal(self): 
        self.health += 20 
        print(f"{self.name} heals themselves for 20 health points!") 
 
# Define the game loop 
def game_loop(): 
    print("You are parachuting into the battlefield...") 
 
    # Create the player and enemy 
    player = Character("Player", 100, 20) 
    enemy = Character("Enemy", 50, 10) 
 
    # Game loop 
    while True: 
        print(f"\n{player.name} has {player.health} health left.") 
        print(f"{enemy.name} has {enemy.health} health left.") 
 
        # Player turn 
        player_choice = input("\nDo you want to attack (a) or heal (h)? ") 
        if player_choice == "a": 
            player.attack(enemy) 
        elif player_choice == "h": 
            player.heal() 
        else: 
            print("Invalid input. Try again.") 
            continue 
 
        # Check if enemy is defeated 
        if enemy.health <= 0: 
            print(f"\n{enemy.name} has been defeated!") 
            break 
 
        # Enemy turn 
        enemy_choice = random.choice(["a", "h"]) 
        if enemy_choice == "a": 
            enemy.attack(player) 
        elif enemy_choice == "h": 
            enemy.heal() 
 
        # Check if player is defeated 
        if player.health <= 0: 
            print(f"\n{player.name} has been defeated!") 
            break 
 
# Call the game loop 
game_loop()
