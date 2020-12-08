from functools import reduce

from lib.loaders import load_file_as_strings


def _new_node():
  return dict(children=dict(), parents=set())


def _parse_line(line):
  outer_bag, inner_text = line.split(" bags contain ")
  bag_words = [
    chunk.split(" ") 
    for chunk in inner_text.split(", ")
    if not chunk.startswith("no other")
  ]
  children = {
    " ".join(words[1:3]): int(words[0]) 
    for words in bag_words
  }
  return outer_bag, children


def _map_line(line, data):
  outer_bag, children = _parse_line(line)
  new_data = dict(data)

  new_data[outer_bag] = new_data.get(outer_bag) or _new_node()
  new_data[outer_bag]["children"].update(children)

  for inner_bag, qty in children.items():
    new_data[inner_bag] = new_data.get(inner_bag) or _new_node()
    new_data[inner_bag]["parents"].add(outer_bag)

  return new_data


def _map_all_data(data):
  return reduce(lambda a, b: _map_line(b, a), [dict(), *data])


def find_all_parents(data, bag):
  return reduce(
    lambda a, b: a | find_all_parents(data, b),
    [set(data[bag]["parents"]), *data[bag]["parents"]]
  )


def count_all_children(data, bag):
  return (
    sum(data[bag]["children"].values()) +
    sum(
      qty * count_all_children(data, child) 
      for child, qty in data[bag]["children"].items()
    )
  )


def count_all_parents_for_gold_bag(data):
  return len(find_all_parents(data, "shiny gold"))


def count_all_children_for_gold_bag(data):
  return count_all_children(data, "shiny gold")


def load_data():
  return _map_all_data(load_file_as_strings("day7.txt"))


part1 = count_all_parents_for_gold_bag
part2 = count_all_children_for_gold_bag