# Ryan Erno

# introduction to the game (title, scenario, etc.)

# "Enter" allows sentences to be read one at a time.

starting_messages = [
    "Alien Abduction The Game.\n",
    "You have been abducted and brought aboard an alien spaceship.",
    "Dazed and confused as you come to, you observe your surroundings.",

    "Within the room you have been contained in, your captor foolishly left one of the doors unlocked allowing you "
    "to enact your escape.",
    "Getting up, you head over to the open door and take a look, to the left the door is a displayed holo map "
    "showing multiple rooms of interest.",

    "For the best chance of escape, you deduce you will need:\n",
    "- A Laser gun from the Armory",
    "- A Space suit from the Airlock for protection",
    "- An Escape pod Manual from the Archives since you do not know how it works",
    "- A Translator from the War room to understand the alien language",
    "- The Keycard in the Control Room for the Escape pod back to Earth",
    "- A Snack from the Kitchen for the trip back home.\n",

    "You will have to face down the Alien Captain on the Main deck of the ship since he can easily shut down the "
    "escape pod to prevent use.\n",

]

# The dictionary links a room to other rooms. Items will be assigned accordingly.
rooms = {

    'Prisoner Room': {'East': 'Armory', 'Items': []},
    'Armory': {'West': 'Prisoner Room', 'East': 'Escape Pod', 'South': 'Archives', 'Items': ['Laser Gun']},
    'Escape Pod': {'West': 'Armory', 'Items': []},
    'Archives': {'West': 'Airlock', 'North': 'Armory', 'East': 'Control Room', 'South': 'War Room',
                 'Items': ['Manual']},
    'Airlock': {'East': 'Archives', 'Items': ['Spacesuit']},
    'Control Room': {'West': 'Archives', 'North': 'Main deck', 'Items': ['Keycard']},
    'Main Deck': {'South': 'Control Room', 'Items': []},
    'War Room': {'North': 'Archives', 'East': 'Kitchen', 'Items': ['Translator']},
    'Kitchen': {'West': 'War Room', 'Items': ['Snack']}
}
# following beyond this point is the main()

# Assign start point to Prisoner Room and provide player inventory.
Curr_room = 'Prisoner Room'
Player_inv = []


# Code identifies if an item exists and tells player before and after pickup and
# allows the player to check their inventory


def Item_in_room(local_room):
    global pickup_item  # < MISSING SOMETHING.
    if local_room in rooms:
        if 'Items' in rooms[local_room]:
            if rooms[local_room]['Items']:
                print("There is an item within the room!\n")
                while True:
                    # Strip() removes whitespace and title() caps 1st letters.
                    pickup_item = input(
                        "Enter name of item to pick up,\n'Inventory' to check current Items,\nor Direction to move." 
                        ">>>").strip().title()
                    if pickup_item in [item.title() for item in rooms[local_room]['Items']]:
                        Player_inv.append(pickup_item)
                        rooms[local_room]['Items'].remove(pickup_item)  # section added items to player and removed
                        print(f"You picked up the {pickup_item}.")  # from rooms inventory.
                        break
                    else:                                       # FIX INTERFERENCE: MUST PICK UP ITEM FIRST BEFORE
                        print("Item is not here!\n")            # ANOTHER COMMAND TO BE USED.
                    # inventory check per player request.
                    check = input("Enter 'Inventory' to check current items").split().title()
                    if check == 'Inventory':
                        if player_inv:
                            print("You have")
                            print(pickup_item)  # < MISSING SOMTHING (interfering with item pickup)

                        else:
                            print("you have no items")


# allows intro messages to print one at a time, better organized for the player.

# also tells when game officially begins.

print("Begin Game")
for messages in starting_messages:
    input(messages + "\npress enter to continue.....")


# This part gives player status updates. and allows exit if desired.
while True:
    if Curr_room == 'Exit':
        # Message is given and enter prompt provided so termination isn't instantaneous.
        input('Thank you for Playing!\nPress enter to Exit')
        # Break stops loop when exit condition is met
        break

    print(f'You currently are in The {Curr_room}.\n')
    Item_in_room(Curr_room)

    Player_move = input('Enter a direction >>>').strip().title()
    # Inputting 'exit' quits the game and stops loops
    if Player_move.lower() == 'exit':
        Curr_room = 'Exit'
        continue  # Skips the rest of the loop and moves to the rest.

    # Elif condition provides navigation validity.
    elif Player_move in rooms[Curr_room]:
        Curr_room = rooms[Curr_room][Player_move]

    # Else condition provides error message when invalid direction is given.
    else:
        print("You cannot go that way")


        # section was also supposed to  oversee "boss battle". win or loss determined by collection of all 6 items.
        # items < 6 = win  items > 6 = loss once boss is encountered
        # wanted game to officially terminate once they reached 'Escape pod' room after boss.


