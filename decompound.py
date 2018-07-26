from collections import defaultdict

def decompound(word, vocabulary):
  '''Decompounds a word.

  This function tries to split a given word up into combinations
  of different words from a given vocabulary.

  Example:
    - decompound('toothbrush', ['tooth', 'brush']) => [['tooth', 'brush']]

  Arguments:
    word {str} -- Target word
    vocabulary {str[]} -- Target vocabulary

  Returns:
    str[][] -- List of possible combinations to construct the target word
               with words from the vocabulary
  '''

  # Prepare dictionary for O(1) lookup and case insensitivity.
  dictionary = { w: w for w in set([ w.lower() for w in vocabulary ]) }

  # Working object containing found words within target word with their indexes
  subwords = defaultdict(list)

  # This list contains the indexes from which a word should be searched.
  #
  # Example:
  #
  # - word = "Autobahn" and todo = [0] => Check "A", "Au", "Aut", "Auto" ...
  # - word = "Autobahn" and todo = [0, 3] => Check "A", "Au", ... AND "b", "ba", "bah", "bahn" ...
  todo = [0]

  # Phase 1: Find all subwords
  while todo:
    if not todo[0] in subwords:
      for i in range(todo[0] + 1, len(word) + 1):
        temp = word[todo[0]:i]
        # print('Checking ' + temp)

        if temp in dictionary:
          # print('Found ' + temp + ' at ' + str(todo[0]))
          # Found a new word for subwords
          subwords[todo[0]].append(temp)

          # Add new index to todo
          todo.append(todo[0] + len(temp))

    del todo[0]

  # Phase 2: Try to combine all subwords
  result = []

  def tree_search(index, configuration):
    w_length, w_words = configuration

    if w_length == len(word):
      result.append(w_words)
      return

    if not index in subwords:
      return

    for w in subwords[index]:
      tree_search(index + len(w), (w_length + len(w), w_words + [w]))

  tree_search(0, (0, []))

  return result
