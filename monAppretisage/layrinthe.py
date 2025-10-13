import os

def clear_screen():
    # for Windows
    _ = os.system('cls')
   
maze = (
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

step =  0
wall_hit = 0
visited_cells = 0.0
goal = False
valid_move = False
DIRECTION = ("w","a","s","d")
pos = (0,1)

def in_bound(next_pos,pos):
    if maze[next_pos[0]][next_pos[1]] == " ":
        pos = tuple(next_pos)
        return pos
    else:
        return pos

def try_move(move,pos):
    next_pos = list(pos)
    match move:
        case "w":
            next_pos[0]-=1
        case "a":
            next_pos[1]-=1
        case "s":
            next_pos[0]+=1
        case "d":
            next_pos[1]+=1
    pos = in_bound(next_pos,pos)
    return pos
        
def check(move,pos):
    move = move.lower()
    for d in DIRECTION:
        if move == d:
            pos = try_move(move,pos)
            return pos
            

def print_maze(maze, pos):
    y,x = pos
    for m in maze:
        if maze.index(m) == y :
            my_line = list(m)
            my_line[x] = "*"
            line = "".join(my_line)
            new_line= (str(line))
            print(new_line)
        else:
            print(m)

    print("number of steps : " + str(step))
    print("number of walls hit : " + str(wall_hit))
    print("Ratio empty cells visited: " + str(visited_cells) + " %")
    move = input("Direction (wasd) :")
    pos = check(move[0],pos)
    return pos

    
first = True
while not goal:
    valid_move = False
    if first:
        pos = print_maze(maze, pos)
        first = False

    if not valid_move:
        clear_screen()
        pos = print_maze(maze, pos)
    else:
        print("hola")

        