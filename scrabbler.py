from tkinter import *

root = Tk()
root.title("Scrabbler")
root.geometry("720x180+700+100")

label_text = Label(root, text = "Enter your letters: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 10)
label_op_chars = Label(root, text = "Enter open letters: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 40)
label_string_pos = Label(root, text = "String in position: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 70)
label_pos_index = Label(root, text = "Index: ", font = ("arial", 20, "bold"), fg = "black").place(x = 400, y = 70)
label_min_length = Label(root, text = "Minimum Length:  ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 100)
label_min_points = Label(root, text = "Minimum Points:  ", font = ("arial", 20, "bold"), fg = "black").place(x = 400, y = 100)

user_input = StringVar()
open_chars = StringVar()
string_pos = StringVar()
string_index = IntVar()
min_length = IntVar()
min_points = IntVar()

entry_box = Entry(root, textvariable = user_input, width = 50).place(x = 250, y = 10)
entry_op_char = Entry(root, textvariable = open_chars, width = 50).place(x = 250, y = 40)
entry_string_pos = Entry(root, textvariable = string_pos, width = 15).place(x = 250, y = 70)
entry_string_index = Entry(root, textvariable = string_index, width = 10).place(x = 500, y = 70)
entry_min_length =  Entry(root, textvariable = min_length, width = 10).place(x = 250, y = 100)
entry_min_points =  Entry(root, textvariable = min_points, width = 10).place(x = 600, y = 100)

points = [('a', 1), ('b', 3), ('c', 3), ('d', 2), ('e', 1), ('f', 4),
('g', 2), ('h', 4), ('i', 1), ('j', 8), ('k', 5), ('l', 1), ('m', 3),
('n', 1), ('o', 1), ('p', 3), ('q', 10), ('r', 1), ('s', 1), ('t', 1),
('u', 1), ('v', 4), ('w', 4), ('x', 8), ('y', 4), ('z', 10)]

file = open('dict_1.txt', 'r')
word_list = file.read().split('\n')
print('\n')
def get_unique_letter(word, chars):
  for i in range(len(word)):
    if word[i:i+1] in chars:
      chars.pop(chars.index(word[i:i+1]))
    else:
      return word[i:i+1]
  return 'null'

def get_points(word):
  total = 0
  for i in range(len(word)):
    letter = word[i:i+1]
    for i in range(len(points)):
      if letter == points[i][0]:
        total += points[i][1]
  return total

def find_combinations():
  combinations = []
  pos_string = string_pos.get()
  print('letters available: ' + user_input.get())
  print('open letters: ' + open_chars.get() + '\n')
  for word in word_list:
    letters_1 = list(user_input.get())
    match = 0
    for i in range(len(word)):
      if word[i:i+1] in letters_1:
        match += 1
        letters_1.pop(letters_1.index(word[i:i+1]))
    if match > len(word) - 2:
      if len(open_chars.get()) > 0:
        open_chars_list = list(open_chars.get())
        unique_letter = get_unique_letter(word, list(user_input.get()))
        if unique_letter in open_chars_list or unique_letter == 'null':
          combinations.append(word)
      else:
        combinations.append(word)
  for comb in combinations:
    if len(comb) >= min_length.get():
      if get_points(comb) >= min_points.get():
        if len(pos_string) > 0:
          if string_index.get() > 0:
            if comb[string_index.get()-1:string_index.get()+len(pos_string)-1] == pos_string:
              print(comb, get_points(comb))
          elif string_index.get() == 0:
            if pos_string in comb:
              print(comb, get_points(comb))
        else:
          print(comb, get_points(comb))
  print('\n')
submit = Button(root, text = "Submit", width = 30, bg = 'lightblue', command = find_combinations).place(x = 250, y = 130)
root.mainloop()
