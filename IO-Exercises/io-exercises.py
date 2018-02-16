# Exercise 1

file_name = input("Enter a file name to open: ")
with open(file_name, 'r') as fh:
    contents = fh.read()
    print(contents)

# Exercise 2

file_name = input("Enter a file name to open: ")
with open(file_name, 'a') as fh:
    fh.write("\nThis is a new file.\n")

# Exericse 3


file_name = input("Enter a file name to open: ")
with open(file_name, 'r') as fh:
    contents = fh.read()
    word = contents
    letter_dict = {
      
    }

    for i in range(0,len(word)):
        char = word[i:i + 1]
        letter_dict[char] = word.count(char)
    print(letter_dict)

    phrase = contents
    word_histogram = []
    word_dict = {
      
    }
    word_histogram = phrase.split()

    for i in range(0,len(word_histogram)):
        word_dict[word_histogram[i]] = phrase.count(word_histogram[i])

    print(word_dict)

# Exercise 4

import json
import matplotlib.pyplot as plot

with open('io-exercises/data.json', 'r') as fh:
    data = json.load(fh)
    plot.plot(data['data'])
    plot.show()
    plot.close()

# Bonus