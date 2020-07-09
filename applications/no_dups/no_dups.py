def no_dups(s):
    # Your code here
    word_dict = {}

    word_list = s.split()

    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
            # print("Word set: ", word_dict)
    
    new_list = list(word_dict)

    final_string = " ".join(new_list)

    # print("Final string: ", final_string)

    return final_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))