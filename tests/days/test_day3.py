from lib.loaders import as_strings
import days.day3 as day

DATA = as_strings("""
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""")


def test_count_trees():
  assert day.count_trees(3, 1, DATA) == 7
  assert day.count_trees(1, 1, DATA) == 2
  assert day.count_trees(5, 1, DATA) == 3
  assert day.count_trees(7, 1, DATA) == 4
  assert day.count_trees(1, 2, DATA) == 2


def test_count_trees_for_slopes():
  assert day.count_trees_for_slopes(day.SLOPES, DATA) == 336


def test_load_data():
  results = day.load_data()
  assert results[0] == "....#..#.................#..#.."


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == 237 
  assert day.part2(data) == 2106818610