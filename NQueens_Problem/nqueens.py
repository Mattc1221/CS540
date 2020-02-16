"""
Author: Matthew Chiang
Class: Computer Science 540: Introduction to Artificial Intelligence
Description: Uses the hill climb algorithm to take an n sized chess board and finds a way to position n queens on the
            board such that no queen can attack another queen. Additionally, a boulder is placed on the board at
            position (boulderX, boulderY) which blocks the path of queens across (boulderX, boulderY).

            To run the program use function nqueens_restart(Number_of_queens, Number_of_restarts, BoulderX, BoulderY)
            Program Output: a list of n (number of queens) where the index denotes the column of the queen and the value
                            of index n in the list is the row of the queen.
"""

import random
import copy


def print_moves(moves):
    """prints moves in a formatted style"""
    for x in moves:
        print str(x[0]) + " - f=" + str(x[1])


def succ(state, boulderX, boulderY):
    """ finds all successor states from state """
    # will store the successor states
    succs = []

    # iterates through all possible positions of each queen
    for pos in range(0, len(state)):
        for i in range(0, len(state)):
            # stores a copy of the current state
            succ = copy.deepcopy(state)

            # filters out non-valid states and the current state
            if not (i == state[pos] or (i == boulderY and pos == boulderX)):
                succ[pos] = i
                succs.append(succ)
    return succs


def f(state, boulderX, boulderY):
    """ calculates the f value of state """
    hits = []  # stores all columns that have a queen that can be attacked
    # check rows
    for col in range(len(state)):
        # iterates through subsequent columns
        for next_queen in range(col + 1, len(state)):
            cq, tq = state[col], state[next_queen]  # cq = queen in column col, tq = queen in subsequent columns
            # handles boulder
            if next_queen == boulderX and cq == boulderY:
                break
            # checks if two queens in column col and next_queen can attack each other from rows
            if cq == tq:
                if col not in hits:
                    hits.append(col)
                if next_queen not in hits:
                    hits.append(next_queen)
                break

    # check diagonal
    for col in range(len(state)):
        # iterates through subsequent columns
        for next_queen in range(col + 1, len(state)):
            cq, tq = state[col], state[next_queen]  # cq = queen in column col, tq = queen in subsequent columns
            # handles boulder
            if next_queen == boulderX and (cq + next_queen - col == boulderY):
                break
            # checks if two queens in column col and next_queen can attack each other from diagonals
            if col + cq == next_queen + tq or col - cq == next_queen - tq:
                if col not in hits:
                    hits.append(col)
                if next_queen not in hits:
                    hits.append(next_queen)
    # length of hits = the f value of the state
    return len(hits)


def choose_next(curr, boulderX, boulderY):
    """ chooses the next state of curr based on the f value """
    succs = succ(curr, boulderX, boulderY)
    succs.append(curr)
    succs = sorted(succs)
    unique_succ = None  # stores the state with the lowest f value
    unique_succ_val = len(curr) + 1  # f value of unique_succ
    tie = False  # tells if there is a tie in f value
    for suc in succs:
        suc_f = f(suc, boulderX, boulderY)
        # checks if tie occurs
        if suc_f == unique_succ_val:
            tie = True
        # checks for new unique_succ
        elif suc_f < unique_succ_val:
            unique_succ_val = suc_f
            unique_succ = suc
            tie = False

    # if no tie, returns the state with lowest f value
    if not tie:
        if unique_succ == curr:
            return None
        return unique_succ

    # handles tie case
    length = len(succs)
    x = 0
    for i in range(length):
        if (x >= length):
            break
        # removes any state with f value greater than unique_succ_val
        if f(succs[x], boulderX, boulderY) > unique_succ_val:
            succs.remove(succs[x])
            x = x - 1
            length = length - 1
        x = x + 1

    # if selected next is the given state, returns none
    if succs[0] == curr:
        return None
    return succs[0]


def nqueens(initial_state, boulderX, boulderY):
    """ finds a local or global minima of initial_state and successor states, based on f value """
    curr_min_f = len(initial_state) + 1
    state = initial_state
    copy_state = state
    moves = []
    # finds minima
    while curr_min_f != 0 and state is not None:
        f_val = f(state, boulderX, boulderY)
        curr_min_f = f_val
        moves.append([state, f_val])
        state = choose_next(state, boulderX, boulderY)

    # prints out order of states from initial to final state
    print_moves(moves)

    # gets the local minima from our list of states
    best = moves[(len(moves) - 1)]
    return best[0]


def get_valid_state(n, bx, by):
    """ randomly generates a valid state, based on the boulder position (bx, by)"""
    state = []
    valid = False
    while not valid:
        for j in range(n):
            rand = random.randint(0, n)
            state.append(rand)
        if state[bx] == by:
            valid = True
        else:
            state = []
    return state


def nqueens_restart(n, k, boulderX, boulderY):
    """ performs same function as nqueens(), but restarts with a random state if a local minimun is reached. Restarts
    up to k times """
    min_f = n + 1
    solutions = []  # list of solutions determined by nqueens
    for i in range(k):
        state = get_valid_state(n, boulderX, boulderY)
        best = nqueens(state, boulderX, boulderY)
        f_val = f(best, boulderX, boulderY)
        if f_val == 0:
            # final solution is a global minima
            return best
        if f_val == min_f:
            solutions.append(best)
        if f_val < min_f:
            min_f = f_val
            solutions = [best]
    # f=0 is not found in k iterations, so sorted list of solutions with equal minimum f value reached
    return sorted(solutions)
