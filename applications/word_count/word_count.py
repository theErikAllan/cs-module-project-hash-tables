def word_count(s):
    # Your code here
    counter = {}

    if len(s) == 0:
        return {}
    
    else:
        word_list = s.split()
        for word in word_list:
            new_word = ""
            for character in word:
                if character.isalpha():
                    new_word += character.lower()
                elif character == "'":
                    new_word += character
            # print("This is new word: ", new_word)

            if new_word == "":
                return {}

            if new_word not in counter:
                counter[new_word] = 1
            else:
                counter[new_word] += 1
        
        return counter
        
    print("Counter: ", counter)



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))