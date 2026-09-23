import random


# -------------------------
# Weapon Class
# -------------------------

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def display(self):
        print(f"Weapon: {self.name}")
        print(f"Damage: {self.damage}")


# -------------------------
# Character Class
# -------------------------

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

    def display_health(self):
        print(f"{self.name}'s Health: {self.health}")


# -------------------------
# Player Class
# Inherits Character
# -------------------------

class Player(Character):

    def __init__(self, name, health, gold, weapon):
        super().__init__(name, health)

        self.gold = gold
        self.weapon = weapon

    def attack(self, monster):
        damage = self.weapon.damage

        print(
            f"{self.name} attacks {monster.name} "
            f"with {self.weapon.name}!"
        )

        monster.health -= damage

        if monster.health < 0:
            monster.health = 0

        print(f"{monster.name} takes {damage} damage.")

    def heal(self):
        amount = 20
        self.health += amount

        if self.health > 100:
            self.health = 100

        print(f"{self.name} healed by {amount} health.")

    def display(self):
        print("\n----- PLAYER -----")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Gold: {self.gold}")
        print(f"Weapon: {self.weapon.name}")


# -------------------------
# Monster Class
# Inherits Character
# -------------------------

class Monster(Character):

    def __init__(self, name, health, damage, gold_reward):
        super().__init__(name, health)

        self.damage = damage
        self.gold_reward = gold_reward

    def attack(self, player):
        print(f"{self.name} attacks {player.name}!")

        player.health -= self.damage

        if player.health < 0:
            player.health = 0

        print(
            f"{player.name} takes "
            f"{self.damage} damage."
        )


# -------------------------
# Dragon Class
# Inherits Monster
# -------------------------

class Dragon(Monster):

    def __init__(self):
        super().__init__(
            "Dragon",
            100,
            25,
            100
        )


# -------------------------
# Game
# -------------------------

def play_game():

    print("==============================")
    print("      MONSTER ADVENTURE")
    print("==============================")

    print("\nWelcome, brave warrior!")

    print(
        "You have entered a mysterious forest."
    )

    print(
        "Defeat all the monsters and collect "
        "their treasure!"
    )

    # Create weapon
    sword = Weapon("Iron Sword", 25)

    # Create player
    player = Player(
        "Hero",
        100,
        0,
        sword
    )

    # Create monsters
    monsters = [
        Monster("Goblin", 50, 10, 20),
        Monster("Orc", 70, 15, 40),
        Dragon()
    ]

    # Game loop
    for monster in monsters:

        print("\n==============================")
        print(f"A {monster.name} appears!")
        print("==============================")

        while monster.is_alive() and player.is_alive():

            print("\n------------------------------")

            player.display_health()
            monster.display_health()

            print("\nChoose an action:")
            print("1. Attack")
            print("2. Heal")
            print("3. Run")

            choice = input("Enter your choice: ")

            if choice == "1":

                player.attack(monster)

                # Monster attacks if still alive
                if monster.is_alive():
                    monster.attack(player)

            elif choice == "2":

                player.heal()

                # Monster attacks after healing
                if monster.is_alive():
                    monster.attack(player)

            elif choice == "3":

                print("You ran away!")

                print("GAME OVER")
                return

            else:

                print("Invalid choice.")

        # Check player
        if not player.is_alive():

            print("\n==============================")
            print("         GAME OVER")
            print("==============================")

            return

        # Monster defeated
        print("\n******************************")
        print(f"You defeated the {monster.name}!")

        player.gold += monster.gold_reward

        print(
            f"You received "
            f"{monster.gold_reward} gold!"
        )

        print(
            f"Total Gold: {player.gold}"
        )

    # All monsters defeated
    print("\n==============================")
    print("         YOU WIN!")
    print("==============================")

    print(
        f"Congratulations {player.name}!"
    )

    print(
        f"You collected {player.gold} gold."
    )


# Start game
play_game()