import string
import os
'''
This is vietnamese version of tictactoe
'''

rule = '''
In this version of tictactoe, the play field is much bigger than the oringinal
game. The size is 21x21 instead of 3x3. The valid coordinate is xy for x
from 1 to 21 and y from a to u. For example, the coordinate for the centre Spot
is '11k'.
    To win in this version, a player has to create an uninteruptted line
(horizontal, vertical or diagonal) consist of 5 symbols (X or O) belong to him
Enter players' names:
(Player 1 will use X and player 2 will use O)
'''


class Player1:
    def __init__(self, name):
        self.name = name
        self.symbol = 'X'


class Player2:
    def __init__(self, name):
        self.name = name
        self.symbol = 'O'


def move(player, board):
    while True:
        draw_board(board)
        move = input('%s turn:' % (player.name))
        move = move.lower()
        if move in board and board[move] == '_':
            print('%s occupied %s' % (player.name, move))
            board[move] = player.symbol
            os.system('clear')
            os.system('cls')

            break
        elif move not in board:
            print('Invalid move! Try again.')
            continue
        elif board[move] != '_':
            print('Spot occupied! Choose another spot')


def playfield():
    row = [y for y in range(1, 22)]
    column = [x for x in string.ascii_lowercase[:21]]
    game_tracker = {}
    for x in column:
        for y in row:
            game_tracker['%d%s' % (y, x)] = '_'
    return game_tracker


def main():
    print(rule)
    board = playfield()
    players = players_init()
    p1 = players[0]
    p2 = players[1]
    turn = 0
    while True:
        move(p1, board)
        move(p2, board)
        if check_win(board) == 'X':
            print('%s win!' % (p1.name))
            break
        elif check_win(board) == 'O':
            print('%s win!' % (p2.name))
            break
        else:
            # print('no one win yet! keep going')
            continue


def check_win(board):
    for y in range(1, 22-4):
        for x in range(97, 118-4):
            # coordinate = str(y)+chr(x)
            if board[str(y)+chr(x)] != '_':
                # Row winning
                if board[str(y)+chr(x)] == board[str(y+1)+chr(x)] == board[str(y+2)+chr(x)]\
                        == board[str(y+3)+chr(x)] == board[str(y+4)+chr(x)]:
                    if board[str(y)+chr(x)] == 'X':
                        return 'X'
                    elif board[str(y)+chr(x)] == 'O':
                        return 'O'
                # Column winning
                if board[str(y)+chr(x)] == board[str(y)+chr(x+1)] == board[str(y)+chr(x+2)]\
                        == board[str(y)+chr(x+3)] == board[str(y)+chr(x+4)]:
                    if board[str(y)+chr(x)] == 'X':
                        return 'X'
                    elif board[str(y)+chr(x)] == 'O':
                        return 'O'
                # Diagonal winning
                if board[str(y)+chr(x)] == board[str(y+1)+chr(x+1)] == board[str(y+2)+chr(x+2)]\
                        == board[str(y+3)+chr(x+3)] == board[str(y+4)+chr(x+4)]:
                    if board[str(y)+chr(x)] == 'X':
                        return 'X'
                    elif board[str(y)+chr(x)] == 'O':
                        return 'O'


def players_init():
    p1 = input('Player 1 name: ')
    p1 = Player1(p1.title())
    p2 = input('Player 2 name: ')
    p2 = Player2(p2.title())
    print('%s vs %s' % (p1.name, p2.name))
    return p1, p2


def draw_board(board):
    index = 0
    label = 97
    for num in range(1, 22):
        if num < 10:
            num = ' '+str(num)
            print(num, end='| ')
        else:
            print(num, end='| ')
    print()
    for item in board.values():
        print(item, end=' | ')
        index += 1
        if index % 21 == 0:
            print(chr(label)+'\n')
            label += 1


if __name__ == '__main__':
    main()
