import random
import time

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} attacks {target.name} and deals {self.damage} damage!")

    def heal(self):
        self.health += 20
        print(f"{self.name} heals themselves and gains 20 health points!")

class Game:
    def __init__(self):
        self.player = Character("Player", 100, 20)
        self.enemy = Character("Enemy", 50, 10)

    def print_welcome_message(self):
        print("**********************************************", PINK)
        print("*                                            *", PINK)
        print("*              WELCOME TO PUBG RPG            *"GREEN)
        print("*                                            *"PINK)
        print("**********************************************"PINK)
        print("\nSurvive the battle and become the last player standing!\n", GREEN)
        time.sleep(1)

    def game_loop(self):
        self.print_welcome_message()

        print("You are entering the battlefield...")

        while True:
            print(f"\n{self.player.name} has {self.player.health} health left.")
            print(f"{self.enemy.name} has {self.enemy.health} health left.")

            player_choice = input("\nDo you want to attack (a) or heal (h)? ")

            if player_choice == "a":
                self.player.attack(self.enemy)
            elif player_choice == "h":
                self.player.heal()
            else:
                print("Invalid input. Please choose 'a' to attack or 'h' to heal.")
                continue

            if self.enemy.health <= 0:
                print(f"\n{self.enemy.name} has been defeated!")
                break

            enemy_choice = random.choice(["a", "h"])

            if enemy_choice == "a":
                self.enemy.attack(self.player)
            elif enemy_choice == "h":
                self.enemy.heal()

            if self.player.health <= 0:
                print(f"\n{self.player.name} has been defeated!")
                break

if __name__ == "__main__":
    game = Game()
    game.game_loop()
