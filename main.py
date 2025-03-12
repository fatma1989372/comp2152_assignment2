from functions import save_monster_kills, load_monster_kills
from hero import Hero
from monster import Monster
from character import Character
import os
import platform

if __name__ == "__main__":
    # Print OS name and Python version
    print(f"Operating System: {os.name}")
    print(f"Python Version: {platform.python_version()}")

    # Load existing monster kills
    total_kills = load_monster_kills()

    # Create hero
    hero = Hero()

    # Create a list of monsters using list comprehension (3 monsters)
    monsters = [Monster() for _ in range(3)]

    print(f"Hero -> Combat Strength: {hero.combat_strength}, Health Points: {hero.health_points}")

    for monster in monsters:
        print(f"\nNew Monster Appeared! Combat Strength: {monster.combat_strength}, Health Points: {monster.health_points}")

        while monster.health_points > 0 and hero.health_points > 0:
            damage = hero.combat_strength
            monster.health_points = max(0, monster.health_points - damage)
            print(f"Hero attacks with {damage} damage! Monster's remaining HP: {monster.health_points}")

            # Monster counterattacks if alive
            if monster.health_points > 0:
                damage = monster.combat_strength
                hero.health_points = max(0, hero.health_points - damage)
                print(f"Monster attacks back with {damage} damage! Hero's remaining HP: {hero.health_points}")

        # If the monster is killed, update the total kills
        if monster.health_points == 0:
            total_kills += 1
            save_monster_kills("save.txt", total_kills)
            print("Monster defeated!")

        # If hero dies, break the loop
        if hero.health_points == 0:
            print("Hero has fallen! Game Over!")
            break

    print(f"Total monsters killed so far: {total_kills}")

    # Clean up objects
    del hero
    del monsters

    # This is a new test comment for Git commit proof
    # this is a new test comment