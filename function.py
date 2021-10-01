from utils import *


def search(values: dict):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    # if the length of the values in all boxes is 1, a solution has been found
    if values == False:
        return False
    if all([len(values[value]) == 1 for value in boxes]):
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    n, search_box = min((len(values[box]), box)
                        for box in boxes if len(values[box]) > 1)
    for number in values[search_box]:
        temp_values = values.copy()
        temp_values[search_box] = number
        attempt = search(temp_values)
        if attempt:
            return attempt

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!

    # If you're stuck, see the solution.py tab!


if __name__ == '__main__':
    grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    # search(grid_values(grid2))
    display(search(grid_values(grid2)))
