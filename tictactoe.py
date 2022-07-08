#tictactoe

def intro():
    print('Welcome to Tic Tac Toe, in order to play there must be 2 players present')
    player1 = input('Enter the name of player 1, who will be using "X": ')
    player2 = input('Enter the name of player 2, who will be using "O": ')
    return [(player1, 'X'), (player2, 'O')]

def player_turns(player_info):
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    winner = [False, '', '']
    printboard(board)
    while winner[0] == False:
        for name, symbol in player_info:
            while True:
                try:
                    choice = int(input(f'{name}, choose the slot you want to select: '))
                    if choice not in range(1, 10) or check_board(choice, board) == False:
                        print('Invalid input, enter a digit from 1-9: ')
                        continue
                    board = update_board(choice, symbol, board)
                    printboard(board)
                    winner = check_win(board, symbol, name)
                    break
                except ValueError:
                    print('Invalid input, enter a digit from 1-9: ')
            if winner[0] == True:
                        break
    if winner[2] == 'Win':
        print(f'congratulations for winning, {winner[1]}')
    elif winner[2] == 'Tie':
        print(f'It was a draw!')
    exit_restart(player_info)

def printboard(board):
    print('\n'*150)
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_board(choice, board):
    if board[choice-1].isdigit() == False:
        return False
    else:
        return True

def update_board(user_input, symbol, board):
    if symbol == 'X':
        board[user_input-1] = symbol
    elif symbol == 'O':
        board[user_input-1] = symbol
    return board

def check_win(board, symbol, name):
    board_word = ''.join(board)
    if symbol == 'O':
        if board_word[:3] == 'OOO' or board_word[3:6] == 'OOO' or board_word[6:] == 'OOO':
            return [True, name, 'Win']
        elif board_word[0] == 'O' and board_word[4] == 'O' and board_word[8] == 'O':
            return [True, name, 'Win']
        elif board_word[2] == 'O' and board_word[4] == 'O' and board_word[6] == 'O':
            return [True, name, 'Win']
        elif board_word[0] == 'O' and board_word[3] == 'O' and board_word[6] == 'O':
            return [True, name, 'Win']
        elif board_word[1] == 'O' and board_word[4] == 'O' and board_word[7] == 'O':
            return [True, name, 'Win']
        elif board_word[2] == 'O' and board_word[5] == 'O' and board_word[8] == 'O':
            return [True, name, 'Win']
    elif symbol == 'X':
        if board_word[:3] == 'XXX' or board_word[3:6] == 'XXX' or board_word[6:] == 'XXX':
            return [True, name, 'Win']
        elif board_word[0] == 'X' and board_word[4] == 'X' and board_word[8] == 'X':
            return [True, name, 'Win']
        elif board_word[2] == 'X' and board_word[4] == 'X' and board_word[6] == 'X':
            return [True, name, 'Win']
        elif board_word[0] == 'X' and board_word[3] == 'X' and board_word[6] == 'X':
            return [True, name, 'Win']
        elif board_word[1] == 'X' and board_word[4] == 'X' and board_word[7] == 'X':
            return [True, name, 'Win']
        elif board_word[2] == 'X' and board_word[5] == 'X' and board_word[8] == 'X':
            return [True, name, 'Win']
    if board_word.isalpha():
        return [True, '', 'Tie']
    else:
        return [False, '', '']

def exit_restart(info):
    while True:
        choice = input('Would you like to keep playing? Y or N: ')
        if choice == 'Y':
            player_turns(info)
        elif choice == 'N':
            print('Game Over')
            exit()
        else:
            print('Invalid input')

def main():
    players = intro()
    player_turns(players)

main()