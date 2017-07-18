# Change the below line to input the state of the puzzle that is trying to be solved.
# 0 is considered to be the empty tile. The default configuration here is the puzzle
# already in its solved state (solved in zero moves, not very useful).

puzzle_to_solve = [1, 2, 3, 4,
                   5, 6, 7, 8,
                   9, 10, 11, 12,
                   13, 14, 15, 0]

puzzle_size = 4

class State():
  def __init__(self, tiles):
    self.tiles = tiles

  # Produces a brief textual description of the puzzle's state.
  def __str__(self):
    tiles = self.tiles
    text = ""
    for i in range(0, len(tiles), puzzle_size):
        text += "["
        for j in range(0, puzzle_size):
            text += str(tiles[i + j]) + " "
            if tiles[i + j] < 10:
                text += " "
        text = text[:-1] + "]\n"
    return text

  def __eq__(self, s2):
    if not (type(self)==type(s2)):
        return False
    t1 = self.tiles; t2 = s2.tiles
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True

  def __hash__(self):
    return (str(self)).__hash__()

  # Performs an appropriately deep copy of a state,
  # for use by operators in creating new states.
  def __copy__(self):
    news = State([])
    for i in range(len(self.tiles)):
        news.tiles.append(self.tiles[i])
    return news

INITIAL_STATE = State(puzzle_to_solve)

CREATE_INITIAL_STATE = lambda: INITIAL_STATE

# This can be changed if the desired goal state is not the puzzle simply in
# numerical order.
GOAL_STATE = State([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])

def can_move(s,From,To):
  try:
   if s.tiles[From] == 0:
       return True
   return False
  except (Exception) as e:
   print(e)

def move(s,From,To):
  news = s.__copy__() # start with a deep copy.
  current_zero_index = From
  news.tiles[From] = news.tiles[To]
  news.tiles[To] = 0
  return news # return new state

def goal_test(s):
    for i in range(len(GOAL_STATE.tiles)):
        if s.tiles[i] != GOAL_STATE.tiles[i]:
            return False
    return True

def goal_message(s):
  return "The Fifteen Puzzle is solved!"

# Defines the operator class which tells the search algorithm what moves it is allowed to make.
class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

# Allowed index movements for the puzzle state. These are listed manually to
# avoid writing out tricky math that would be present with using just one list
# to represent the 2D puzzle, which is done here to save memory.
tile_combinations = [[0,1],[0,4],[1,0],[1,2],[1,5],[2,1],[2,3],[2,6],[3,2],[3,7],
                     [4,0],[4,5],[4,8],[5,1],[5,4],[5,6],[5,9],[6,2],[6,5],[6,7],[6,10],
                     [7,3],[7,6],[7,11],[8,4],[8,9],[8,12],[9,5],[9,8],[9,10],[9,13],
                     [10,6],[10,9],[10,11],[10,14],[11,7],[11,10],[11,15],[12,8],[12,13],
                     [13,9],[13,12],[13,14],[14,10],[14,13],[14,15],[15,11],[15,14]]

# Iterates through the possible index movements and selects only the allowed
# tile movements.
OPERATORS = [Operator("Move tile from "+str(m[0])+" to "+str(m[1]),
                      lambda s,p1=m[0],q1=m[1]: can_move(s,p1,q1),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p1=m[0],q1=m[1]: move(s,p1,q1) )
             for m in tile_combinations]

GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)

# Calculates the puzzle's "Manhattan Distance", an admissable heurstic for the puzzle.
def manhattan_distance(s):
    distance = 0
    for i in range(len(s.tiles) - 1):
        x_current = s.tiles.index(i)
        x_goal = GOAL_STATE.tiles.index(i)
        y_current = s.tiles.index(i)
        y_goal = GOAL_STATE.tiles.index(i)
        distance += abs((x_current % puzzle_size) - (x_goal % puzzle_size)) + abs((y_current // puzzle_size) - (y_goal // puzzle_size))
    return distance

# Other heuristics can be implemented and added here.
HEURISTICS = {'manhattan_distance': manhattan_distance}