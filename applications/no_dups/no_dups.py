def no_dups(s):
    cache = {}

    # split string into words
    words = s.split()

    no_dups = []

    # check if word is already in cache
    # if not, add word to cache and to no_dups list
    for w in words:
        if w not in cache:
            cache[w] = w
            no_dups.append(w)

    # return input string without duplicate words
    return ' '.join(no_dups)


    print(words)
    print(no_dups)
    print(cache)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))