def no_dups(s):
    # Your code here
    counts = {}
    if s == "":
        return ""
    
    # We loop through the string
    for word in s.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    word_list = []
    for word in counts:
        word_list.append(word)
    
    final_word_list = " ".join(word_list)

    return final_word_list

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))