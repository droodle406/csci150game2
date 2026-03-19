import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase):
    #qtp default value
    if quantityToPurchase <= 0:
        quantityToPurchase = 0
    
    #determining how much you can possibly afford
    max_affordable = startingMoney // itemPrice

    #determining if your order is purchasable
    if max_affordable >= quantityToPurchase:
        items_bought = quantityToPurchase
    #if its not, your quantity becomes the most you can buy
    else:
        items_bought = max_affordable
    #final calculations, return
    LeftoverMoney = startingMoney-(itemPrice*items_bought)

    return items_bought, LeftoverMoney

# DIVIDER

def new_random_monster():

    # determines monster selection
    monster = (random.randint(1,4))
    #provides attributes for every possible monster
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
    monsterdict = {"name": monstername, "description": monsterdesc, "health": monsterhealthpool, "power": monsterpower, "money": monstermoney}
    return monsterdict

def print_welcome(name, width):
    
    # These 4 lines do some math (probably ineffeciently) to find how many spaces need to come before and after the name
    strlngth = len(name)+7
    twidth = (width - strlngth)
    half = int(twidth/2)
    
    # outputs!
    print(f"{' ' * half}Hello, {name} {' ' * half}")
    return None

# Function Calls
print(print_welcome("Jeff", 20))
print(print_welcome("Audrey", 30))
print(print_welcome("Andrew", 55))

def print_shop_menu(item1name, item1price, item2name, item2price):
    # Converts prices to Floats
    item1 = float(item1price)
    item2 = float(item2price)
    # gets the number of spaces between each value for item1
    item1spaces1 = 12 - len(item1name)
    item1leng = len(str(f"{item1:.2f}"))
    item1spaces2 = 8 - item1leng
    #same thing item2
    item2spaces1 = 12 - len(item2name)
    item2leng = len(str(f"{item2:.2f}"))
    item2spaces2 = 8 - item2leng


    print(f"/----------------------\ \n| {item1name}{' ' * item1spaces1}{' ' * item1spaces2}${item1:.2f}|\n| {item2name}{' ' * item2spaces1}{' ' * item2spaces2}${item2:.2f}|\n\----------------------/")

    return None


# Function Calls
print(print_shop_menu("Apple", 31, "Pear", 1.234))
print(print_shop_menu("Egg", .23, "Bag of Oats", 12.34))
print(print_shop_menu("Sword", 4000, "Ham", 22.25))
