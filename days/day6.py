from functools import reduce

from lib.loaders import load_file_as_blocks_of_strings


def _unify(lines):
  return reduce(lambda a, b: a | b, [set(l) for l in lines])


def _intersect(lines):
  return reduce(lambda a, b: a & b, [set(l) for l in lines])


def tally_uniques(blocks):
  return sum(len(_unify(block)) for block in blocks)  


def tally_common(blocks):
  return sum(len(_intersect(block)) for block in blocks)  


def load_data():
  return load_file_as_blocks_of_strings("day6.txt")


part1 = tally_uniques
part2 = tally_common