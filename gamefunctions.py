"""Game Functions Module.

This module contains functions relating to gameplay technicalities."""


import random
import json
import os

def purchase_item(itemPrice, startingMoney, quantityToPurchase):

    """
    Purchases an item for a Player

    Parameters:
    itemPrice (float): Price of an individual item
    startingMoney (float): Player Bank Account
    quantityToPurchase (int): Number of items player wishes to buy

    Returns:
    items bought and leftover money

    Example:
        purchase_item(2, 200, 10)
        2, 180
    """
    
    if quantityToPurchase <= 0:
        quantityToPurchase = 0
    
    max_affordable = startingMoney // itemPrice

    if max_affordable >= quantityToPurchase:
        items_bought = quantityToPurchase
    else:
        items_bought = max_affordable

    LeftoverMoney = startingMoney-(itemPrice*items_bought)

    return items_bought, LeftoverMoney


def new_random_monster():

    """
    Generates a random monster for the player

    Parameters:
    None

    Returns:
    Dictionary of the monsters stats.

    Example:
        new_random_monster()
    """

    monster = (random.randint(1,4))

    if monster == 1:
        monstername = "goblin"
        monsterdesc = "The curious green goblin see you and snarls. Good luck."
        monsterhealthpool = (random.randint(100,500))
        monsterpower = (random.randint(1,7))
        monstermoney = (random.randint(245,1000))
    elif monster == 2:
        monstername = "ork"
        monsterdesc = "The hulking green beast stares you down and roars. Good luck."
        monsterhealthpool = (random.randint(1500,3000))
        monsterpower = (random.randint(10,25))
        monstermoney = (random.randint(1,200))
    elif monster == 3:
        monstername = "troll"
        monsterdesc = "As you cross a bridge you hear loud footsteps through the river it crosses, this troll has no riddle. Good luck."
        monsterhealthpool = (random.randint(5000,10000))
        monsterpower = (random.randint(5,15))
        monstermoney = (random.randint(750,2000))
    elif monster == 4:
        monstername = "skeleton"
        monsterdesc = "Those spooky scary skeletons will make you shiver and shriek. Good luck."
        monsterhealthpool = (random.randint(100,150))
        monsterpower = (random.randint(1,5))
        monstermoney = (random.randint(1,100))
    else:
        return None

    monsterdict = {
        "name": monstername,
        "description": monsterdesc,
        "health": monsterhealthpool,
        "power": monsterpower,
        "money": monstermoney
    }

    return monsterdict


def print_welcome(name, width):

    """
    Welcomes the player to the game

    Parameters:
    name (str): Player name
    Width (int): number of characters allowed

    Returns:
    Welcome, Player name between a set amount of spaces/characters

    Example:
        print_welcome(Jeff, 15)
              Welcome, Jeff      
    """
    
    strlngth = len(name)+7
    twidth = (width - strlngth)
    half = int(twidth/2)
    
    print(f"{' ' * half}Hello, {name} {' ' * half}")
    return None


def print_shop_menu(item1name, item1price, item2name, item2price):

    """
    Generates a menu for a shop

    Parameters:
    item1name (str): Name of item1
    item1Price (float): cost of item1
    item2name (str): Name of item2
    item2Price (float): cost of item2

    Returns:
    None

    Example:
        print_shop_menu(Food, 2, Drink, 3)
        Outputs formatted menu
    """

    item1 = float(item1price)
    item2 = float(item2price)

    item1spaces1 = 12 - len(item1name)
    item1leng = len(str(f"{item1:.2f}"))
    item1spaces2 = 8 - item1leng

    item2spaces1 = 12 - len(item2name)
    item2leng = len(str(f"{item2:.2f}"))
    item2spaces2 = 8 - item2leng

    print(f"/----------------------\\ \n| {item1name}{' ' * item1spaces1}{' ' * item1spaces2}${item1:.2f}|\n| {item2name}{' ' * item2spaces1}{' ' * item2spaces2}${item2:.2f}|\n\\----------------------/")

    return None

def battle(playerhp, gold, playerdamage, player_inventory, equipped):

    """
    Runs a battle between the player and a monster

    Parameters:
    playerhp (int): Player health
    gold (int): Player gold
    playerdamage (int): Player damage

    Returns:
    playerhp and gold

    Example:
        battle(100, 50, 10)
    """

    monster_info = new_random_monster()
    
    while playerhp > 0 and monster_info["health"] > 0:

        if equipped:
            totaldamage = playerdamage + equipped["damage"]
        else:
            totaldamage = playerdamage
        
        print(f"{monster_info['description']}\nThe {monster_info['name']} has {monster_info['health']} health and does {monster_info['power']} damage.")
        if equipped:
            print(f"You do {totaldamage} damage, you have a {equipped['name']} equipped and you have {playerhp} health.")
        else:
            print(f"You do {totaldamage} damage and you have {playerhp} health.")
        
        user_action = input("What would you like to do? \n1) Fight \n2) Equip Item (Will use your turn!!)\n3) Use consumable\n4) Run\n")
        
        if user_action == "1":
            if equipped:
                equipped["currentDurability"] -= 1
                monster_info["health"] -= totaldamage
                playerhp -= monster_info["power"]
                if equipped["currentDurability"] == 0:
                    print("Your sword shatters in your hand!")
                    if equipped in player_inventory:
                        player_inventory.remove(equipped)
                    equipped = None
            else:
                monster_info["health"] -= totaldamage
                playerhp -= monster_info["power"]

        elif user_action == "2":
            item_type = input("What type of item would you like to equip? \nChoices: weapon")
            if item_type == "weapon":
                equipped = equip_item(player_inventory, "weapon")
                    
            else:
                print("That is not a supported type, try again.")

        elif user_action == "3":
            consumables = [item for item in player_inventory if item["type"] == "consumable"]

            if not consumables:
                print("You have no consumables.")
            else:
                print("\n--- Consumables ---")
                for i, item in enumerate(consumables, start=1):
                    print(f"{i}) {item['name']}")
                print("-------------------")

                choice = int(input("Choose a consumable: "))

                if 1 <= choice <= len(consumables):
                    selected_item = consumables[choice - 1]
                    playerhp, monster_info["health"] = use_consumable(
                        player_inventory,
                        selected_item["name"],
                        playerhp,
                        monster_info
                    )
                else:
                    print("Invalid choice.")

            playerhp, monster_info["health"] = use_consumable(player_inventory, selected_item["name"], playerhp, monster_info)
            
        elif user_action == "4":
            print("You ran away.")
            return playerhp, gold, playerdamage, player_inventory, equipped, "ran"
        else:
            print("Unrecognized command")
        
        if playerhp <= 0:
            print("Your character passed out.")
            return playerhp, gold, playerdamage, player_inventory, equipped, "ko"
        elif monster_info["health"] <= 0:
            print(f"Congratulations! You have defeated the {monster_info['name']}!")
            gold += 15
            return playerhp, gold, playerdamage, player_inventory, equipped, "end"

    return playerhp, gold, playerdamage, player_inventory, equipped

def shoploop(gold, inventory):
    """
    Runs the shop interaction loop for the player.

    Parameters:
    gold (int): The player's current gold amount
    inventory (list): The player's current inventory list

    Returns:
    int: The player's updated gold amount after purchases

    Example:
        shoploop(100, [])
        # Displays shop menu, prompts player to buy items, returns remaining gold
    """
    curgold = gold
    print_shop_menu("Sword", 10, "Charm of Doom", 15)
    choice = input("What would you like to buy?\n1) Sword\n2)Charm of Doom\n0) Exit shop")

    if choice == "0":
        print("Have a good day, come again soon!")
        return gold

    if choice == "1":
        item_name = "1"
        price = 10
    elif choice == "2":
        item_name = "2"
        price = 15
    else:
        print("Invalid choice.")
        return gold

    qty = int(input(f"How many would you like to buy? "))

    items_bought, gold = purchase_item(price, curgold, qty)

    for _ in range(items_bought):
        if item_name == "1":
            inventory.append({
                "name": "Sword",
                "type": "weapon",
                "maxDurability": 10,
                "currentDurability": 10,
                "damage": 5,
                "equipped": False
            })
        elif item_name == "2":
            inventory.append({
                "name": "Pendant of Doom",
                "type": "consumable",
                "effect": "auto_defeat"
            })

    print(f"Bought!")
    return gold

def equip_item(inventory, item_type):
    """
    Prompts the player to select and equip an item of a given type.

    Parameters:
    inventory (list): The player's current inventory list
    item_type (str): The type of item to equip (e.g. "weapon", "armor")

    Returns:
    dict or None: The selected item dictionary if one was chosen, otherwise None

    Example:
        equip_item(inventory, "weapon")
        # Displays available weapons and returns the chosen one, or None
    """
    items = [item for item in inventory if item["type"] == item_type]

    if not items:
        print(f"You have no {item_type}s to equip.")
        return None

    print(f"Choose a {item_type} to equip:")
    for i, item in enumerate(items, start=1):
        print(f"{i}) {item['name']}")
    print(f"{len(items)+1}) None")

    choice = int(input("Enter choice: "))

    if choice == len(items) + 1:
        return None
    
    else:
        return items[choice - 1]

def use_consumable(player_inventory, item_name, playerhp, monster_info):
    """
    Uses a consumable item from the player's inventory during battle.

    Parameters:
    player_inventory (list): The player's current inventory list
    item_name (str): Name of the consumable item to use
    playerhp (int): The player's current health points
    monster_info (dict): Dictionary containing the monster's current stats

    Returns:
    tuple: Updated (playerhp, monster health) after the consumable's effect is applied.
           Returns a dict with playerhp and monster on failure (item not found).

    Example:
        use_consumable(inventory, "Pendant of Doom", 80, monster_info)
        # Applies item effect, removes item from inventory, returns updated hp values
    """
    for item in player_inventory:
        if item["name"].lower() == item_name.lower() and item["type"] == "consumable":

            if item.get("effect") == "heal":
                playerhp += item["heal"]
                print(f"You drink a {item['name']} and heal {item['heal']} HP!")
            
            if item.get("effect") == "damage":
                monster_info["health"] -= item["damage"]
                print(f"You throw a {item['name']} and deal {item['damage']} damage!")

            if item.get("effect") == "auto_defeat":
                monster_info["health"] = 0
                print(f"You use your charm, it lights up and instantly turns the monster and itself to dust!")

            if item["type"] != "consumable":
                print(f"{item['name']} is not a consumable.")
                return playerhp, monster_info["health"]

            player_inventory.remove(item)
            return playerhp, monster_info["health"]
    
    print("You don't have that consumable.")
    return playerhp, monster_info["health"]

def printinv(player_inventory):
    """
    Prints a formatted display of the player's inventory.

    Parameters:
    player_inventory (list): The player's current inventory list

    Returns:
    None

    Example:
        printinv(inventory)
        # Displays each item with its type, stats, and relevant attributes
    """
    if not player_inventory:
        print("Your inventory is empty.")
        return
    
    print("\n--- Your Inventory ---")
    for i, item in enumerate(player_inventory, start=1):
        if item["type"] == "weapon":
            print(f"{i}) {item['name']} (Weapon, Damage: {item['damage']}, Durability: {item['currentDurability']}/{item['maxDurability']})")

        elif item["type"] == "consumable":
            if item.get("effect") == "heal":
                print(f"{i}) {item['name']} (Consumable, Heals: {item['heal']})")
            elif item.get("effect") == "damage":
                print(f"{i}) {item['name']} (Consumable, Damage: {item['damage']})")
            elif item.get("effect") == "auto_defeat":
                print(f"{i}) {item['name']} (Consumable), Instant Victory in Battle")
        
        else:
            print(f"{i}) {item['name']} ({item['type']})")
    print("-----------------------\n")

def save_game(filename, playerhp, gold, playerdamage, inventory, equipped):
    """
    Saves the current game state to a file using JSON.

    Parameters:
    filename (str): Name of the save file
    playerhp (int): Player health points
    gold (int): Player gold amount
    playerdamage (int): Player base damage
    inventory (list): Player inventory list
    equipped (dict or None): Currently equipped item

    Returns:
    None
    """
    save_data = {"playerhp": playerhp, "gold": gold, "playerdamage": playerdamage, "inventory": inventory, "equipped": equipped}

    with open(filename, "w") as f:
        json.dump(save_data, f, indent=4)

    print("Game saved successfully!")

def load_game(filename):
    """
    Loads a saved game state from a JSON file.

    Parameters:
    filename (str): Name of the save file to load

    Returns:
    tuple: (playerhp, gold, playerdamage, inventory, equipped) if file exists,
           None if file is not found
    """
    if not os.path.exists(filename):
        print("Save file not found.")
        return None

    with open(filename, "r") as f:
        data = json.load(f)

    print("Game loaded successfully!")
    return data["playerhp"], data["gold"], data["playerdamage"], data["inventory"], data["equipped"]

def move_player(map_state, direction):
    """
    Moves the player one tile in the specified direction and updates the map state.

    Parameters:
    map_state (dict): Dictionary containing map data such as player position,
                      town position, monster position, and movement flags.
    direction (str): Direction to move the player. Must be one of:
                     'up', 'down', 'left', 'right'.

    Returns:
    str: Result of the movement:
         "moved" – player moved successfully
         "blocked" – movement was not possible (edge of map)
         "returned_to_town" – player moved back onto the town square after leaving
         "monster_encounter" – player moved onto the monster square

    Example:
        move_player(map_state, "up")
    """
    x, y = map_state["player_pos"]

    if direction == "up" and y > 0:
        y -= 1
    elif direction == "down" and y < 9:
        y += 1
    elif direction == "left" and x > 0:
        x -= 1
    elif direction == "right" and x < 9:
        x += 1
    else:
        return "blocked"

    map_state["player_pos"] = [x, y]

    if map_state["player_pos"] != map_state["town_pos"]:
        map_state["has_left_town"] = True

    if map_state["player_pos"] == map_state["town_pos"] and map_state["has_left_town"]:
        return "returned_to_town"

    if map_state["player_pos"] == map_state["monster_pos"]:
        return "monster_encounter"

    return "moved"

def print_map(map_state):
    """
    Displays a text-based 10x10 map of the current game state.

    Parameters:
    map_state (dict): Dictionary containing map data including:
                      player position, town position, and monster position.

    Returns:
    None

    Notes:
    - "P" represents the player
    - "T" represents the town
    - "M" represents the monster
    - "." represents empty space

    Example:
        print_map(map_state)
    """
    for y in range(10):
        row = ""
        for x in range(10):
            pos = [x, y]

            if pos == map_state["player_pos"]:
                row += "P"
            elif pos == map_state["town_pos"]:
                row += "T"
            elif pos == map_state["monster_pos"]:
                row += "M"
            else:
                row += "."
        print(row)

def map_interface(map_state):
    """
    Runs the map exploration interface, allowing the player to move around the map.

    Parameters:
    map_state (dict): Dictionary containing current map state including player,
                      town, and monster positions.

    Returns:
    tuple:
        (str, dict)
        str:
            "town" – player returned to town square
            "monster" – player encountered a monster
        dict:
            Updated map_state after movement

    Controls:
        w – move up
        s – move down
        a – move left
        d – move right

    Example:
        result, map_state = map_interface(map_state)
    """
    
    while True:
        print_map(map_state)

        choice = input("Move with w/a/s/d: ").lower()

        if choice == "w":
            result = move_player(map_state, "up")
        elif choice == "s":
            result = move_player(map_state, "down")
        elif choice == "a":
            result = move_player(map_state, "left")
        elif choice == "d":
            result = move_player(map_state, "right")
        else:
            print("Invalid input.")
            continue

        if result == "blocked":
            print("You cannot move that way.")
        elif result == "returned_to_town":
            return "town", map_state
        elif result == "monster_encounter":
            return "monster", map_state

