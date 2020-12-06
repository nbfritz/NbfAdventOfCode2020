import days.day6 as day

DATA = [
  ["abc"],
  ["a", "b", "c"],
  ["ab", "ac"],
  ["a", "a", "a", "a"],
  ["b"],
]


def test_unify():
  assert day._unify(["abcx", "abcy", "abcz"]) == {"a", "b", "c", "x", "y", "z"}


def test_intersect():
  assert day._intersect(["abcx", "abcy", "abcz"]) == {"a", "b", "c"}


def test_tally_uniques():
  assert day.tally_uniques(DATA) == 11


def test_tally_common():
  assert day.tally_common(DATA) == 6


def test_load_data():
  data = day.load_data()
  assert data[0] == ["mz", "mz", "mzch"]


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == 6583
  assert day.part2(data) == 3290