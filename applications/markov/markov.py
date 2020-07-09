import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    word_list = words.split()

# TODO: analyze which words can follow other words
# Your code here

word_dict = {}
counter = 0

for word in word_list[:-1]:
    if word not in word_dict:
        word_dict[word] = []
    word_dict[word].append(word_list[counter + 1])
    counter += 1

# separate lists for start and stop words
# if word starts with " or uppercase
# if word ends with " or period

# print("Word list: ", word_list)
print("\n")
print("Word dictionary: ", word_dict)


# TODO: construct 5 random sentences
# Your code here

