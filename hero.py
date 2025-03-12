from character import Character

import random
class Hero(Character):
    def __init__(self):
        # Call the parent constructor
        super().__init__()

    # Method for the hero to attack a monster
    def hero_attacks(self, monster):
        try:
            if not isinstance(monster, Character):
                raise TypeError("The target must be a Character object.")

            damage = self.combat_strength
            monster.health_points -= damage
            print(f"Hero attacks with {damage} damage! Monster's remaining HP: {monster.health_points}")

        except TypeError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Getter for combat_strength
    @property
    def combat_strength(self):
        return self._combat_strength

    # Setter for combat_strength
    @combat_strength.setter
    def combat_strength(self, value):
        if isinstance(value, int) and value >= 0:
            self._combat_strength = value
        else:
            raise ValueError("Combat strength must be a non-negative integer.")

    # Getter for health_points
    @property
    def health_points(self):
        return self._health_points

    # Setter for health_points
    @health_points.setter
    def health_points(self, value):
        if isinstance(value, int) and value >= 0:
            self._health_points = value
        else:
            raise ValueError("Health points must be a non-negative integer.")

    # Destructor
    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector.")


if __name__ == "__main__":
    hero = Hero()
    print(f"Hero -> Combat Strength: {hero.combat_strength}, Health Points: {hero.health_points}")

    monster = Character()
    print(f"Monster -> Combat Strength: {monster.combat_strength}, Health Points: {monster.health_points}")

    hero.hero_attacks(monster)

    del hero
    del monster

