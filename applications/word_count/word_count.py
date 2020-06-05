def word_count(s):
    # Your code here
    counts = {}
    if s == "":
        return {}

    for word in s.split():
        word = word.lower()
        new_word = ""
        for character in word:
            if character.isalnum() or character == "\'":
                new_word += character
                # print("This is new_word: ", new_word)

        if new_word in counts:
            counts[new_word] += 1
            # print("This is counts: ", counts[new_word])
        elif new_word == "":
            return {}
        else:
            counts[new_word] = 1
    
    words = dict(counts.items())
    print("This is words: ", words)
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))