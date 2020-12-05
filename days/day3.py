from lib.loaders import load_file_as_strings

def count_trees(rows, x_slope, y_slope):
  row_len = len(rows[0])
  coords = [
    (i * x_slope % row_len, y)
    for i, y in enumerate(range(0, len(rows), y_slope))
  ]
  return sum(1 if rows[y][x] == "#" else 0 for x, y in coords)


def count_trees_for_slopes(rows, slopes):
  total = 1
  for x_slope, y_slope in slopes:
    total *= count_trees(rows, x_slope, y_slope)
  return total


def load_data():
  return load_file_as_strings("day3.txt")


def part1(data):
  return count_trees(data, 3, 1)


def part2(data):
  return count_trees_for_slopes(data, [(1,1),(3,1),(5,1),(7,1),(1,2)])
