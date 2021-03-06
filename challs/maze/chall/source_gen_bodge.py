## Kruskal's Algorithm for Maze Generation
## Neil Thistlethwaite

import numpy as np

global GRAPH_SIZE, CELL_THICKNESS, WALL_THICKNESS

## Maze generation parameters. Change as desired.
GRAPH_SIZE = 30
CELL_THICKNESS = 20
WALL_THICKNESS = 5

def pick_move(bindex):
    move = "exit(-1);"
    if bindex=='1':
        move = "return;"
    return move

def generate_validator(possible_moves):
    bits = format(possible_moves, "04b")
    called_from_up = pick_move(bits[-1])
    called_from_right = pick_move(bits[-2])
    called_from_down = pick_move(bits[-3])
    called_from_left = pick_move(bits[-4])

    function_template = f"""
void validator_{possible_moves}(void* this, void* calling, int offset, int width) {{
if (this - offset*width == calling) {{
        {called_from_up}
    }}
    else if (this + offset == calling) {{
        {called_from_right}
    }}
    else if (this + offset*width == calling) {{
        {called_from_down}
    }}
    else if (this - offset == calling) {{
        {called_from_left}
    }} else {{
        exit(-1);
    }}
}}
"""
    return function_template

def generate_function(i, j, possible_moves):
    bits = format(possible_moves, "04b")
    if i==0 and j==0: possible_moves = "start"
    #possible_moves = "debug"
    finish = "(this + right*offset + down*offset*width) (this, moves+1, offset);"
    #finish = "(this + offset) (this, moves+1, offset);"
    if i==29 and j ==29: finish = 'system("cat flag.txt");'
    function_template = f"""
void function_{i}_{j}(void* calling, char* moves, long int offset) {{
    int width = 30;
    void (*this) (void*, char*, long int) = function_{i}_{j};
    validator_{possible_moves}(this, calling, offset, width);
    char move = *moves;
    int down = 0;
    int right = 0;
    if (move == 'U') {{
        down = -1;
    }} else if (move == 'R') {{
        right = 1;
    }} else if (move == 'D') {{
        down = 1;
    }} else if (move == 'L') {{
        right = -1;
    }}
    {finish}
}}
"""
    return function_template

def print_bits(matrix):
    for ln in matrix:
        print('|', end=" ")
        for elt in ln:
            moves = ""
            if elt & 0x1 == 1:
                moves = "U" + moves
            if elt & 0x2 == 2:
                moves = "R" + moves
            if elt & 0x4 == 4:
                moves = "D" + moves
            if elt & 0x8 == 8:
                moves = "L" + moves
            while len(moves) < 4:
                moves = " " + moves
            print(moves, end=" ")
        print('|')

def get_move(cell_1, cell_2):
    #mirrored na normal axes
    if cell_1[0] == cell_2[0]:
        #x same, y change
        if cell_1[1] < cell_2[1]:
            #moved up
            return 1
        else:
            #moved down
            return 4
    else:
        #y same, x change
        if cell_1[0] < cell_2[0]:
            #moved right
            return 2
        else:
            #moved left
            return 8
            
def get_move_fucked(cell_1, cell_2):
    # LDRU
    if cell_1[0] == cell_2[0]:
        #fuckd up coord system
        #UD isto, LR change
        if cell_1[1] < cell_2[1]:
            #moved right
            return 2
        else:
            #moved left
            return 8
    else:
        #LR isto, UD bo change
        if cell_1[0] < cell_2[0]:
            #moved down
            return 4
        else:
            #moved up
            return 1


#print(maze)
#FIKSIRAJ
maze = [((3, 2), (2, 2)), ((26, 2), (25, 2)), ((14, 8), (13, 8)), ((23, 23), (24, 23)), ((23, 1), (24, 1)), ((8, 15), (7, 15)), ((8, 1), (7, 1)), ((1, 1), (2, 1)), ((5, 10), (4, 10)), ((16, 20), (16, 21)), ((18, 7), (19, 7)), ((3, 19), (3, 18)), ((1, 17), (0, 17)), ((10, 22), (9, 22)), ((8, 24), (7, 24)), ((26, 27), (26, 26)), ((1, 2), (2, 2)), ((10, 25), (11, 25)), ((12, 27), (13, 27)), ((21, 25), (21, 24)), ((3, 10), (3, 11)), ((17, 13), (17, 12)), ((26, 20), (26, 21)), ((20, 4), (20, 5)), ((2, 27), (3, 27)), ((4, 17), (4, 18)), ((17, 6), (17, 7)), ((7, 2), (8, 2)), ((9, 19), (10, 19)), ((23, 5), (24, 5)), ((11, 14), (11, 13)), ((21, 10), (20, 10)), ((29, 6), (28, 6)), ((21, 11), (20, 11)), ((20, 18), (21, 18)), ((19, 20), (19, 21)), ((12, 19), (13, 19)), ((11, 11), (12, 11)), ((7, 1), (6, 1)), ((11, 16), (11, 17)), ((18, 19), (19, 19)), ((24, 27), (25, 27)), ((26, 10), (27, 10)), ((2, 14), (3, 14)), ((3, 26), (4, 26)), ((18, 7), (18, 6)), ((12, 7), (12, 8)), ((2, 0), (2, 1)), ((11, 21), (10, 21)), ((0, 29), (0, 28)), ((7, 28), (8, 28)), ((6, 16), (6, 17)), ((26, 25), (26, 26)), ((11, 21), (12, 21)), ((9, 0), (9, 1)), ((11, 20), (12, 20)), ((23, 11), (23, 10)), ((18, 11), (18, 10)), ((16, 25), (15, 25)), ((13, 13), (14, 13)), ((16, 0), (16, 1)), ((22, 15), (22, 16)), ((29, 20), (29, 21)), ((6, 21), (6, 22)), ((18, 1), (18, 2)), ((21, 6), (20, 6)), ((20, 26), (20, 27)), ((0, 7), (1, 7)), ((28, 22), (28, 23)), ((20, 21), (20, 20)), ((7, 7), (6, 7)), ((12, 3), (12, 2)), ((2, 25), (2, 26)), ((11, 4), (10, 4)), ((7, 9), (7, 8)), ((9, 19), (9, 18)), ((14, 18), (13, 18)), ((9, 17), (10, 17)), ((15, 14), (14, 14)), ((6, 18), (5, 18)), ((27, 11), (27, 10)), ((22, 2), (23, 2)), ((29, 5), (29, 6)), ((3, 21), (3, 22)), ((22, 17), (23, 17)), ((23, 3), (24, 3)), ((13, 2), (14, 2)), ((22, 18), (22, 19)), ((27, 2), (27, 1)), ((3, 4), (4, 4)), ((14, 14), (14, 15)), ((10, 19), (10, 18)), ((23, 17), (24, 17)), ((10, 16), (10, 15)), ((5, 20), (6, 20)), ((23, 7), (23, 6)), ((29, 26), (28, 26)), ((6, 14), (5, 14)), ((19, 9), (19, 8)), ((0, 1), (0, 2)), ((4, 7), (5, 7)), ((0, 5), (1, 5)), ((19, 28), (20, 28)), ((4, 24), (5, 24)), ((4, 24), (4, 23)), ((9, 8), (8, 8)), ((14, 23), (14, 24)), ((18, 22), (18, 21)), ((13, 18), (13, 19)), ((21, 7), (21, 6)), ((29, 28), (28, 28)), ((5, 14), (4, 14)), ((0, 19), (1, 19)), ((16, 20), (15, 20)), ((15, 3), (16, 3)), ((27, 10), (27, 9)), ((18, 17), (18, 18)), ((15, 0), (14, 0)), ((17, 16), (16, 16)), ((9, 18), (9, 17)), ((14, 20), (13, 20)), ((20, 14), (20, 13)), ((10, 19), (10, 20)), ((19, 27), (20, 27)), ((12, 17), (11, 17)), ((6, 14), (6, 15)), ((10, 21), (9, 21)), ((3, 23), (3, 24)), ((18, 24), (18, 23)), ((7, 6), (6, 6)), ((18, 14), (19, 14)), ((27, 17), (26, 17)), ((22, 7), (22, 6)), ((16, 7), (17, 7)), ((24, 17), (25, 17)), ((4, 13), (4, 12)), ((2, 25), (2, 24)), ((2, 16), (1, 16)), ((6, 19), (6, 20)), ((10, 19), (11, 19)), ((22, 6), (23, 6)), ((17, 16), (18, 16)), ((8, 23), (9, 23)), ((6, 27), (7, 27)), ((26, 29), (26, 28)), ((5, 0), (4, 0)), ((24, 16), (24, 15)), ((14, 4), (14, 3)), ((26, 15), (25, 15)), ((25, 3), (24, 3)), ((9, 21), (8, 21)), ((9, 3), (10, 3)), ((16, 12), (17, 12)), ((24, 14), (24, 15)), ((6, 23), (6, 24)), ((9, 8), (9, 7)), ((16, 29), (15, 29)), ((16, 7), (16, 8)), ((13, 26), (14, 26)), ((9, 20), (10, 20)), ((25, 16), (26, 16)), ((13, 10), (12, 10)), ((24, 12), (24, 11)), ((18, 13), (18, 14)), ((10, 5), (9, 5)), ((18, 5), (17, 5)), ((22, 22), (22, 21)), ((21, 23), (21, 22)), ((14, 24), (13, 24)), ((24, 0), (24, 1)), ((1, 9), (0, 9)), ((10, 3), (11, 3)), ((4, 1), (5, 1)), ((6, 18), (6, 19)), ((17, 15), (18, 15)), ((25, 16), (25, 15)), ((5, 1), (5, 2)), ((19, 15), (20, 15)), ((15, 28), (14, 28)), ((20, 26), (21, 26)), ((13, 4), (14, 4)), ((1, 12), (0, 12)), ((17, 19), (18, 19)), ((28, 11), (28, 10)), ((28, 15), (28, 14)), ((9, 20), (9, 21)), ((26, 6), (25, 6)), ((21, 20), (21, 21)), ((7, 18), (6, 18)), ((21, 20), (20, 20)), ((6, 24), (6, 25)), ((12, 26), (12, 25)), ((4, 13), (5, 13)), ((6, 17), (5, 17)), ((8, 20), (8, 21)), ((27, 6), (28, 6)), ((24, 5), (25, 5)), ((12, 4), (12, 3)), ((17, 1), (17, 0)), ((14, 21), (13, 21)), ((1, 21), (2, 21)), ((22, 25), (23, 25)), ((4, 29), (3, 29)), ((22, 0), (22, 1)), ((0, 17), (0, 18)), ((4, 10), (3, 10)), ((6, 17), (6, 18)), ((13, 25), (14, 25)), ((27, 3), (27, 4)), ((19, 22), (19, 23)), ((16, 27), (15, 27)), ((12, 20), (13, 20)), ((27, 13), (27, 14)), ((29, 0), (28, 0)), ((24, 12), (23, 12)), ((26, 8), (26, 7)), ((17, 8), (17, 9)), ((4, 27), (4, 28)), ((19, 10), (18, 10)), ((21, 26), (22, 26)), ((2, 22), (1, 22)), ((11, 24), (11, 23)), ((25, 26), (26, 26)), ((26, 15), (26, 14)), ((4, 9), (4, 8)), ((29, 28), (29, 29)), ((2, 29), (2, 28)), ((20, 15), (20, 14)), ((10, 15), (10, 14)), ((6, 11), (6, 10)), ((3, 24), (3, 25)), ((4, 14), (4, 13)), ((19, 6), (19, 7)), ((25, 15), (25, 14)), ((10, 21), (10, 22)), ((13, 23), (13, 22)), ((1, 23), (2, 23)), ((17, 15), (16, 15)), ((10, 5), (11, 5)), ((7, 9), (7, 10)), ((18, 24), (17, 24)), ((9, 4), (10, 4)), ((29, 0), (29, 1)), ((12, 3), (13, 3)), ((5, 7), (6, 7)), ((12, 18), (13, 18)), ((7, 0), (6, 0)), ((11, 2), (11, 1)), ((17, 17), (18, 17)), ((4, 1), (3, 1)), ((6, 25), (5, 25)), ((23, 1), (23, 2)), ((7, 2), (6, 2)), ((5, 23), (5, 24)), ((18, 29), (17, 29)), ((9, 14), (9, 13)), ((24, 26), (23, 26)), ((27, 12), (27, 13)), ((11, 16), (11, 15)), ((15, 22), (16, 22)), ((29, 24), (29, 23)), ((19, 25), (19, 24)), ((14, 9), (14, 8)), ((21, 26), (21, 25)), ((19, 17), (20, 17)), ((4, 17), (5, 17)), ((19, 6), (20, 6)), ((22, 21), (22, 20)), ((23, 17), (23, 16)), ((12, 10), (12, 9)), ((20, 5), (19, 5)), ((13, 19), (13, 20)), ((1, 17), (1, 18)), ((15, 3), (15, 4)), ((7, 27), (7, 28)), ((8, 8), (7, 8)), ((1, 15), (2, 15)), ((20, 11), (20, 12)), ((1, 27), (2, 27)), ((18, 10), (18, 9)), ((27, 22), (28, 22)), ((22, 20), (22, 19)), ((26, 23), (27, 23)), ((19, 17), (18, 17)), ((14, 15), (15, 15)), ((14, 3), (14, 2)), ((20, 16), (21, 16)), ((2, 23), (3, 23)), ((15, 7), (15, 8)), ((11, 20), (11, 19)), ((19, 16), (19, 15)), ((25, 16), (25, 17)), ((0, 25), (0, 26)), ((7, 8), (7, 7)), ((16, 15), (16, 16)), ((27, 29), (28, 29)), ((21, 8), (20, 8)), ((5, 19), (4, 19)), ((26, 5), (25, 5)), ((15, 28), (15, 29)), ((21, 17), (20, 17)), ((10, 11), (11, 11)), ((29, 3), (29, 4)), ((6, 13), (7, 13)), ((16, 10), (16, 9)), ((5, 24), (5, 25)), ((12, 29), (13, 29)), ((9, 13), (10, 13)), ((21, 19), (20, 19)), ((4, 14), (4, 15)), ((18, 27), (18, 28)), ((27, 4), (27, 5)), ((19, 21), (20, 21)), ((28, 4), (27, 4)), ((27, 29), (26, 29)), ((11, 24), (10, 24)), ((21, 20), (21, 19)), ((7, 4), (8, 4)), ((24, 19), (25, 19)), ((9, 0), (10, 0)), ((9, 23), (9, 24)), ((12, 21), (13, 21)), ((3, 16), (3, 15)), ((1, 29), (2, 29)), ((5, 27), (6, 27)), ((7, 16), (8, 16)), ((25, 20), (25, 21)), ((27, 18), (28, 18)), ((23, 25), (23, 26)), ((22, 3), (22, 4)), ((25, 13), (25, 12)), ((11, 29), (10, 29)), ((4, 6), (4, 7)), ((29, 10), (29, 11)), ((20, 17), (20, 18)), ((9, 26), (10, 26)), ((16, 21), (17, 21)), ((16, 19), (16, 18)), ((17, 12), (17, 11)), ((28, 21), (28, 22)), ((7, 17), (6, 17)), ((10, 10), (11, 10)), ((17, 1), (17, 2)), ((14, 20), (14, 19)), ((3, 0), (3, 1)), ((28, 1), (28, 0)), ((19, 3), (18, 3)), ((21, 1), (21, 2)), ((27, 16), (27, 17)), ((0, 6), (0, 5)), ((21, 27), (21, 28)), ((1, 24), (1, 23)), ((27, 25), (27, 24)), ((22, 15), (21, 15)), ((8, 11), (8, 12)), ((4, 9), (3, 9)), ((13, 13), (13, 14)), ((23, 20), (23, 19)), ((9, 26), (9, 25)), ((2, 7), (2, 6)), ((14, 3), (15, 3)), ((1, 26), (1, 25)), ((0, 21), (1, 21)), ((20, 29), (20, 28)), ((27, 22), (27, 21)), ((23, 10), (23, 9)), ((16, 17), (15, 17)), ((2, 0), (3, 0)), ((3, 6), (4, 6)), ((10, 16), (10, 17)), ((27, 11), (26, 11)), ((17, 29), (17, 28)), ((25, 22), (26, 22)), ((5, 6), (6, 6)), ((21, 22), (22, 22)), ((8, 17), (9, 17)), ((8, 28), (8, 29)), ((20, 29), (19, 29)), ((11, 7), (11, 6)), ((26, 9), (26, 8)), ((24, 24), (24, 25)), ((2, 14), (1, 14)), ((6, 3), (5, 3)), ((16, 4), (16, 3)), ((11, 22), (10, 22)), ((21, 0), (20, 0)), ((20, 13), (20, 12)), ((27, 11), (27, 12)), ((17, 3), (17, 4)), ((5, 19), (5, 18)), ((28, 27), (29, 27)), ((5, 2), (5, 3)), ((18, 11), (19, 11)), ((22, 10), (22, 9)), ((25, 5), (25, 6)), ((23, 4), (24, 4)), ((12, 13), (12, 14)), ((20, 7), (20, 6)), ((9, 3), (8, 3)), ((7, 19), (8, 19)), ((1, 24), (2, 24)), ((4, 29), (5, 29)), ((14, 9), (14, 10)), ((2, 10), (1, 10)), ((0, 22), (0, 23)), ((21, 10), (21, 11)), ((14, 6), (14, 5)), ((8, 20), (7, 20)), ((14, 2), (15, 2)), ((27, 6), (27, 5)), ((17, 17), (17, 18)), ((29, 15), (29, 16)), ((1, 28), (1, 27)), ((21, 24), (20, 24)), ((8, 4), (8, 5)), ((6, 9), (6, 10)), ((24, 28), (24, 27)), ((25, 24), (24, 24)), ((15, 19), (15, 20)), ((9, 16), (9, 15)), ((1, 24), (0, 24)), ((10, 28), (11, 28)), ((15, 20), (14, 20)), ((17, 22), (17, 23)), ((4, 2), (4, 1)), ((8, 27), (9, 27)), ((9, 10), (9, 9)), ((25, 12), (26, 12)), ((8, 4), (8, 3)), ((24, 9), (24, 10)), ((20, 19), (20, 18)), ((23, 12), (22, 12)), ((8, 19), (8, 20)), ((7, 21), (7, 20)), ((7, 25), (8, 25)), ((28, 23), (29, 23)), ((3, 21), (3, 20)), ((23, 13), (22, 13)), ((27, 11), (28, 11)), ((29, 28), (29, 27)), ((20, 15), (21, 15)), ((14, 9), (13, 9)), ((17, 29), (16, 29)), ((4, 24), (3, 24)), ((0, 1), (0, 0)), ((24, 28), (25, 28)), ((3, 28), (2, 28)), ((17, 8), (17, 7)), ((6, 5), (6, 6)), ((18, 14), (18, 15)), ((20, 24), (19, 24)), ((12, 7), (12, 6)), ((5, 1), (6, 1)), ((3, 28), (4, 28)), ((22, 5), (22, 6)), ((22, 17), (22, 18)), ((21, 28), (20, 28)), ((25, 18), (25, 19)), ((11, 3), (12, 3)), ((11, 2), (12, 2)), ((11, 11), (11, 12)), ((19, 13), (19, 12)), ((16, 22), (16, 21)), ((7, 14), (7, 13)), ((23, 0), (23, 1)), ((25, 2), (24, 2)), ((19, 18), (18, 18)), ((2, 12), (1, 12)), ((29, 24), (28, 24)), ((29, 22), (29, 23)), ((26, 2), (27, 2)), ((25, 27), (25, 26)), ((26, 23), (25, 23)), ((25, 7), (26, 7)), ((4, 5), (5, 5)), ((19, 0), (20, 0)), ((18, 20), (18, 21)), ((1, 14), (0, 14)), ((19, 25), (18, 25)), ((4, 27), (5, 27)), ((9, 27), (10, 27)), ((5, 10), (6, 10)), ((24, 8), (25, 8)), ((12, 23), (13, 23)), ((3, 7), (4, 7)), ((27, 26), (27, 25)), ((15, 16), (14, 16)), ((27, 27), (27, 26)), ((29, 21), (28, 21)), ((22, 13), (22, 12)), ((26, 29), (25, 29)), ((23, 8), (23, 9)), ((14, 28), (14, 27)), ((22, 24), (21, 24)), ((19, 17), (19, 16)), ((26, 13), (26, 14)), ((14, 1), (15, 1)), ((11, 29), (12, 29)), ((13, 5), (14, 5)), ((29, 16), (28, 16)), ((29, 14), (29, 15)), ((20, 24), (20, 23)), ((16, 14), (16, 13)), ((23, 15), (23, 14)), ((21, 28), (22, 28)), ((16, 3), (16, 2)), ((10, 8), (10, 9)), ((17, 25), (18, 25)), ((17, 3), (16, 3)), ((7, 0), (8, 0)), ((3, 22), (2, 22)), ((19, 26), (19, 25)), ((26, 18), (26, 17)), ((8, 23), (7, 23)), ((19, 12), (18, 12)), ((15, 24), (14, 24)), ((8, 18), (8, 19)), ((10, 26), (10, 27)), ((25, 4), (24, 4)), ((7, 4), (7, 5)), ((5, 16), (5, 15)), ((22, 20), (23, 20)), ((9, 24), (8, 24)), ((6, 1), (6, 0)), ((26, 20), (25, 20)), ((28, 8), (27, 8)), ((19, 24), (19, 23)), ((16, 24), (16, 23)), ((5, 27), (5, 26)), ((13, 3), (14, 3)), ((18, 14), (17, 14)), ((4, 10), (4, 11)), ((8, 14), (9, 14)), ((1, 11), (1, 10)), ((8, 11), (7, 11)), ((4, 22), (4, 21)), ((14, 28), (13, 28)), ((6, 28), (6, 29)), ((5, 10), (5, 9)), ((8, 6), (9, 6)), ((10, 6), (10, 7)), ((9, 25), (10, 25)), ((15, 9), (15, 10)), ((22, 28), (23, 28)), ((13, 4), (13, 5)), ((11, 5), (11, 4)), ((6, 27), (6, 26)), ((10, 3), (10, 4)), ((29, 15), (28, 15)), ((1, 28), (0, 28)), ((19, 28), (18, 28)), ((19, 21), (19, 22)), ((10, 12), (10, 11)), ((20, 27), (20, 28)), ((15, 17), (14, 17)), ((9, 13), (9, 12)), ((1, 8), (1, 9)), ((8, 10), (9, 10)), ((26, 4), (25, 4)), ((6, 23), (6, 22)), ((3, 22), (4, 22)), ((5, 12), (5, 11)), ((4, 8), (5, 8)), ((1, 23), (1, 22)), ((13, 5), (13, 6)), ((26, 20), (26, 19)), ((0, 22), (1, 22)), ((7, 16), (7, 15)), ((25, 8), (25, 7)), ((1, 4), (0, 4)), ((21, 2), (21, 3)), ((1, 28), (1, 29)), ((27, 5), (28, 5)), ((8, 7), (7, 7)), ((19, 8), (19, 7)), ((13, 27), (14, 27)), ((7, 7), (7, 6)), ((27, 18), (27, 19)), ((29, 14), (29, 13)), ((7, 5), (6, 5)), ((17, 13), (16, 13)), ((7, 15), (6, 15)), ((12, 10), (11, 10)), ((9, 2), (9, 3)), ((2, 4), (1, 4)), ((4, 16), (5, 16)), ((11, 9), (11, 8)), ((25, 21), (24, 21)), ((23, 16), (23, 15)), ((28, 4), (29, 4)), ((8, 8), (8, 9)), ((22, 22), (23, 22)), ((16, 19), (16, 20)), ((1, 15), (1, 16)), ((7, 24), (6, 24)), ((24, 25), (23, 25)), ((14, 12), (15, 12)), ((17, 22), (18, 22)), ((8, 9), (9, 9)), ((21, 22), (21, 21)), ((27, 15), (26, 15)), ((13, 10), (13, 9)), ((4, 20), (3, 20)), ((5, 11), (6, 11)), ((18, 6), (17, 6)), ((15, 6), (14, 6)), ((23, 22), (23, 23)), ((5, 29), (6, 29)), ((29, 10), (29, 9)), ((12, 28), (12, 27)), ((14, 7), (14, 6)), ((0, 2), (1, 2)), ((15, 12), (16, 12)), ((16, 11), (16, 12)), ((24, 28), (24, 29)), ((2, 18), (2, 19)), ((21, 12), (21, 11)), ((16, 9), (17, 9)), ((2, 5), (2, 6)), ((13, 27), (13, 26)), ((2, 9), (3, 9)), ((22, 21), (23, 21)), ((0, 13), (0, 12)), ((0, 13), (0, 14)), ((20, 1), (21, 1)), ((17, 26), (18, 26)), ((24, 4), (24, 3)), ((4, 2), (4, 3)), ((4, 7), (4, 8)), ((3, 2), (3, 3)), ((15, 28), (15, 27)), ((4, 10), (4, 9)), ((26, 9), (25, 9)), ((26, 0), (27, 0)), ((27, 24), (27, 23)), ((24, 19), (24, 20)), ((1, 25), (0, 25)), ((17, 25), (17, 24)), ((12, 5), (12, 4)), ((19, 1), (19, 2)), ((22, 11), (23, 11)), ((7, 27), (7, 26)), ((19, 9), (18, 9)), ((5, 13), (6, 13)), ((19, 20), (18, 20)), ((17, 17), (16, 17)), ((14, 11), (15, 11)), ((5, 4), (5, 5)), ((15, 21), (16, 21)), ((7, 13), (7, 12)), ((29, 9), (29, 8)), ((11, 18), (12, 18)), ((10, 7), (9, 7)), ((26, 23), (26, 24)), ((1, 24), (1, 25)), ((6, 8), (6, 7)), ((7, 16), (6, 16)), ((24, 12), (24, 13)), ((23, 8), (24, 8)), ((0, 10), (1, 10)), ((21, 15), (21, 14)), ((21, 14), (21, 13)), ((5, 21), (4, 21)), ((19, 5), (19, 4)), ((10, 23), (11, 23)), ((24, 5), (24, 4)), ((3, 26), (3, 27)), ((9, 16), (8, 16)), ((0, 13), (1, 13)), ((22, 22), (22, 23)), ((28, 25), (29, 25)), ((22, 14), (22, 13)), ((1, 1), (1, 2)), ((10, 8), (10, 7)), ((26, 6), (26, 7)), ((13, 24), (13, 23)), ((1, 6), (2, 6)), ((21, 27), (22, 27)), ((6, 26), (6, 25)), ((24, 7), (24, 6)), ((12, 27), (11, 27)), ((8, 22), (9, 22)), ((2, 17), (1, 17)), ((11, 0), (10, 0)), ((13, 0), (12, 0)), ((25, 22), (25, 23)), ((9, 6), (9, 7)), ((14, 7), (15, 7)), ((20, 12), (19, 12)), ((12, 23), (12, 22)), ((17, 25), (17, 26)), ((23, 18), (22, 18)), ((24, 8), (24, 7)), ((9, 16), (10, 16)), ((27, 7), (28, 7)), ((8, 24), (8, 25)), ((5, 4), (6, 4)), ((18, 2), (18, 3)), ((24, 11), (24, 10)), ((29, 19), (29, 18)), ((0, 20), (1, 20)), ((0, 4), (0, 5)), ((28, 3), (28, 4)), ((12, 8), (12, 9)), ((11, 1), (11, 0)), ((15, 9), (14, 9)), ((2, 19), (2, 20)), ((2, 6), (3, 6)), ((17, 6), (17, 5)), ((0, 10), (0, 9)), ((3, 5), (2, 5)), ((27, 0), (27, 1)), ((11, 6), (11, 5)), ((7, 3), (7, 2)), ((8, 3), (7, 3)), ((16, 24), (17, 24)), ((29, 12), (29, 11)), ((25, 29), (25, 28)), ((22, 0), (23, 0)), ((16, 28), (15, 28)), ((28, 0), (27, 0)), ((24, 15), (25, 15)), ((22, 12), (22, 11)), ((26, 24), (26, 25)), ((19, 8), (18, 8)), ((14, 12), (13, 12)), ((17, 10), (16, 10)), ((4, 24), (4, 25)), ((14, 16), (14, 17)), ((2, 2), (2, 3)), ((28, 16), (27, 16)), ((5, 12), (6, 12)), ((8, 22), (7, 22)), ((26, 3), (26, 4)), ((13, 16), (14, 16)), ((20, 3), (20, 4)), ((29, 13), (29, 12)), ((15, 25), (14, 25)), ((2, 29), (3, 29)), ((1, 15), (0, 15)), ((16, 14), (16, 15)), ((15, 16), (15, 15)), ((5, 21), (5, 20)), ((11, 26), (10, 26)), ((4, 4), (4, 3)), ((18, 2), (17, 2)), ((15, 1), (15, 0)), ((23, 13), (23, 14)), ((11, 28), (12, 28)), ((10, 29), (9, 29)), ((0, 20), (0, 21)), ((24, 22), (23, 22)), ((26, 28), (27, 28)), ((29, 8), (28, 8)), ((18, 18), (18, 19)), ((5, 22), (5, 21)), ((13, 7), (13, 6)), ((0, 11), (0, 10)), ((0, 18), (0, 19)), ((9, 12), (8, 12)), ((10, 13), (10, 12)), ((15, 5), (14, 5)), ((12, 24), (12, 23)), ((23, 2), (23, 3)), ((18, 11), (17, 11)), ((3, 16), (4, 16)), ((21, 29), (22, 29)), ((10, 13), (11, 13)), ((12, 25), (11, 25)), ((13, 29), (13, 28)), ((15, 13), (15, 12)), ((27, 20), (28, 20)), ((20, 5), (20, 6)), ((22, 5), (23, 5)), ((12, 6), (12, 5)), ((27, 19), (26, 19)), ((29, 7), (29, 8)), ((8, 26), (8, 25)), ((9, 27), (9, 28)), ((17, 3), (17, 2)), ((17, 5), (17, 4)), ((3, 4), (3, 5)), ((13, 16), (13, 17)), ((28, 11), (29, 11)), ((9, 28), (9, 29)), ((24, 23), (24, 24)), ((3, 19), (4, 19)), ((21, 22), (20, 22)), ((26, 22), (27, 22)), ((7, 29), (6, 29)), ((14, 12), (14, 13)), ((16, 16), (15, 16)), ((1, 14), (1, 15)), ((20, 9), (21, 9)), ((23, 28), (24, 28)), ((24, 3), (24, 2)), ((5, 15), (6, 15)), ((22, 5), (21, 5)), ((4, 5), (4, 6)), ((11, 15), (12, 15)), ((7, 11), (6, 11)), ((15, 23), (16, 23)), ((5, 12), (5, 13)), ((11, 8), (12, 8)), ((25, 1), (26, 1)), ((13, 1), (13, 0)), ((26, 9), (27, 9)), ((2, 21), (2, 22)), ((1, 9), (2, 9)), ((20, 9), (20, 10)), ((23, 25), (23, 24)), ((21, 8), (21, 9)), ((28, 25), (27, 25)), ((24, 29), (23, 29)), ((15, 26), (16, 26)), ((21, 3), (21, 4)), ((4, 17), (3, 17)), ((28, 12), (29, 12)), ((19, 16), (20, 16)), ((22, 8), (22, 7)), ((0, 3), (0, 2)), ((23, 26), (23, 27)), ((1, 20), (2, 20)), ((21, 1), (21, 0)), ((28, 19), (27, 19)), ((13, 10), (13, 11)), ((28, 7), (28, 6)), ((18, 29), (18, 28)), ((4, 0), (4, 1)), ((0, 12), (0, 11)), ((28, 8), (28, 7)), ((1, 3), (2, 3)), ((18, 0), (17, 0)), ((12, 22), (12, 21)), ((27, 17), (28, 17)), ((16, 6), (15, 6)), ((24, 19), (23, 19)), ((16, 1), (16, 2)), ((18, 2), (19, 2)), ((14, 2), (14, 1)), ((19, 2), (20, 2)), ((13, 2), (13, 1)), ((17, 20), (17, 19)), ((25, 19), (25, 20)), ((13, 29), (14, 29)), ((1, 6), (1, 5)), ((23, 18), (24, 18)), ((27, 28), (28, 28)), ((22, 10), (22, 11)), ((13, 24), (13, 25)), ((29, 19), (28, 19)), ((12, 12), (12, 13)), ((22, 2), (21, 2)), ((20, 25), (20, 24)), ((25, 0), (25, 1)), ((14, 11), (14, 12)), ((25, 13), (26, 13)), ((15, 19), (15, 18)), ((25, 11), (25, 10)), ((13, 1), (12, 1)), ((21, 28), (21, 29)), ((12, 16), (12, 15)), ((12, 13), (11, 13)), ((10, 15), (11, 15)), ((10, 1), (10, 2)), ((5, 29), (5, 28)), ((2, 11), (2, 12)), ((10, 1), (9, 1)), ((0, 26), (0, 27)), ((1, 19), (2, 19)), ((11, 25), (11, 24)), ((28, 13), (29, 13)), ((15, 26), (14, 26)), ((25, 10), (24, 10)), ((0, 0), (1, 0)), ((29, 27), (29, 26)), ((28, 3), (28, 2)), ((29, 17), (28, 17)), ((28, 9), (29, 9)), ((14, 22), (13, 22)), ((17, 28), (17, 27)), ((9, 11), (10, 11)), ((3, 14), (3, 13)), ((25, 1), (24, 1)), ((27, 20), (27, 21)), ((7, 13), (8, 13)), ((3, 12), (4, 12)), ((18, 3), (18, 4)), ((3, 8), (4, 8)), ((2, 13), (2, 14)), ((14, 15), (13, 15)), ((16, 5), (16, 6)), ((25, 26), (25, 25)), ((0, 8), (1, 8)), ((22, 5), (22, 4)), ((1, 6), (1, 7)), ((2, 8), (1, 8)), ((1, 16), (0, 16)), ((29, 2), (28, 2))]

maze_matrix = np.zeros((GRAPH_SIZE, GRAPH_SIZE), dtype="byte")
#bit0 = can go up, bit1 = can go right, bit2 = can go down, bit3 = can go left, npr. 1010 = A : can go right and left
for edge in maze:
    cell_1 = edge[0]
    cell_2 = edge[1]
    #LDRU
    move = get_move_fucked(cell_1, cell_2)
    maze_matrix[cell_1[0]][cell_1[1]] = maze_matrix[cell_1[0]][cell_1[1]] | move
    move_complement = move << 2

    if move_complement > 8:
        move_complement = move_complement >> 4
    #print(f"move {move}, comp {move_complement}")
    maze_matrix[cell_2[0]][cell_2[1]] = maze_matrix[cell_2[0]][cell_2[1]] | move_complement
#works

header = """
#include <stdio.h>
#include <stdlib.h>

"""
print(header)

for i in range(16):
    print(generate_validator(i))

start_val = """
void validator_start(void* this,  void* calling, int offset, int width) {
    return;
}
"""
print(start_val)
debug_val = """
void validator_debug(void* this, void* calling, int offset, int width) {
    printf("from function %p jumping to %p\\n", calling, this);
}
"""
#print(debug_val)

#print(maze_matrix)

for i, ln in enumerate(maze_matrix):
    for j, elt in enumerate(ln):
        #fun_i_j : i-ta vrstica, j-ti stolpec
        print(generate_function(i,j,elt))
        #print(generate_prints(j,i))

int_main = """
int main() {
    char input[100];
"""
print(int_main)

#for i in range(30):
    #for j in range(30):
        #print(f"p[{j}][{i}] = function_{j}_{i};")
binb_main = """
    
    long int offset = function_0_1 - function_0_0;   
    //int offset = 220;
    printf("The outside world awaits.\\n");
    scanf(\"%100s\", input);
    function_0_0(main, input, offset);
}
"""
print(binb_main)
