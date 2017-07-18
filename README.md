# Fifteen Puzzle Solver

This Python program implements and solves the classic sliding tile Fifteen Puzzle, aiming to do so as efficiently as possible. This program uses A* search to find the solution path, and uses the [Manhattan Distance](https://heuristicswiki.wikispaces.com/Manhattan+Distance) as its primary heuristic. The code is written so that it is easy to define and utilize other admissable heuristics if desired. Simply enter the current state of the Fifteen Puzzle to be solved at the top of FifteenPuzzleSolver.py and then run AStar.py, and a solution path will be generated.

Example usage:

    Welcome to the Fifteen Puzzle Solver!
    Initial State:
    [1  2  3  0 ]
    [5  6  8  4 ]
    [9  10 7  12]
    [13 14 11 15]
    
    The Fifteen Puzzle is solved!
    Solution path: 
    [1  2  3  0 ]
    [5  6  8  4 ]
    [9  10 7  12]
    [13 14 11 15]
    
    [1  2  3  4 ]
    [5  6  8  0 ]
    [9  10 7  12]
    [13 14 11 15]
    
    [1  2  3  4 ]
    [5  6  0  8 ]
    [9  10 7  12]
    [13 14 11 15]
    
    [1  2  3  4 ]
    [5  6  7  8 ]
    [9  10 0  12]
    [13 14 11 15]
    
    [1  2  3  4 ]
    [5  6  7  8 ]
    [9  10 11 12]
    [13 14 0  15]
    
    [1  2  3  4 ]
    [5  6  7  8 ]
    [9  10 11 12]
    [13 14 15 0 ]
    
    
    Path length = 5
    5 states examined.