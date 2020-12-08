import days.day7 as day


DATA1 = [
  "light red bags contain 1 bright white bag, 2 muted yellow bags.",
  "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
  "bright white bags contain 1 shiny gold bag.",
  "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
  "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
  "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
  "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
  "faded blue bags contain no other bags.",
  "dotted black bags contain no other bags.",
]

DATA2 = [
  "shiny gold bags contain 2 dark red bags.",
  "dark red bags contain 2 dark orange bags.",
  "dark orange bags contain 2 dark yellow bags.",
  "dark yellow bags contain 2 dark green bags.",
  "dark green bags contain 2 dark blue bags.",
  "dark blue bags contain 2 dark violet bags.",
  "dark violet bags contain no other bags.",
]


def test_parse_line():
  first = "light red bags contain 1 bright white bag, 2 muted yellow bags."
  bag_data = day._parse_line(first)
  assert bag_data == ("light red", {"bright white": 1, "muted yellow": 2})


def test_map_line():
  first = "light red bags contain 1 bright white bag, 2 muted yellow bags."
  data = day._map_line(first, dict())
  assert data["light red"]["children"] == {"bright white": 1, "muted yellow": 2}
  assert data["bright white"]["parents"] == {"light red",}
  assert data["muted yellow"]["parents"] == {"light red",}


def test_map_all_data():
  data = day._map_all_data(DATA1)
  assert data["shiny gold"] == dict(
    children={"dark olive": 1, "vibrant plum": 2},
    parents={"bright white", "muted yellow"}
  )


def test_find_all_parents():
  data = day._map_all_data(DATA1)
  assert day.find_all_parents(data, "shiny gold") == {
    "bright white", "muted yellow", "dark orange", "light red"
  }


def test_count_all_children():
  data = day._map_all_data(DATA2)
  assert day.count_all_children(data, "shiny gold") == 126


def test_count_all_parents_for_gold_bag():
  data = day._map_all_data(DATA1)
  assert day.count_all_parents_for_gold_bag(data) == 4
  

def test_count_all_children_for_gold_bag():
  data = day._map_all_data(DATA2)
  assert day.count_all_children_for_gold_bag(data) == 126
  

def test_load_data():
  data = day.load_data()
  assert data["light chartreuse"]["children"] == {"mirrored yellow": 1, "vibrant violet": 2}
  assert data["light chartreuse"]["parents"] == set()


def test_final_results():
  data = day.load_data()
  assert day.part1(data) == 252
  assert day.part2(data) == 35487