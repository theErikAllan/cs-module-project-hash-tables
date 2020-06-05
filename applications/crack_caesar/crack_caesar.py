# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
global_counter = 0
counts = {}

freq_list = [
    'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
]

with open("ciphertext.txt") as f:
    words = f.read()

    # print("This is words: ", words)

    for character in words:
        # print("This is character: ", character)
        global_counter += 1

        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1

    characters = dict(
        sorted((counts.items()), key=lambda x: x[1], reverse=True))

    for element in characters:
        percent = (counts[element] / global_counter) * 100
        print("Character: ", element)
        print("Percent of total characters: ", percent)


# Correlate frequency of characters with
