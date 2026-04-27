import gamefunctions
import json
import os
import random
from wanderingmonster import wanderingmonster

playerhp = 300
gold = 50
playerdamage = 25
map_state = {"player_pos": [0, 0],"town_pos": [0, 0],"has_left_town": False,"monsters": [wanderingmonster.random_spawn(occupied=[],forbidden=[(0, 0)],grid_w=10,grid_h=10)]}
player_inventory = [{"name": "Charm of Home", "desc": "A charm given to you by your mother before leaving as a good luck token, has no effects.", "type": "trinket"}, ]
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
    global playerhp, gold, playerdamage, player_inventory, equipped, map_state
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
                    playerhp, gold, playerdamage, player_inventory, equipped, map_state = loaded
                    break
                else:
                    print("Save file not found. Try again.")

            if filename.lower() != "back":
                break

        else:
            print("Invalid input, try again.")

    while running:
        user_input = input(f"You are in town.\n Current HP: {playerhp}, Current Gold: {gold}\nWhat would you like to do?\n1) Leave town (Explore the Map!)\n2) Sleep (Restore HP for 5 gold)\n3) Go to the Store\n4) View Inventory\n5) Quit\n6) Save Game")

        if user_input == "1":
            result, map_state = gamefunctions.map_interface(map_state)

            if result == "town":
                print("You returned to town.")

            elif result == "monster":
                playerhp, gold, playerdamage, player_inventory, equipped, result = gamefunctions.battle(playerhp, gold, playerdamage, player_inventory, equipped)
                map_state["monsters"] = [monster for monster in map_state["monsters"] if [monster.x, monster.y] != map_state["player_pos"]]

                if len(map_state["monsters"]) == 0:
                    for _ in range(2):
                        occupied = [(monster.x, monster.y) for monster in map_state["monsters"]]
                        forbidden = [tuple(map_state["player_pos"]),tuple(map_state["town_pos"])]

                        new_monster = gamefunctions.wanderingmonster.random_spawn(occupied,forbidden,10,10)

                        map_state["monsters"].append(new_monster)
                        
                if result == "ran":
                    map_state["player_pos"] = map_state["town_pos"]
                    map_state["has_left_town"] = False
                    print("You flee back to town!")
                    
                if result == "ko":
                    map_state["player_pos"] = map_state["town_pos"]
                    map_state["has_left_town"] = False
                    print("You were knocked unconcious and woke up in town!")

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
            gamefunctions.save_game(filename, playerhp, gold, playerdamage, player_inventory, equipped, map_state)

        else:
            print("Invalid input, try again.")
            
if __name__ == "__main__":
    loop()
