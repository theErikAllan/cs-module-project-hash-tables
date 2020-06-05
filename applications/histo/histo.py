def histo(file):
    with open(file) as f:
        words = f.read()
    
    counts = {}
    
    for word in words.split():
        word = word.lower()
        new_word = ""
        for character in word:
            if character.isalnum():
                new_word += character
        
        # longest_word = ?

        if new_word in counts:
            counts[new_word] += 1
        elif new_word == "":
            return None
        else:
            counts[new_word] = 1

    words = dict(sorted((counts.items()), key=lambda x: x[1], reverse=True))
    # print("This is words: ", words)

    for element in words:
        # print("Word: ", element)
        hashes = "#" * counts[element]
        # print(f'{element} {hashes}')
        spaces = " " * 8
        print(f'{element}: {spaces} {hashes}')


if __name__ == "__main__":
    print(histo("robin.txt"))