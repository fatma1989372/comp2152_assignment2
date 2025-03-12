def save_monster_kills(filename="save.txt", kills=0):
    """Save the total number of monster kills to the file."""
    try:
        with open(filename, "w") as file:
            file.write(str(kills))
        print(f"Total monster kills saved: {kills}")
    except Exception as e:
        print(f"Error while saving monster kills: {e}")

def load_monster_kills(filename="save.txt"):
    """Load the total number of monster kills from the file."""
    try:
        with open(filename, "r") as file:
            data = file.read()
            return int(data) if data else 0
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
    except Exception as e:
        print(f"Error while loading monster kills: {e}")
        return 0

if __name__ == "__main__":
    # Test functions to ensure they work correctly
    print("Testing save and load monster kills...")
    save_monster_kills("save.txt", 5)
    kills = load_monster_kills("save.txt")
    print(f"Loaded monster kills: {kills}")
