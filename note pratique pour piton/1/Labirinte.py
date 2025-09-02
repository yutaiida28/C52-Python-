maze_clear = False

maze = ( #tuple 
    '┌S┬────────────────┬───────────┐',
    '│ │                │           G',
    '│ │ ┌─────┐ ┌───┬──┘ ┌───┬───┬─┤',
    '│ └─┘     │ │   │    │   │   │ │',
    '│     ┌─┐ │ │ │ │ ┌──┘ │ │ │ │ │',
    '│ ┌── │ │ │ │ │ │ │    │   │   │',
    '│ │   │   │ │ │ │ │ ┌──┴─┬─┴─┐ │',
    '│ │ ──┴───┘ │ │ │ │ │    │   │ │',
    '│ │         │ │   │ │  │ │ │ │ │',
    '│ └─────────┘ └───┴─┘  │ │ │ │ │',
    '│                      │   │   │',
    '└──────────────────────┴───┴───┘',
)

step_counter = int(0)
wall_hit = int(0)

moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
pos = (1,1)

while not maze_clear:
    for i in maze:
        print(i)
    valid_move = False
    
    while not valid_move:
        char = input("use wasd to reach the goal :")
        print(pos)
        if char in "wasd":
            step_counter += 1
            valid_move = True
        else:
            print("that not a valid move try again")
            step_counter += 1
    if char == "W":
        if pos[0] == 1:
            break
        else:
            pos- moves['w']
    elif char == "a":
        pass
    elif char == "s":
        if pos[0] == 11:
            break
        else:
            pos += moves['s']    
    else:
        pass