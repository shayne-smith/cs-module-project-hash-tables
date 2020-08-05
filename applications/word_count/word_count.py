import string

def word_count(s):
    d = {}
    punctuation = '\":;,.-+=/\\|[]\{\}()*^&'

    # remove all punctuation from string
    no_punct = ""
    for char in s:
        if char not in punctuation:
            no_punct = no_punct + char

    # make all characters lowercase, split words by spaces, and put words into a list
    words = no_punct.lower().split()

    # count each word and add it to dictionary
    for w in words:
        if w not in d:
            d[w] = 0
        
        d[w] += 1

    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))