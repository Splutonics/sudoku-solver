from utils import *
from eliminate import *

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    for box in values:
      unit_value = ''
      for unit in units[box]:
        'look through each unit (array of boxes)'
        'check what numbers show up'
        # if count(each number in box)= count(each number in unit summed up)(aka 1)
        #assign that number to the box

        # add up the whole unit into a single string representation
        for element in unit:
          unit_value = unit_value + values[element]

        # for each number in the current box
        for number in values[box]:
          # if the box has more than one number, and it only shows up once in
          # the unit, then assign that number to the current box
          if len(values[box]) != 1 and unit_value.count(number) == 1 :
            values[box] = number
            break

    return values

if __name__ == '__main__':
    grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    display(only_choice(eliminate(grid_values(grid))))
