def break_word(word):
  """we don't konw about it"""
  stuff = word.split(' ')
  return stuff

def sort_word(words):
  """know words"""
  return sorted(words)

def print_first_word(words):
  """print first word"""
  word = words.pop(0)
  print(word)

def print_last_word(words):
  """print lats words"""
  word = words.pop(-1)
  print(word)

def sort_sentence(sentence):
  """print a sentence"""
  words = break_word(sentence)
  return sorted(words)

def print_first_and_last(sentence):
  """"print first and last sentence"""
  words = break_word(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sort(sentence):
  """"print sort sentence"""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)