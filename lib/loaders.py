def load_file(name):
  with open(f"./data/{name}") as in_file:
    return in_file.read()


def as_strings(content):
  return [line for line in content.split("\n") if line]


def as_ints(content):
  return [int(line) for line in content.split("\n") if line]


def as_blocks(content):
  return [block.replace("\n", " ") for block in content.split("\n\n") if block]


def load_file_as_strings(name):
  return as_strings(load_file(name))


def load_file_as_ints(name):
  return as_ints(load_file(name))


def load_file_as_blocks(name):
  return as_blocks(load_file(name))
