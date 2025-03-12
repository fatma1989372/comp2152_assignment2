import random

class Character:
    def __init__(self):
        # Private attributes
        self._combat_strength = random.randint(1, 100)
        self._health_points = random.randint(1, 100)

    # Getter for combat_strength
    @property
    def combat_strength(self):
        return self._combat_strength

    # Setter for combat_strength
    @combat_strength.setter
    def combat_strength(self, value):
        if isinstance(value, int) and value > 0:
            self._combat_strength = value
        else:
            raise ValueError("Combat strength must be a positive integer.")

    # Getter for health_points
    @property
    def health_points(self):
        return self._health_points

    # Setter for health_points
    @health_points.setter
    def health_points(self, value):
        # Ensure health points never drop below zero
        if isinstance(value, int) and value >= 0:
            self._health_points = value
        elif value < 0:
            self._health_points = 0  # Set to zero if value is negative
        else:
            raise ValueError("Health points must be a non-negative integer.")