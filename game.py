import gamefunctions
import json
import os

playerhp = 300
gold = 50
playerdamage = 25
player_inventory =  [{"name": "Charm of Home", "desc": "A charm given to you by your mother before leaving as a good luck token, has no effects.", "type": "trinket"},]
equipped = None

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
    global playerhp, gold, playerdamage, player_inventory, equipped
    running = True

    while True:
        choice = input("1) New Game\n2) Load Game\n")

        if choice == "1":
            print("Starting new game...")
            break

        elif choice == "2":
            while True:
                filename = input("Enter save file name (or type 'back' to return): ")

                if filename.lower() == "back":
                    break

                loaded = gamefunctions.load_game(filename)

                if loaded:
                    playerhp, gold, playerdamage, player_inventory, equipped = loaded
                    break
                else:
                    print("Save file not found. Try again.")

            if filename.lower() != "back":
                break

        else:
            print("Invalid input, try again.")

    while running:
        user_input = input(f"You are in town.\n Current HP: {playerhp}, Current Gold: {gold}\nWhat would you like to do?\n1) Leave town (Fight Monster)\n2) Sleep (Restore HP for 5 gold)\n3) Go to the Store\n4) View Inventory\n5) Quit\n6) Save Game")

        if user_input == "1":
            playerhp, gold, playerdamage, player_inventory, equipped = gamefunctions.battle(
                playerhp, gold, playerdamage, player_inventory, equipped
            )

        elif user_input == "2":
            print("You sleep at the local tavern.\n-5 Gold")
            gold -= 5
            playerhp += 20

        elif user_input == "3":
            gold = gamefunctions.shoploop(gold, player_inventory)
            print("Gold now:", gold)
            gamefunctions.printinv(player_inventory)

        elif user_input == "4":
            gamefunctions.printinv(player_inventory)

        elif user_input == "5":
            print("Thank you for playing, have a good day.")
            running = False

        elif user_input == "6":
            filename = input("Enter filename to save: ")
            gamefunctions.save_game(filename, playerhp, gold, playerdamage, player_inventory, equipped)

        else:
            print("Invalid input, try again.")
            
if __name__ == "__main__":
    loop()
