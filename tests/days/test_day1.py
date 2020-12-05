from lib.loaders import as_ints
import days.day1 as day

DATA = as_ints("""
1721
979
366
299
675
1456
""")

def test_find_pairs_for_sum():
  results = day.find_pair_for_sum(2020, DATA)
  assert results == ({299, 1721}, 514579)


def test_find_trio_for_sum():
  results = day.find_trio_for_sum(2020, DATA)
  assert results == ({366, 675, 979}, 241861950)


def test_load_data():
  data = day.load_data()
  assert data[0] == 1597


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == ({909, 1111}, 1009899)
  assert day.part2(data) == ({74, 1564, 382}, 44211152)