word_count = {}
count_word = {}

def build_dictionaries(words):

    # build word_count dictionary
    for w in words:
        if w not in word_count:
            word_count[w] = 0
        
        word_count[w] += 1

    # build count_word dictionary
    for word, count in word_count.items():
        if count not in count_word:
            count_word[count] = []
        count_word[count].append(word)


    for i in sorted(count_word, reverse=True):

        # handle case where only 1 word has a particular count
        if len(count_word[i]) == 1:
            print("%-*s" % (20, count_word[i][0]), end="")
            for j in range(word_count[count_word[i][0]]):
                print("#", end="")
            print()

        # handle case where more than 1 word has a particular count
        else:
            for k in sorted(count_word[i]):
                print("%-*s" % (20, k), end="")
                for m in range(word_count[k]):
                    print("#", end="")
                print()



# Read in all the words in one go
with open("robin.txt") as f:
    s = f.read()

punctuation = '\":;,.-+=/\\|[]\{\}()*^&'

# remove all punctuation from string
no_punct = ""
for char in s:
    if char not in punctuation:
        no_punct = no_punct + char

# make string lowercase, split string into words, and place words in a list
words = no_punct.lower().split()
build_dictionaries(words)  

