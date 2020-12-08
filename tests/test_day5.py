from lib.loaders import as_strings
import days.day5 as day


DATA1 = as_strings("""
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
""")

DATA2 = as_strings("""
FFFFBBBRRR
FFFFBBBRRL
FFFFBBBRLL
""")


def test_parse_pass_id():
  assert day._parse_pass_id("BFFFBBFRRR") == 567
  assert day._parse_pass_id("FFFBBBFRRR") == 119
  assert day._parse_pass_id("BBFFBBFRLL") == 820
  
  assert day._parse_pass_id("FFFFBBBRRR") == 63
  assert day._parse_pass_id("FFFFBBBRRL") == 62
  assert day._parse_pass_id("FFFFBBBRLL") == 60


def test_find_highest_pass_id():
  assert day.find_highest_pass_id(DATA1) == 820


def test_find_missing_pass_id():
  assert day.find_missing_pass_id(DATA2) == 61
  

def test_load_data():
  data = day.load_data()
  assert data[0] == "FFBFBFBRRL"


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == 904
  assert day.part2(data) == 669