# inp = input()
# try:
#   topics = inp.split(', ')
# except:
#   topics = [inp]

# points = [('a', 1), ('b', 3), ('c', 3), ('d', 2), ('e', 1), ('f', 4), ('g', 2), ('h', 4), ('i', 1), ('j', 8), ('k', 5), ('l', 1), ('m', 3), ('n', 1), ('o', 1), ('p', 3), ('q', 10), ('r', 1), ('s', 1), ('t', 1), ('u', 1), ('v', 4), ('w', 4), ('x', 8), ('y', 4), ('z', 10)]

# letters = list(topics[0])
# file = open('/Users/rishabhtatia/Desktop/coding/py/projects/assets/dict_1.txt', 'r')
# word_list = file.read().split('\n')
# combinations = []

# def get_unique_letter(word, chars):
#   for i in range(len(word)):
#     if word[i:i+1] in chars:
#       chars.pop(chars.index(word[i:i+1]))
#     else:
#       return word[i:i+1]
#   return 'null'

# def get_points(word):
#   total = 0
#   for i in range(len(word)):
#     letter = word[i:i+1]
#     for i in range(len(points)):
#       if letter == points[i][0]:
#         total += points[i][1]
#   return total

# for word in word_list:
#   letters_1 = list(topics[0])
#   match = 0
#   for i in range(len(word)):
#     if word[i:i+1] in letters_1:
#       match += 1
#       letters_1.pop(letters_1.index(word[i:i+1]))
#   if match > len(word) - 2:
#     if len(topics) > 1:
#       open_chars = list(topics[1])
#       unique_letter = get_unique_letter(word, list(topics[0]))
#       if unique_letter in open_chars or unique_letter == 'null':
#         combinations.append(word)
#     else:
#       combinations.append(word)

# for comb in combinations:
#   if len(comb) > 2:
#     if get_points(comb) > 0:
#       # if 'f' in comb:
#       # if comb[4] == 't':
#       # if len(comb) > 6:
#       print(comb, get_points(comb))

import keras