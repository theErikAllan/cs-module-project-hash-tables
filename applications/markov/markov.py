import random

start_words = {}
stop_words = {}

stop_chars = [".", "!", "?"]

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

[(One), (thing), (was)]
   |       |       |
(thing)  (was)  (certain)
   |
 (paw)

 # Need if statement that doesn't add word after if word[-1] == .


# TODO: analyze which words can follow other words
# Your code here
    for word in words.split():
        if word[0].isupper():
            print("This is a start word: ", word)

        if word[0] == "\"" and word[1].isupper():
            print("This is a start word: ", word)


        if word[-1] in stop_chars:
            print("This is a stop word: ", word)
        
        if len(word) > 1:
            if word[-1] == "\"" and word[-2] in stop_chars:
                print("This is a stop word: ", word)


# TODO: construct 5 random sentences
# Your code here

