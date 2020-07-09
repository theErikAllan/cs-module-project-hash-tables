# Your code here

with open("robin.txt") as f:
    words = f.read()
    word_list = words.split()

word_dict = {}

ignored = [ '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '!', '?' ]

for word in word_list:

    for character in ignored:
        word = word.replace(character, '')

    if word not in word_dict:
        word_dict[word.lower()] = -1
    else:
        word_dict[word.lower()] -= 1

tuple_list = list(word_dict.items())
tuple_list.sort(key=lambda e : (e[1], e[0]))

for item in tuple_list:
    hashes = "#" * abs(item[1])
    print(f'%15s  {hashes}' % item[0])