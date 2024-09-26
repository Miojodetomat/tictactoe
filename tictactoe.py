import math

X = 'X'
O = 'O'
EMPTY = None


def initial_state():
    '''
    returns starting state of the board.
    '''
    raise NotImplementedError


def playear(board):
    '''
    returns player who has the next turn on a board.
    '''
    raise NotImplementedError


def actions(board):
    '''
    returns set of all possible actions (i, j) available on the board.
    '''
    raise NotImplementedError


def result(board, action):
    '''
    returns the board that results from making move (i, j) on the board.
    '''
    raise NotImplementedError


def winner(board):
    '''
    returns the winner of the game, if there is one.
    '''
    raise NotImplementedError


def terminal(board):
    '''
    returns True if game is over, False otherwise.
    '''
    raise NotImplementedError


def utility(board):
    '''
    returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    '''
    raise NotImplementedError


def minimax(board):
    '''
    returns the optimal action for the current player on the board.
    '''
    raise NotImplementedError