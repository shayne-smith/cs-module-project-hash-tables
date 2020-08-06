import random

lookup_table = {}

# TODO: analyze which words can follow other words
def build_dataset(words):

    for k, v in enumerate(words):

        if words[k] not in lookup_table:
            lookup_table[v] = []
            
        if k < len(words) - 1:
            lookup_table[v].append(words[k + 1])

def build_sentence():
    start = random.choice(list(lookup_table.keys()))

    # find start word
    while True:
        if start[0].isupper() or (start[0] == "\"" and start[1].isupper()):
            break
        start = random.choice(list(lookup_table.keys()))

    # print start word
    print(start)

    next_word = random.choice(lookup_table[start])

    while True:
        if next_word[-1] == "." or next_word[-1] == "?" or next_word[-1] == "!":
            break
        if next_word[-1] == "\"" and len(next_word) >= 2:
            if next_word[-2] == "." or next_word[-2] == "?" or next_word[-2] == "!":
                break
        
        print(next_word)
        next_word = random.choice(lookup_table[next_word])

    print(next_word)


# Read in all the words in one go
with open("input.txt") as f:
    s = f.read()
    words = s.split()
    build_dataset(words)

# Build 5 sentences
for i in range(5):
    build_sentence()
    print()
    print()


