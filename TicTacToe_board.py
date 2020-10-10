# Display the board
# Take user input for each player's move
# Display the updated board

from random import randint

print("Importing bot...", end="")
try:
    from TicTacToe_bot import bot_move
    print(" | SUCCESS")
    bot_imported = True
except ModuleNotFoundError:
    print(" | FAILURE\nModuleNotFoundError")
    bot_imported = False


"""
 \/ | \/ | \/
 /\ | /\ | /\
____|____|____
 \/ | \/ | \/
 /\ | /\ | /\
____|____|____
 \/ | \/ | \/
 /\ | /\ | /\

 /\ | /\ | /\
 \/ | \/ | \/
____|____|____
 /\ | /\ | /\
 \/ | \/ | \/
____|____|____
 /\ | /\ | /\
 \/ | \/ | \/
"""

board_d = [
    [' 1  ', '|', ' 2  ', '|', ' 3  '],  # 0]
    ['    ', '|', '    ', '|', '    '],  # 1]
    ['____', '|', '____', '|', '____'],  # 2
    [' 4  ', '|', ' 5  ', '|', ' 6  '],  # 3]
    ['    ', '|', '    ', '|', '    '],  # 4]
    ['____', '|', '____', '|', '____'],  # 5
    [' 7  ', '|', ' 8  ', '|', ' 9  '],  # 6]
    ['    ', '|', '    ', '|', '    ']   # 7]
]

player = True
available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
difficulty = ''


def print_board():
    global board_d
    for i in board_d:
        for x in i:
            print(x, end='')
        print()


def get_input():
    print_board()
    print('Enter your move as the number of the open box you would like')
    try:
        move = int(input('>> '))
    except ValueError:
        return get_input()
    for i in available:
        if move == i:
            return move
        else:
            pass
    return get_input()


def do_move(move):
    global board_d
    global player
    global available

    if player:
        symbol = ' \/  /\ '
    else:
        symbol = ' /\  \/ '

    # 3, 6, 9 == 3rd Column
    if move % 3 == 0:
        board_d[move - 3][4] = symbol[0:4]
        board_d[move - 2][4] = symbol[4:8]
    # 2, 5, 8 == 2nd Column
    elif move % 3 == 2:
        board_d[move - 2][2] = symbol[0:4]
        board_d[move - 1][2] = symbol[4:8]
    # 1, 4, 7 == 3rd Column
    elif move % 3 == 1:
        board_d[move - 1][0] = symbol[0:4]
        board_d[move][0] = symbol[4:8]

    available.remove(move)


def game_condition():
    global board_d
    # Second character being \ means x, / means o
    if board_d[3][2][1] != '5':  # Middle
        if board_d[0][2][1] == board_d[3][2][1] == board_d[6][2][1]:
            win(board_d[0][2] + board_d[1][2])
            return False
        elif board_d[0][0][1] == board_d[3][2][1] == board_d[6][4][1]:
            win(board_d[0][0] + board_d[1][0])
            return False
        elif board_d[0][4][1] == board_d[3][2][1] == board_d[6][0][1]:
            win(board_d[0][4] + board_d[1][4])
            return False
        elif board_d[3][0][1] == board_d[3][2][1] == board_d[3][4][1]:
            win(board_d[3][0] + board_d[4][0])
            return False

    if board_d[0][0][1] != '1':  # Top Left
        if board_d[3][0][1] == board_d[0][0][1] == board_d[6][0][1]:
            win(board_d[0][0] + board_d[1][0])
            return False
        elif board_d[0][2][1] == board_d[0][0][1] == board_d[0][4][1]:
            win(board_d[0][0] + board_d[1][0])
            return False

    if board_d[6][4][1] != '9':  # Bottom Right
        if board_d[6][2][1] == board_d[6][4][1] == board_d[6][0][1]:
            win(board_d[6][0] + board_d[7][0])
            return False
        elif board_d[3][4][1] == board_d[6][4][1] == board_d[0][4][1]:
            win(board_d[0][4] + board_d[1][4])
            return False

    if len(available) == 0:
        print_board()
        print('\nTie!')
        input()
        return False

    else:
        return True


def win(symbol):
    print_board()
    print()
    input(symbol[0:4] + '    \  /\  / | |\ | |\n' + symbol[4:8] +
                        '     \/  \/  | | \| .')


def title_screen():
    global board_d
    global available
    global player
    global difficulty

    print("\n\n")
    print(" \/ | \/ | \/      /\ | /\ | /\ \n" +
          " /\ | /\ | /\      \/ | \/ | \/ \n" +
          "____|____|____    ____|____|____\n" +
          " \/ | \/ | \/      /\ | /\ | /\ \n" +
          " /\ | /\ | /\      \/ | \/ | \/ \n" +
          "____|____|____    ____|____|____\n" +
          " \/ | \/ | \/      /\ | /\ | /\ \n" +
          " /\ | /\ | /\      \/ | \/ | \/ \n")
    print("          Tic-Tac-Toe!\n\n")

    mode = input("Type 1 for one player mode, 2 for two player mode, and exit to close the program.\n>> ")
    board_d = [
        [' 1  ', '|', ' 2  ', '|', ' 3  '],  # 0]
        ['    ', '|', '    ', '|', '    '],  # 1]
        ['____', '|', '____', '|', '____'],  # 2
        [' 4  ', '|', ' 5  ', '|', ' 6  '],  # 3]
        ['    ', '|', '    ', '|', '    '],  # 4]
        ['____', '|', '____', '|', '____'],  # 5
        [' 7  ', '|', ' 8  ', '|', ' 9  '],  # 6]
        ['    ', '|', '    ', '|', '    ']  # 7]
    ]
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = True

    if mode == '1':
        if bot_imported:
            difficulty = input("Would you like to play on easy or hard mode? Type 'e' for easy and 'h' for hard.\n>> ")
            if difficulty != 'e' and difficulty != 'h':
                input("Please only enter 'e' or 'h'. Press enter to continue...")
                title_screen()
            else:
                play_computer()
        else:
            print("Sorry, the bot program did not import correctly and so one-player mode is nonfunctional.")
            title_screen()
    elif mode == '2':
        play()
    elif mode == 'exit':
        exit()
    else:
        input("Please only enter 1, 2, or exit. Press enter to return to the title screen.")
        title_screen()


def play():
    global player

    while game_condition():
        do_move(get_input())

        player = not player

    title_screen()


def play_computer():
    global player
    global difficulty
    global board_d
    global available

    if difficulty == 'e':

        while game_condition():
            do_move(get_input())

            player = not player

            if game_condition():
                do_move(available[randint(0, len(available) - 1)])
                player = not player
            else:
                break

        title_screen()

    if difficulty == 'h':

        while game_condition():
            do_move(get_input())

            player = not player

            if game_condition():
                """
                DEBUGGING
                print(bot_move([board_d[0][0][1], board_d[0][2][1], board_d[0][4][1],
                                board_d[3][0][1], board_d[3][2][1], board_d[3][4][1],
                                board_d[6][0][1], board_d[6][2][1], board_d[6][4][1],
                                ]))
                """

                do_move(bot_move([board_d[0][0][1], board_d[0][2][1], board_d[0][4][1],
                                  board_d[3][0][1], board_d[3][2][1], board_d[3][4][1],
                                  board_d[6][0][1], board_d[6][2][1], board_d[6][4][1],
                                  ]))

                player = not player

            else:
                break

        title_screen()


title_screen()
