# Hugo Gomes Soares
# Julia Enriquetto de Brito
import math

X = 'X'
O = 'O'
EMPTY = None

def initial_state():
    '''
    returns starting state of the board.
    '''
    return [[EMPTY for i in range(3)] for j in range(3)] # fills rows and columns with EMPTY


def player(board):
    '''
    returns player who has the next turn on a board.
    '''
    # initialize counters
    X_moves, O_moves = (0,0)

    for i in range(3): # loop over rows
        for j in range(3): # loop over columns 
            if board[i][j] == X:
                X_moves += 1
            elif board[i][j] == O:
                O_moves += 1

    # next player based on the counts
    if X_moves == O_moves:
        return X # equal moves, X turn 
    else:
        return O # if x has more moves, O turn 

def actions(board):
    '''
    returns set of all possible actions (i, j) available on the board.
    '''
    possible_actions = [] # list of all possible actions the player could choose 
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: # possible actions = empty spaces in the board
                possible_actions.append((i,j)) # join all the actions in a list of tuples
    return possible_actions

def result(board, action):
    '''
    returns the board that results from making move (i, j) on the board.
    '''
    i, j = action
    
    # copy of the original board
    copy = []
    for i_index in range(3):
        new_i = []
        for j_index in range(3):
            new_i.append(board[i_index][j_index])
        copy.append(new_i)

    # current player and his moves
    current_player = player(board)

    # copy player action
    copy[i][j] = current_player

    return copy

def winner(board):
    '''
    returns the winner of the game, if there is one.
    '''
    win = utility(board)
    if win == 1: # if win is = 1, X won
        return X
    elif win == -1: # if win is = -1, O won 
        return O
    else:
        return None # otherwise, is a tie

def terminal(board):
    '''
    returns True if game is over, False otherwise.
    ''' 
    # if there is a winner, game has ended 
    if winner(board) is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: # if there is some empty cell, the game is not over yet
                return False
                
    # no empty cells and no winner, must be a tie 
    return True

def utility(board):
    '''
    returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    '''
    # rows
    for i in range(3):
        count = 1
        aux = board[i][0]
        for j in range(1,3):
            if board[i][j] == aux:
                count += 1
            else:
                break
        if count == 3:
            if aux == X:
                return 1
            elif aux == O:
                return -1

    # columns 
    for j in range(3):
        count = 1
        aux = board[0][j]
        for i in range(1,3):
            if board[i][j] == aux:
                count += 1
            else:
                break
        if count == 3:
            if aux == X:
                return 1
            elif aux == O:
                return -1

    # diagonal
    mid = board[1][1]
    if (board[0][0] == mid and board[2][2] == mid) or (board[2][0] == mid and board[0][2] == mid):
        if mid == X:
            return 1
        elif mid == O:
            return -1

    return 0

def minimax(board): # recursive decision tree algorithm 
    '''
    returns the optimal action for the current player on the board.
    '''
    # first call of the method => where the action taken is the relevant one
    cPlayer = player(board)
    if cPlayer == X: # player wants to maximize the result
        value = -2  # value smaller than all possible values [-1, 0, 1]
        bestAction = None
        for a in actions(board):
            newValue = insideMinimax(result(board, a)) # finds the outcomes of the action taken, seeking the decision that maximizes the value
            if newValue > value: # checks if the new value is greater than the previous one
                value = newValue # maximizes the value
                bestAction = a   # stores the best action corresponding to the maximization
        return bestAction # returns the best action found
    
    if cPlayer == O: # player wants to minimize the result
        value = 2 # value greater than all possible values [-1, 0, 1]
        bestAction = None
        for a in actions(board):
            newValue = insideMinimax(result(board, a)) # finds the outcomes of the action taken, seeking the decision that minimizes the value
            if newValue < value: # checks if the new value is greater than the previous one
                value = newValue # minimizes the value
                bestAction = a   # stores the best action corresponding to the minimization
        return bestAction # returns the best action found
    
def insideMinimax(board): # internal recursion (I’m unsure how to make this method private in Python, or if it's even possible, but I believe that would be ideal. *How can I do this, Guilherme?)

    # stop condition of the recursion => when reaching the end of the game
    if terminal(board):
        return utility(board) # returns the winner
    
    cPlayer = player(board)
    if cPlayer == X: # player wants to maximize the result
        value = -math.inf
        for a in actions(board):
            value = max(value, insideMinimax(result(board, a))) # tries to find the choice that maximizes the value
        return value # returns the best action found

    if cPlayer == O: # player wants to minimize the result
        value = math.inf
        for a in actions(board):
            value = min(value, insideMinimax(result(board, a))) # tries to find the choice that minimizes the value
        return value # returns the best action found