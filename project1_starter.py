"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Angel Drake
Date: 10.31.2025

AI Usage: Handiling Errors and implementing the functions

"""
#Create_character: 1st Function
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    char_dict = {"name": name,
                 "class": character_class,
                 "level": level,
                 "strength": strength,
                 "magic": magic,
                 "health": health,
                 "gold": 100
                 }
    return char_dict


    pass
#Stats Calculation: 2nd Function
def calculate_stats(character_class, level):
    """

    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    strength = 0
    magic = 0
    health = 0

    if character_class.lower() == "mage":
        strength = 5 + level
        magic = 80 + level * 2
        health = 50 + level * 2

    elif character_class.lower() == "warrior":
        strength = 80 + level * 2
        magic = 10 + level * 1
        health = 80 + level * 3

    elif character_class.lower() == "rogue":
        strength = 50 + level * 2
        magic = 50 + level * 2
        health = 30 + level
    elif character_class.lower() == "cleric":
        strength = 50 + level * 2
        magic = 80 + level * 2
        health = 80 + level * 3
    else:
        print("No class given")
        strength = 10
        magic = 10
        health = 10

    return (strength, magic, health)
    
import os
#Saving character information: 3rd function
def save_character(character, filename):
    
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    

    text = (
        f"Character Name: {character['name']}\n"
        f"Class: {character['class']}\n"
        f"Level: {character['level']}\n"
        f"Strength: {character['strength']}\n"
        f"Magic: {character['magic']}\n"
        f"Health: {character['health']}\n"
        f"Gold: {character['gold']}\n"
        )
    
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False
    
    f = open(filename, "w", encoding='utf-8') 
    f.write(text)
    f.close()
    
    # We must assume True, as we cannot verify without try/except.
    return True
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    
import os
#Function 4: Loading Character
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    
    # Check for file existence (to pass FileNotFoundError test)
    if not os.path.exists(filename):
        return None
        
    # FIX: Use encoding='utf-8' here to read the file correctly
    f = open(filename, "r", encoding='utf-8') 
    lines = f.readlines()
    f.close()

    character = {}
    mapping = {
        "Character Name": "name",
        "Class": "class",
        "Level": "level",
        "Strength": "strength",
        "Magic": "magic",
        "Health": "health",
        "Gold": "gold"
    }

    for line in lines:
        line = line.strip()
        parts = line.split(": ")
        if len(parts) == 2:
            key_label, value = parts
            
            key = mapping[key_label]
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            character[key] = value

    return character
 
#Display Character: 5th Function
def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    
#Leveling recalculation: 6th Function
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character["level"] += 1
    
    # Recalculate stats based on new level
    strength, magic, health = calculate_stats(character["class"], character["level"])
    
    # Update the dictionary
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    
    

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
