
Talha_move = 'X'
PLAYER_O = 'O'
EMPTY = ' '


board = [[EMPTY for _ in range(3)] for _ in range(3)]
current_player = Talha_move

def print_board():
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def is_winner(player):
    # Check rows, columns, and diagonals for a win
    return any(all(cell == player for cell in line) for line in board) or \
           any(all(row[i] == player for row in board) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_full():
    return all(cell != EMPTY for row in board for cell in row)

def evaluate():
    if is_winner(Talha_move):
        return -10
    elif is_winner(PLAYER_O):
        return 10
    elif is_full():
        return 0

def minimax(depth, is_maximizing):
    if is_winner(Talha_move) or is_winner(PLAYER_O) or is_full():
        return evaluate()

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = Talha_move
                    eval = minimax(depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move():
    best_move = None
    best_eval = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                eval = minimax(0, False)
                board[i][j] = EMPTY

                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

def on_button_click(row, col):
    global current_player
    if board[row][col] == EMPTY and current_player == Talha_move:
        buttons[row][col].config(text=Talha_move, state='disabled')
        board[row][col] = Talha_move

        if is_winner(Talha_move):
            print_board()
            messagebox.showinfo("Game Over", "Player X wins!")
            root.quit()
        elif is_full():
            print_board()
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = PLAYER_O
            ai_move()

def ai_move():
    global current_player
    row, col = find_best_move()
    buttons[row][col].config(text=PLAYER_O, state='disabled')
    board[row][col] = PLAYER_O

    if is_winner(PLAYER_O):
        print_board()
        messagebox.showinfo("Game Over", "Player O (AI) wins!")
        root.quit()
    elif is_full():
        print_board()
        messagebox.showinfo("Game Over", "It's a draw!")
        root.quit()
    else:
        current_player = Talha_move

def play_game():
    global root, buttons, board, current_player

    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    buttons = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=EMPTY, font=('Arial', 24), width=5, height=2, command=lambda i=i, j=j: on_button_click(i, j))
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    play_game()
