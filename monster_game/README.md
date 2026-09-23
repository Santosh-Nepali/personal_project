It uses **classes, objects, inheritance, class attributes, object attributes, and association**.

# 🎮 Game Project: Monster Adventure

## 1. Game Story

The player is a brave warrior who enters a mysterious forest to defeat monsters and collect treasure.

The player starts with a certain amount of health and gold. During the adventure, they encounter different monsters. They can:

- Attack a monster
- Heal themselves
- Run away
- Collect gold after defeating monsters

The goal is to **defeat all the monsters and survive the adventure**.

---

# 2. OOP Design

We'll have four classes:

```text
              Character
              /       \
             /         \
        Player         Monster
                         |
                    Dragon
```

And:

```text
Player ---- has/uses ---- Weapon
```

### Inheritance

```text
Player IS-A Character
Monster IS-A Character
Dragon IS-A Monster
```

### Association

```text
Player HAS-A Weapon
```

---

# 3. Algorithm

### Step 1

Start the game.

### Step 2

Create a `Weapon` object.

### Step 3

Create a `Player` object.

### Step 4

Create different monster objects.

### Step 5

Display the game introduction.

### Step 6

For each monster:

1. Display monster information.
2. Show the player menu.
3. Player chooses:
   - Attack
   - Heal
   - Run

4. If the player attacks:
   - Calculate damage.
   - Reduce monster's health.

5. If monster survives:
   - Monster attacks the player.

6. If monster dies:
   - Player receives gold.

7. Continue to the next monster.

### Step 7

If player's health reaches zero:

```text
GAME OVER
```

### Step 8

If all monsters are defeated:

```text
YOU WIN!
```

---

# 4. Python Implementation

```python
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
```

# 5. Where are the OOP concepts?

### Class

We have several classes:

```python
class Weapon:
class Character:
class Player:
class Monster:
class Dragon:
```

### Object

Objects are created from those classes:

```python
sword = Weapon("Iron Sword", 25)

player = Player(
    "Hero",
    100,
    0,
    sword
)

dragon = Dragon()
```

### Object attributes

These belong to individual objects:

```python
self.name
self.health
self.gold
self.weapon
```

For example:

```python
player.health
dragon.health
```

They can have different values.

### Class attributes

We haven't actually needed a class attribute in this basic version. You could add one:

```python
class Character:
    game_name = "Monster Adventure"
```

Then every `Character` object can access:

```python
print(player.game_name)
print(dragon.game_name)
```

### Inheritance

```python
class Player(Character):
```

means:

```text
Player IS-A Character
```

And:

```python
class Monster(Character):
```

means:

```text
Monster IS-A Character
```

Finally:

```python
class Dragon(Monster):
```

means:

```text
Dragon IS-A Monster
```

### Association

This is particularly important:

```python
class Player(Character):

    def __init__(self, name, health, gold, weapon):
        ...
        self.weapon = weapon
```

The `Player` **has a `Weapon`**.

```text
Player ──────── HAS-A ────────> Weapon
```

The `Player` doesn't inherit from `Weapon`. It simply uses a `Weapon` object.

---

## 6. Final OOP structure

```text
                    Character
                   /         \
                  /           \
             Player           Monster
               |             /       \
               |            /         \
               |       Goblin/Orc    Dragon
               |
               |
             Weapon
```

This is a good beginner project because you can start with the basic version above and then add features such as **multiple weapons, inventory, levels, experience points, different player classes, boss battles, saving/loading the game, and a shop**.
