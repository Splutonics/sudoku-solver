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
    for key in values:
        if len(values[key])==1:
            for peer in peers[key]:
                if values[key] in values[peer]:
                  values[peer] = values[peer].replace(values[key],'')
                  none_deleted = False

    return values


if __name__ == '__main__':
    grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    display(eliminate(grid_values(grid)))
