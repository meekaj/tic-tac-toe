import os
import random

# Initialize the game board
board = [' ' for _ in range(10)]

def print_board():
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def is_board_full():
    return board.count(' ') < 2

def is_winner(l):
    wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)]
    return any(board[a] == board[b] == board[c] == l for a, b, c in wins)

def insert_letter(letter, pos):
    if board[pos] == ' ':
        board[pos] = letter
        return True
    return False

def player_move():
    while True:
        try:
            pos = int(input("Please select a position to place X (1-9): "))
            if 1 <= pos <= 9 and insert_letter('X', pos):
                break
            print('Invalid move. Try again.')
        except ValueError:
            print('Please enter a number.')

def computer_move():
    possible_moves = [i for i, x in enumerate(board) if x == ' ' and i != 0]
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(let):
                return i

    if 5 in possible_moves:
        return 5

    corners = [i for i in possible_moves if i in [1, 3, 7, 9]]
    if corners:
        return random.choice(corners)

    edges = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges:
        return random.choice(edges)

    return 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def game_play():
    global board
    board = [' ' for _ in range(10)]
    clear_screen()
    while not is_board_full():
        if not is_winner('O'):
            player_move()
            clear_screen()
            print_board()
        else:
            print("You lose! :(")
            return

        if not is_winner('X'):
            move = computer_move()
            if move:
                insert_letter('O', move)
                clear_screen()
                print_board()
        else:
            print("You win! :)")
            return

        if is_board_full() and not (is_winner('X') or is_winner('O')):
            print("It's a tie!")
            return

def main():
    while True:
        game_play()
        if input("Play again? (y/n): ").lower() not in ['y', 'yes']:
            print("Good luck, have fun!")
            break

if __name__ == "__main__":
    main()
