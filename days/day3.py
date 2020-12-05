from functools import partial
from lib.loaders import load_file_as_strings

SLOPES = ((1,1), (3,1), (5,1), (7,1), (1,2))


def count_trees(x_slope, y_slope, rows):
  row_len = len(rows[0])
  coords = [
    (i * x_slope % row_len, y)
    for i, y in enumerate(range(0, len(rows), y_slope))
  ]
  return sum(1 if rows[y][x] == "#" else 0 for x, y in coords)


def count_trees_for_slopes(slopes, rows):
  total = 1
  for x_slope, y_slope in slopes:
    total *= count_trees(x_slope, y_slope, rows)
  return total


def load_data():
  return load_file_as_strings("day3.txt")


part1 = partial(count_trees, 3, 1)
part2 = partial(count_trees_for_slopes, SLOPES)
