import random

# Define player and enemy classes
class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

# Define the game loop
def game_loop():
    # Create the player and enemy
    player = Player("Player", 100, 20)
    enemy = Enemy("Enemy", 50, 10)

    print("You are parachuting into the battlefield...")

    # Game loop
    while True:
        print(f"\n{player.name} has {player.health} health left.")
        print(f"{enemy.name} has {enemy.health} health left.")

        # Player turn
        player_choice = input("\nDo you want to attack (a) or heal (h)? ")
        if player_choice == "a":
            enemy.health -= player.damage
            print(f"You attack {enemy.name} for {player.damage} damage!")
        elif player_choice == "h":
            player.health += 20
            print(f"You heal yourself for 20 health points!")
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
            player.health -= enemy.damage
            print(f"{enemy.name} attacks you for {enemy.damage} damage!")
        elif enemy_choice == "h":
            enemy.health += 10
            print(f"{enemy.name} heals himself for 10 health points!")

        # Check if player is defeated
        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            break

# Call the game loop
game_loop()