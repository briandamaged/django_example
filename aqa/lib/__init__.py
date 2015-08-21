
def normalize_string(string):
  """
  Trims a string and normalizes its whitespace.
  """
  components = string.split()
  return " ".join(components)

def truncate(string, length):
  """
  Ensures that the string does not exceed the specified
  length.  If it does, then truncate it and add "...".
  """
  if string is None:
    return None

  string = normalize_string(string)

  if len(string) <= length:
    return string


  # Why length - 3?  Because we need to account for
  # the "..." characters, of course!
  length_limit = length - 3

  components = string.split()

  # If the first word already exceeds the limit, then
  # I guess we just truncate the word.  Oh well.
  if len(components[0]) > length:
    return components[0][:length_limit] + "..."

  # Otherwise, we'll grab as many words as we can until
  # we exceed the length limit.
  current_length = 0
  for index, word in enumerate(components):
    current_length = current_length + len(word)

    if current_length > length_limit:
      return " ".join(components[:index - 1]) + "..."


