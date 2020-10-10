# TicTacToe_bot.py
# This bot should play Tic-Tac-Toe and never lose
# The bot should take input in the form of only the 2nd character of the top line of each box (where the numbers are)
# The bot should be set to always be o
# The bot should output the same as the user inputs so that the move function can be used in the same way
# (Enter the number of the box you would like to move into)


def bot_move(board):
    bot_symbol = '/'  # This is just the first symbol of the o, but it is what the bot will use to recognize its marks
    player_symbol = '\\'  # Opposite of the bot_symbol (need \\ instead of \ for the string to close
    
    # Check if the bot can win
    if board[1] == bot_symbol and board[2] == bot_symbol or board[4] == bot_symbol and board[8] == bot_symbol or \
            board[3] == bot_symbol and board[6] == bot_symbol:
        if board[0] == '1':
            return 1
    if board[4] == bot_symbol and board[7] == bot_symbol or board[0] == bot_symbol and board[2] == bot_symbol:
        if board[1] == '2':
            return 2
    if board[0] == bot_symbol and board[1] == bot_symbol or board[6] == bot_symbol and board[4] == bot_symbol or \
            board[5] == bot_symbol and board[8] == bot_symbol:
        if board[2] == '3':
            # DEBUG
            print('Checkpoint 1')
            #
            return 3
    if board[0] == bot_symbol and board[6] == bot_symbol or board[4] == bot_symbol and board[5] == bot_symbol:
        if board[3] == '4':
            return 4
    if board[0] == bot_symbol and board[8] == bot_symbol or board[2] == bot_symbol and board[6] == bot_symbol or \
            board[1] == bot_symbol and board[7] == bot_symbol or board[3] == bot_symbol and board[5] == bot_symbol:
        if board[4] == '5':
            return 5
    if board[3] == bot_symbol and board[4] == bot_symbol or board[2] == bot_symbol and board[8] == bot_symbol:
        if board[5] == '6':
            return 6
    if board[0] == bot_symbol and board[3] == bot_symbol or board[4] == bot_symbol and board[2] == bot_symbol or \
            board[7] == bot_symbol and board[8] == bot_symbol:
        if board[6] == '7':
            return 7
    if board[1] == bot_symbol and board[4] == bot_symbol or board[6] == bot_symbol and board[8] == bot_symbol:
        if board[7] == '8':
            return 8
    if board[0] == bot_symbol and board[4] == bot_symbol or board[2] == bot_symbol and board[5] == bot_symbol or \
            board[6] == bot_symbol and board[7] == bot_symbol:
        if board[8] == '9':
            return 9

    # Check if the opponent could win next turn
    if board[1] == player_symbol and board[2] == player_symbol or board[4] == player_symbol and \
            board[8] == player_symbol or \
            board[3] == player_symbol and board[6] == player_symbol:
        if board[0] == '1':
            return 1
    if board[4] == player_symbol and board[7] == player_symbol or board[0] == player_symbol and \
            board[2] == player_symbol:
        if board[1] == '2':
            return 2
    if board[0] == player_symbol and board[1] == player_symbol or board[6] == player_symbol and \
            board[4] == player_symbol or \
            board[5] == player_symbol and board[8] == player_symbol:
        if board[2] == '3':
            # DEBUG
            print('Checkpoint 2')
            #
            return 3
    if board[0] == player_symbol and board[6] == player_symbol or board[4] == player_symbol and \
            board[5] == player_symbol:
        if board[3] == '4':
            return 4
    if board[0] == player_symbol and board[8] == player_symbol or board[2] == player_symbol and \
            board[6] == player_symbol or \
            board[1] == player_symbol and board[7] == player_symbol or board[3] == player_symbol and \
            board[5] == player_symbol:
        if board[4] == '5':
            return 5
    if board[3] == player_symbol and board[4] == player_symbol or board[2] == player_symbol and \
            board[8] == player_symbol:
        if board[5] == '6':
            return 6
    if board[0] == player_symbol and board[3] == player_symbol or board[4] == player_symbol and \
            board[2] == player_symbol or \
            board[7] == player_symbol and board[8] == player_symbol:
        if board[6] == '7':
            return 7
    if board[1] == player_symbol and board[4] == player_symbol or board[6] == player_symbol and \
            board[8] == player_symbol:
        if board[7] == '8':
            return 8
    if board[0] == player_symbol and board[4] == player_symbol or board[2] == player_symbol and \
            board[5] == player_symbol or \
            board[6] == player_symbol and board[7] == player_symbol:
        if board[8] == '9':
            return 9

    # Check if the center is taken
    if board[4] == '5':
        return 5

    # Check if the corners are taken
    if board[0] == '1':
        if board[8] == '9':
            if board[6] == '7':
                return 7
            elif board[2] == '3':
                # DEBUG
                print('Checkpoint 3')
                #
                return 3
            else:
                return 1
        else:
            return 1

    elif board[2] == '3':
        if board[6] == '7':
            if board[0] == '1':
                return 1
            elif board[8] == '9':
                return 9
            else:
                # DEBUG
                print('Checkpoint 4')
                #
                return 3
        else:
            # DEBUG
            print('Checkpoint 5')
            #
            return 3

    elif board[6] == '7':
        return 7

    elif board[8] == '9':
        return 9

    # Take a side
    if board[1] == '2' and board[7] == '8':
        return 2
    elif board[3] == '4' and board[5] == '6':
        return 4
