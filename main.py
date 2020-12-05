import re
import importlib

import pytest

day_input = input("What day or days should I run (ie. 1,4-5,8)? ")
day_numbers = re.sub(
  "(\d+)-(\d+)", 
  lambda p: ",".join(str(i) for i in range(int(p.group(1)), int(p.group(2)) + 1)), 
  day_input.replace(" ", "")
).split(",")

for day_number in day_numbers:
  try: 
    day = importlib.import_module(f"days.day{day_number}")
  except ModuleNotFoundError:
    print("That day isn't implemented yet.")
    exit()
  
  print("\n")
  print("*"*80)
  print(f"RUNNING DAY {day_number}")
  print("*"*80)

  pytest.main([f"tests/days/test_day{day_number}.py"])
  
  data = day.load_data()
  print(f"Part 1: {day.part1(data)}")
  print(f"Part 2: {day.part2(data)}")