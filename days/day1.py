from timeit import timeit
from lib.loaders import load_file_as_ints

def find_pair_for_sum(target_sum, rows):
  targets = set()
  for value in rows:
    diff = target_sum - value
    if diff in targets:
      return (value, diff, value * diff)
    else:
      targets.add(value)


def find_trio_for_sum(target_sum, rows):
  for value in rows:
    diff = 2020 - value
    results = find_pair_for_sum(diff, rows[1:])
    if results:
      return (value, *results[0:2], value * results[2])


def load_data():
  return load_file_as_ints("day1.txt")


def part1(data):
  return find_pair_for_sum(2020, data)


def part2(data):
  return find_trio_for_sum(2020, data)

