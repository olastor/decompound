from nltk.stem import SnowballStemmer
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

  # Prepare dictionary for O(1) lookup and stemming.
  stemmer = SnowballStemmer('german')
  dictionary = { w: w for w in set([ stemmer.stem(w) for w in vocabulary ]) }

  # Dict containing found words within target word with their indexes
  subwords = defaultdict(set)

  # This list contains the indexes from which a word should be searched.
  #
  # Example:
  #
  # - word = "Autobahn" and todo = [0] => Check "A", "Au", "Aut", "Auto" ...
  # - word = "Autobahn" and todo = [0, 3] => Check "A", "Au", ... AND "b", "ba", "bah", "bahn" ...
  todo = [0]

  # Phase 1: Find all subwords
  fugenlaute = ['e', 's', 'es', 'n', 'en', 'er', 'ens']

  while todo:
    if not todo[0] in subwords:
      for i in range(todo[0] + 1, len(word) + 1):
        current_subword = word[todo[0]:i]
        current_subword_stemmed = stemmer.stem(current_subword)

        if current_subword_stemmed in dictionary:
          # determine possible indices for the 
          # next word.
          
          # 1. Just right after the non-stemmed subword
          next_indices = [todo[0] + len(current_subword)]

          # 2. If 'Fugenlaut' comes afterwards, respect that too
          #    as a possible start of a new subword.
          for j in range(1, 3):
            tmp = next_indices[0] + j

            if tmp > len(word):
              break

            if word[next_indices[0]:tmp] in fugenlaute:
              next_indices.append(tmp) 

          # Add subword to dict 
          subwords[todo[0]] = subwords[todo[0]].union(next_indices)

          # Update todo list
          todo += next_indices

    del todo[0]

  # Phase 2: Try to combine all subwords
  result = []

  def tree_search(i, configuration):
    if i == len(word):
      if configuration:
        # Found a match
        result.append(configuration)

      return

    if not i in subwords:
      return

    for j in subwords[i]:
      tree_search(j, configuration + [word[i:j]])

  tree_search(0, [])

  return result
