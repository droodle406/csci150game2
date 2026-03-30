import gamefunctions

playerhp = 300
gold = 50
playerdamage = 25

def loop():

    """
    Main game loop to start off with

    Parameters:
    None

    Returns:
    None

    Example:
        loop()
    """

    global playerhp, gold, playerdamage
    
    user_input = input(f"You are in town.\n Current HP: {playerhp}, Current Gold: {gold}\nWhat would you like to do?\n1) Leave town (Fight Monster)\n2) Sleep (Restore HP for 5 gold)\n3) Quit")

    if user_input == "1":
        playerhp, gold = gamefunctions.battle(playerhp, gold, playerdamage)

    if user_input == "2":
        print(f"You sleep at the local tavern. \n-5 Gold")
        gold -= 5
        playerhp += 20
        loop()

    if user_input == "3":
        print(f"Thank you for playing, have a good day.")

    else:
        print("Invalid Input, Try again.")
        loop()

if __name__ == "__main__":
    loop()
