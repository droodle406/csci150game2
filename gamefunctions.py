"""Game Functions Module.

This module contains functions relating to gameplay technicalities."""


import random

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


print(print_welcome("Jeff", 20))
print(print_welcome("Audrey", 30))
print(print_welcome("Andrew", 55))


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

    print(f"/----------------------\ \n| {item1name}{' ' * item1spaces1}{' ' * item1spaces2}${item1:.2f}|\n| {item2name}{' ' * item2spaces1}{' ' * item2spaces2}${item2:.2f}|\n\----------------------/")

    return None


print(print_shop_menu("Apple", 31, "Pear", 1.234))
print(print_shop_menu("Egg", .23, "Bag of Oats", 12.34))
print(print_shop_menu("Sword", 4000, "Ham", 22.25))


def test_functions():
    
    """
    Tests all above code

    Parameters:
    None

    Returns:
    None

    Example:
        test_functions()
    """

    print_welcome("Jeff", 20)
    print_shop_menu("Sword", 4000, "Ham", 22.25)
    purchase_item(Potion, 10, 50)
    random_monster()

    return None


def battle(playerhp, gold, playerdamage):

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
        print(f"{monster_info['description']}\nThe {monster_info['name']} has {monster_info['health']} health and does {monster_info['power']} damage.")
        print(f"You do {playerdamage} damage and you have {playerhp} health.")
        
        user_action = input("What would you like to do? \n1) Fight \n2) Run\n")
        
        if user_action == "1":
            monster_info["health"] -= playerdamage
            playerhp -= monster_info["power"]
        elif user_action == "2":
            print("You ran away.")
            return playerhp, gold
        else:
            print("Unrecognized command")
        
        if playerhp <= 0:
            print("Your character passed out.")
            return playerhp, gold
        elif monster_info["health"] <= 0:
            print(f"Congratulations! You have defeated the {monster_info['name']}!")
            gold += 3
            return playerhp, gold

    return playerhp, gold


if __name__ == "__main__":
    test_functions()
