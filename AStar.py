import sys
import importlib
from queue import PriorityQueue

import FifteenPuzzleSolver as Problem

print("\nWelcome to the Fifteen Puzzle Solver!")
COUNT = None
BACKLINKS = {}

# Creates a class called TupleSort which can store the cost, total moves,
# and current state of the puzzle. TupleSort is comparable based on cost,
# allowing it to be used in a priority queue.
class TupleSort():
    def __init__(self, cost, moves, state):
        self.cost = cost
        self.moves = moves
        self.state = state

    def __lt__(self, rhs):
        return self.cost < rhs.cost

    def __gt__(self, rhs):
        return self.cost > rhs.cost

    def __le__(self, rhs):
        return self.cost <= rhs.cost

    def __ge__(self, rhs):
        return self.cost >= rhs.cost

    def get_state(self):
        return self.state

    def get_moves(self):
        return self.moves

    def get_cost(self):
        return self.cost

# Grabs any heuristics implemented in FifteenPuzzleSolver.py, additional heuristics
# should be added here
heuristics = lambda s: Problem.HEURISTICS['manhattan_distance'](s)

# Begins the AStar search to find the puzzle's solution, and returns the solution once found.
def runAStar():
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS
    COUNT = 0
    BACKLINKS = {}
    path = AStar(initial_state)
    print(str(COUNT) + " states examined.")
    return path

# AStar search implementation. Uses the Fifteen Puzzle's Manhattan Distance as its
# primary heuristic.
def AStar(initial_state):
    global COUNT, BACKLINKS
    OPEN = PriorityQueue()
    cost_to_complete = heuristics(initial_state)
    OPEN.put(TupleSort(cost_to_complete, 0, initial_state))
    CLOSED = []
    BACKLINKS[initial_state] = -1

    while not OPEN.empty():
        tuple = OPEN.get()
        S = tuple.get_state()
        while S in CLOSED:
            tuple = OPEN.get()
            S = tuple.get_state()
        CLOSED.append(S)
        moves = tuple.get_moves()
        cost = tuple.get_cost()

        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S)
            return path

        COUNT += 1

        for op in Problem.OPERATORS:
            if op.precond(S):
                new_state = op.state_transf(S)
                cost = heuristics(new_state)
                local_moves = moves
                total_cost = cost + moves
                if not (new_state in CLOSED):
                    OPEN.put(TupleSort(total_cost, local_moves, new_state))
                    BACKLINKS[new_state] = S

# Once the optimal solution is found, iterates back through the puzzles previous states
# that were iterated through originally, in order to show the solution path.
def backtrace(S):
    global BACKLINKS
    path = []
    while not S == -1:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(s)
    print("\nPath length = " + str(len(path) - 1))
    return path

if __name__ == '__main__':
    path = runAStar()