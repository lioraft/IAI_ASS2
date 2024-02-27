import math


def alphabeta_max(current_game):
    return maximin(current_game)

def alphabeta_min(current_game):
    return minimax(current_game)


def maximin(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, alpha, beta)
        if v < mx:
            v = mx
            best_move = move
        # update max alpha
        alpha = max(alpha, v)
        # if beta is less than alpha, prune the rest of the moves
        if beta <= alpha:
            break
    return v, best_move


def minimax(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, alpha, beta)
        if v > mx:
            v = mx
            best_move = move
        # update min beta
        beta = min(beta, v)
        # if beta is less than alpha, prune the rest of the moves
        if beta <= alpha:
            break
    return v, best_move
