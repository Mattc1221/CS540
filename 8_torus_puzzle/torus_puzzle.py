""" author: Matthew Chiang
    source: Computer Science 540
"""
import copy
import priority_queue


def print_succ(state):
    states = generate_succ(state)
    states = sorted(states)
    for i in states:
        print str(i) + " h = " + str(calculate_heuristic(i))
        # print_state(i)


def swap(index1, index2, state):
    """ swaps the values of the elements at index1 and index2 in state and returns it as a new state variable """
    new_state = copy.deepcopy(state)
    new_state[index1] = state[index2]
    new_state[index2] = state[index1]
    return new_state


def calculate_heuristic(state):
    """ calculates the heuristic for the state given, h(s) = # of displaced tiles """
    h = 0
    for i in range(len(state) - 1):
        if i != state[i] - 1:
            h = h + 1
    # if state[len(state) - 1] != 0:
    #    h = h + 1
    return h


def generate_succ(state):
    """ generates the successors of state and returns them in a list of states """
    blank = None  # index that 0 is stored in

    # finds what index in state that 0 is stored in
    for i in range(len(state)):
        if state[i] == 0:
            blank = i

    states = []

    # move up
    up = blank - 3
    if up < 0:
        up = len(state) + up
    states.append(swap(blank, up, state))

    # move down
    down = blank + 3
    if down >= len(state):
        down = down - len(state)
    states.append(swap(blank, down, state))

    # move left
    left = (blank % 3) - 1
    if left < 0:
        left = blank + 2
    else:
        left = blank - 1
    states.append(swap(blank, left, state))

    # move right
    right = (blank % 3) + 1
    if right > 2:
        right = blank - 2
    else:
        right = blank + 1
    states.append(swap(blank, right, state))

    # return a list of 4 states
    return states


def add_to_closed(closed, dict_state):
    """ adds dict_state to closed """
    # gets the state from state_dict
    new_state = dict_state['state']

    added = False

    # compares the state to all items in queue to find a match
    for dict in closed:
        if dict['state'] == new_state:
            # replaces dict in closed if the cost is lower
            if (dict['f'] >= dict_state['f']):
                closed.remove(dict)
                closed.append(dict_state)
            added = True

    # if not already in closed list, then add it
    if not added:
        closed.append(dict_state)


def find_dict(state, list):
    """ finds and returns the dictionary with the given state """
    dict = None
    # linear searches the list to find state
    for s in list:
        print(s['state'])
        if (state == s['state']):
            dict = s  # sets dict to s if the state is found

    # returns the dictionary with 'state': state
    return dict


def solve(state):
    """ solves the 8-torus problem in the least amount of moves possible """
    # run A* search algorithm
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # this is the desired state we wish to reach
    pq = priority_queue.PriorityQueue()

    # stores the given state as a dictionary and stores it in our priority queue
    state_dict = {'state': state, 'h': calculate_heuristic(state), 'parent': None, 'g': 0,
                  'f': calculate_heuristic(state)}
    pq.enqueue(state_dict)
    found = False

    closed = []  # stores all 'closed' nodes
    goal_dict = None  # will store the dictionary of the desired goal state

    # finds the goal state through the A* algorithm
    while not pq.is_empty():
        # pops the min-cost element from the queue, adds it to closed, and stores the state
        curr_dict = pq.pop()
        curr_state = curr_dict['state']
        add_to_closed(closed, curr_dict)

        # checks if goal_state is reached
        if curr_state == goal_state:
            goal_dict = curr_dict  # stores the goal dictionary
            break

        # generates and enqueues the successor states as dictionaries
        succ_states = generate_succ(curr_state)

        for succ in succ_states:
            enqueue = True
            succ_dict = {'state': succ, 'h': calculate_heuristic(succ), 'parent': curr_dict['state'],
                         'g': curr_dict['g'] + 1, 'f': calculate_heuristic(succ) + curr_dict['g'] + 1}
            for closed_dict in closed:
                if (closed_dict['state'] == succ_dict['state']):
                    if (closed_dict['f'] < succ_dict['f']):
                        enqueue = False
            if enqueue:
                pq.enqueue(succ_dict)

    prev = goal_dict  # this is our goal that we have reached
    moves = [prev]  # stores the list of moves requires to solve the puzzle

    # performs the second half of the A* algorithm by going through the closed list to produce a a list of moves
    # required to reach the goal state
    num_moves = int(goal_dict['f'])
    for i in range(num_moves):
        for curr in closed:
            if curr['state'] == prev['parent']:  # finds the parent state within the of the current state
                prev = curr;  # sets the previous state to the parent (current) state
                moves.append(curr)  # adds the current (parent) to the moves list
                break;

    # reverses the list of moves into the correct order
    moves = reversed(moves)

    # prints out the desired results
    for x in moves:
        print str(x['state']) + " h= " + str(x['h']) + " moves: " + str(x['g'])
    print("Max queue length: " + str(pq.max_len))
