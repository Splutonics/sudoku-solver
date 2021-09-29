from utils import *


def eliminate(values: dict) -> dict:
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    eliminated_grid = values

    while True:
        none_deleted = True
        for key in eliminated_grid:
            if len(eliminated_grid[key])==1:
                for peer in peers[key]:
                     pass


        if none_deleted:
            break

    return eliminated_grid


if __name__ == '__main__':
    grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    display(eliminate(grid_values(grid)))
