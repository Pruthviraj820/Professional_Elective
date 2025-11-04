import copy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]



def player(board):
    """
    Returns the player ('X' or 'O') who has the next turn on the board.
    """
    x_moves = sum(row.count(X) for row in board)
    o_moves = sum(row.count(O) for row in board)

    
    if x_moves == o_moves:
        return X
    else:
        return O



def actions(board):
    
    
    possible_moves = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_moves.add((row, col))

    return possible_moves



# 4. Apply a move to the board
def result(board, action):
    """
    Returns the new board that results from making the move (row, col).
    Raises an error if the move is invalid.
    """
    row, col = action

  
    if board[row][col] is not EMPTY:
        raise Exception("Invalid move! Cell already filled.")

    new_board = copy.deepcopy(board)
    new_board[row][col] = player(board)  # Place 'X' or 'O'

    return new_board


# 5. Check if someone has won
def winner(board):
    """
    Returns 'X' or 'O' if a player has won, otherwise None.
    """
 
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]

   
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]


    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None  


# 6. Check if the game is over
def terminal(board):
    """
    Returns True if the game is over (win or draw), otherwise False.
    """
   
    if winner(board) is not None:
        return True


    for row in board:
        if EMPTY in row:
            return False

    return True



# 7. Score the final result
def utility(board):
   

    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


# 8. AI Decision Maker (Minimax)
def minimax(board):
   

    # If game already over, no moves left
    if terminal(board):
        return None

    current_player = player(board)


    def max_value(state):
        if terminal(state):
            return utility(state), None

        best_score = float("-inf")
        best_move = None

        for move in actions(state):
            score, _ = min_value(result(state, move))
            if score > best_score:
                best_score = score
                best_move = move

            # X can't do better than a guaranteed win
            if best_score == 1:
                break

        return best_score, best_move

  
    def min_value(state):
        if terminal(state):
            return utility(state), None

        best_score = float("inf")
        best_move = None

        for move in actions(state):
            score, _ = max_value(result(state, move))
            if score < best_score:
                best_score = score
                best_move = move

            # O can't do better than a guaranteed win
            if best_score == -1:
                break

        return best_score, best_move

    if current_player == X:
        _, chosen_move = max_value(board)
    else:
        _, chosen_move = min_value(board)

    return chosen_move
