import math

X = 'X'
O = 'O'
EMPTY = None
vezDe = 'O'

def initial_state():
    '''
    returns starting state of the board.
    '''
    return [[EMPTY for i in range(3)] for j in range(3)] #preenche com EMPTY as linhas e colunas


def playear(board):
    '''
    returns player who has the next turn on a board.
    '''
    if vezDe == X: #se a vez atual for de X então o próximo será O
        return O
    else:  #se a vez atual for de O então o próximo será X
        return X


def actions(board):
    '''
    returns set of all possible actions (i, j) available on the board.
    '''
    possible_actions = [] # list of all possible actions the player can take 
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: # possible actions = empty spaces in the board
                possible_actions.append((i,j)) # join all the actions in a list of tuples
    return possible_actions


def result(board, action):
    '''
    returns the board that results from making move (i, j) on the board.
    '''
    i, j = actions
    if vezDe == X:
        vezDe = O #altera a vez devido ação realizada
        board[i][j] = X #atualiza a mudança do tabuleiro
        return board
    else:
        vezDe = X #altera a vez devido ação realizada
        board[i][j] = O #atualiza a mudança do tabuleiro
        return board


def winner(board):
    '''
    returns the winner of the game, if there is one.
    '''
    winner = utility(board)
    if winner != 0:
        if winner == 1:
            return X
        elif winner == -1:
            return O
    else:
        return None


def terminal(board):
    '''
    returns True if game is over, False otherwise.
    '''
    hasWinner = winner(board)
    if hasWinner is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True



def utility(board):
    '''
    returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    '''
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
            else:
                return -1

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
            else:
                return -1

    mid = board[1][1]
    if board[0][0] == mid and board[2][2] == mid:
        if mid == X:
            return 1
        else:
            return -1

    if board[2][0] == mid and board[0][2] == mid:
        if mid == X:
            return 1
        else:
            return -1

    return 0

def minimax(board):
    '''
    returns the optimal action for the current player on the board.
    '''
    raise NotImplementedError