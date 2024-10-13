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

def minimax(board): #algoritmo recursivo (árvore)
    '''
    returns the optimal action for the current player on the board.
    '''
    #primeira chamada do método => onde a ação tomada é a relevante
    cPlayer = player(board)
    if cPlayer == X: #player quer maximizar o resultado
        value = -2  #valor menor que todos os valores possíveis [-1, 0, 1]
        bestAction = None
        for a in actions(board):
            newValue = insideMinimax(result(board, a)) #encontra os desdobramentos da ação tomada, buscando a decisão que maximiza o value
            if newValue > value: #verifica se o novo valor é maior que o anterior
                value = newValue #maximiza o valor
                bestAction = a   #armazena a melhor ação correspondente à maximização
        return bestAction # retorna a melhor ação encontrada

    if cPlayer == O: #player quer minimizar o resultado
        value = 2 #valor maior que todos os valores possíveis [-1, 0, 1]\s
        bestAction = None
        for a in actions(board):
            newValue = insideMinimax(result(board, a)) #encontra os desdobramentos da ação tomada, buscando a decisão que minimiza o value
            if newValue < value: #verifica se o novo valor é maior que o anterior
                value = newValue #minimiza o valor
                bestAction = a   #armazena a melhor ação correspondente à minimização
        return bestAction # retorna a melhor ação encontrada
    
def insideMinimax(board): #recursão interna (n sei como tornar esse metodo privado, nem sei se é possivel, mas é o ideal)
    #condição de parada da recursão => quando alcançar o fim do jogo
    if terminal(board):
        return utility(board) #retorna quem foi o vencedor
    
    cPlayer = player(board)
    if cPlayer == X: #player quer maximizar o resultado
        value = -math.inf
        for a in actions(board):
            value = max(value, insideMinimax(result(board, a))) #tenta encontrar a escolha que maximiza o value
        return value # retorna a melhor ação encontrada

    if cPlayer == O: #player quer minimizar o resultado
        value = math.inf
        for a in actions(board):
            value = min(value, insideMinimax(result(board, a))) #tenta encontrar a escolha que minimize o value
        return value # retorna a melhor ação encontrada