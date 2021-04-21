board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

step = 0


def print_board():
    print(9 * '-')
    print(f"| {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"| {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"| {board[2][0]} {board[2][1]} {board[2][2]} |")
    print(9 * '-')


print_board()

while True:
    coords = input('Enter the coordinates: ').split()
    if coords and len(coords) == 1 and coords[0].isdigit():
        print('You should enter two coordinates')
    elif coords and coords[0].isdigit() and coords[1].isdigit():
        if int(coords[0]) not in range(1, 4) or int(coords[1]) not in range(1, 4):
            print('Coordinates should be from 1 to 3!')
        elif board[int(coords[0]) - 1][int(coords[1]) - 1] in ("X", "O"):
            print('This cell is occupied! Choose another one!')
        else:
            if step == 0:
                board[(int(coords[0]) - 1)][(int(coords[1]) - 1)] = 'X'
                print_board()
                step = 1
            else:
                board[(int(coords[0]) - 1)][(int(coords[1]) - 1)] = 'O'
                print_board()
                step = 0
    else:
        print('You should enter numbers!')

    flat_board = ''.join(''.join(i for i in lst) for lst in board)
    lines = [flat_board[0:3], flat_board[3:6], flat_board[6:], flat_board[0:9:3], flat_board[1:9:3], flat_board[2:9:3],
             flat_board[0:9:4], flat_board[2:7:2]]

    if 'XXX' in lines:
        print('X wins')
        break
    elif 'OOO' in lines:
        print('O wins')
        break
    elif flat_board.count('_') == 0:
        print('Draw')
        break
