
def base_heuristic(curr_state):
    # if the current player is 1, get number of possible moves for player 1
    if curr_state.get_curr_player() == 1:
        player_one = len(curr_state.potential_moves())
        # switch to player 2
        curr_state.set_curr_player(2)
        player_two = len(curr_state.potential_moves())
        # switch back to player 1
        curr_state.set_curr_player(1)
    else:
        # if the current player is 2, get number of possible moves for player 2
        player_two = len(curr_state.potential_moves())
        # switch to player 1
        curr_state.set_curr_player(1)
        player_one = len(curr_state.potential_moves())
        # switch back to player 2
        curr_state.set_curr_player(2)
    # return the difference between the number of possible moves for player 1 and player 2
    return player_one - player_two

# advanced heuristic: the difference between the number of possible moves for the current player and the distance between the two players
def advanced_heuristic(curr_state):
    # get locations of players
    locs = curr_state.get_player_locations()
    player_one = locs[1]
    player_two = locs[2]
    # get the distance between the two players
    distance = abs(player_one[0] - player_two[0]) + abs(player_one[1] - player_two[1])
    # return available moves for current player minus the distance between the two players
    return abs(len(curr_state.potential_moves()) - distance)



# control of the center heuristic: the difference between the number of central squares controlled by each player
def control_of_center(state):
    # central squares of the board
    central_squares = [(2, 3), (2, 4), (3, 3), (3, 4), (4, 3), (4, 4)]
    # get grid of the current state
    grid = state.get_grid()
    # number of central squares controlled by each player
    player_one_control = sum(1 for square in central_squares if grid[square[0], square[1]] == 1)
    player_two_control = sum(1 for square in central_squares if grid[square[0], square[1]] == 2)
    # return the difference in control of central squares
    return abs(player_one_control - player_two_control)

# potential isolation heuristic: the difference between the number of possible moves for the current player and the distance between the two players
def potential_isolation(state):
    # get locations of players
    locs = state.get_player_locations()
    player_one = locs[1]
    player_two = locs[2]
    # calculate manhattan distance between the two players
    distance = abs(player_one[0] - player_two[0]) + abs(player_one[1] - player_two[1])
    # if current player is 1, get number of possible moves for player 2
    if state.get_curr_player() == 1:
        state.set_curr_player(2)
        opponent_empty_adjacent = len(state.potential_moves())
        state.set_curr_player(1)
    else:
        # if current player is 2, get number of possible moves for player 1
        state.set_curr_player(1)
        opponent_empty_adjacent = len(state.potential_moves())
        state.set_curr_player(2)
    # return the potential for isolating the opponent's pawn
    return abs(opponent_empty_adjacent - distance)

# combined heuristic: the sum of control of the center and potential isolation heuristics
def combined_heuristic(state):
    # control of the center
    center_control = control_of_center(state)
    # potential isolation
    isolation_potential = potential_isolation(state)
    # return combined heuristic
    return center_control + isolation_potential

