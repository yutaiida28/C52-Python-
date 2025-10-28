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
visited_cell = 0.0
case_vide = None
goal = False
valid_move = False
visited_cells = set([])
DIRECTION = ("w","a","s","d")
pos = (0,1)

def in_bound(next_pos,pos,goal):

    if maze[next_pos[0]][next_pos[1]] == " ":
        pos = tuple(next_pos)
        
    if maze[next_pos[0]][next_pos[1]] == "G":
        goal = True

        
    return pos, goal

def try_move(move,pos, goal):
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
    pos, goal = in_bound(next_pos, pos, goal)
    return pos, goal
        
def check(move, pos, goal):
    if move != "":
        move = move[0]
        move = move.lower()
        for d in DIRECTION:
            if move == d:
                pos, goal = try_move(move, pos, goal)

    return pos, goal

def occurences_case_vide():
    case_vide = 0
    for m in maze:
        case_vide += m.count(" ")
    return case_vide

def visited():
    return round(len(visited_cells)/case_vide * 100,1)

def print_maze(pos, goal, wall_hit,step):
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
    print("Ratio empty cells visited: " + str(visited()) + " %")
    move = input("Direction (wasd) :")
    pos2, goal = check(move,pos, goal)
    if pos == pos2:
        wall_hit += 1
    else:
        step += 1
    return pos2, goal, wall_hit,step

    
case_vide = occurences_case_vide()
while not goal:
    
    if not valid_move:
        clear_screen()
        pos,goal, wall_hit, step = print_maze(pos, goal, wall_hit,step)
        visited_cells.add(pos)
    else:
        print("hola")

clear_screen()
print("victoir !!!!")
        