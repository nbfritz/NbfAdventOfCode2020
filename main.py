import importlib

while True:
  day_number = input("What day should I run? ")
  if not day_number:
    break

  try: 
    day = importlib.import_module(f"days.day{day_number}")
    importlib.reload(day)
    
    data = day.load_data()
    print(f"Part 1: {day.part1(data)}")
    print(f"Part 2: {day.part2(data)}")
    
  except ModuleNotFoundError:
    print("That day isn't implemented yet.")