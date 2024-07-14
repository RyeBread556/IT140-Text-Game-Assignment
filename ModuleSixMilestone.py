
#ModuleSixMilestone.py
# Ryan Erno
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
}

# Provided greeting to let the player know game started.
print("Welcome to The Dragon-Themed Text Game\n")
print('To move Input "North", "South", "East" or "West"\n')


# assign start point within the Great Hall
Start_room = "Great Hall"


# Set room to be used in loop
Curr_room = Start_room

# Assigning the Current Room is needed to start game.
while True:
        print(f'You currently are in The {Curr_room}.')
        Player_move = input('Enter a direction >>>')
# inputting exit quits the game and stops loops
        if Player_move == 'Exit':
           Curr_room = 'Exit'
           # message is given and enter prompt provided so termination isnt instantaneous.
           input('Thank you for Playing!\nPress enter to Exit')
#break stops loop when exit condition is met
           break

# elif condition provides navigation validity.
        elif Player_move in rooms[Curr_room]:
                Curr_room = rooms[Curr_room][Player_move]

# else condition provides error message when invalid direction is given.
        else:
                print("you cannot go that way")

