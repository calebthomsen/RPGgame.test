# Base Character class

import os

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

def display_stats(self):
    print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    turns=5
    for current_turn in turns:
        print(player.hp, enemy.hp)   #player and enemy are not defined, hp isnt defined
        if current_turn == "player":
            print(f"TURNS: \n{current_turn}\n{turns[turns.index(current_turn)+ 1:]}")
            choice = input("1. Attack\n2. Defend\n")
            if choice == "1":
                self.Attack(player, enemy) #player and enemy are not defined
                player.dif = 20  #player is not defined
            elif choice == "2":
                player.dif *= 2  #player is not defined
            else:
                print("Lost your chance!")
        elif current_turn == "enemy":
            print("Enemy turn!")
            print(f"Next turns are: {turns}")
            enemy_choice = random.randint(1, 2)
            if enemy_choice == 2:
                print("He attacks you!")
                self.Attack(enemy, player) #player and enemy are not defined
                enemy.dif = 0 #enemy is not defined
            else:
                print("He defends himself.")
                enemy.dif = 10
        os.system("clear")
        turns.pop(0)
        if player.hp <= 0: #player is not defined
            print("You died!")
            break
        elif enemy.hp <= 0: #enemy is not defined
            print("YOU WON!")
            break
        

import random

def calculate_damage(min_damage, max_damage):
  """Calculates random damage between min and max values."""
  return random.randint(min_damage, max_damage)

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=60)

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        pass  # Implement Archer class
    elif class_choice == '4':
        pass  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            pass  # Implement special abilities player.heal and player.special_attack
        elif choice == '3':
            pass  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
