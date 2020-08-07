ref = {
    11.53: 'E',
    9.75: 'T',
    8.46: 'A',
    8.08: 'O',
    7.71: 'H', 
    6.73: 'N',
    6.29: 'R',
    5.84: 'I',
    5.56: 'S',
    4.74: 'D',
    3.92: 'L',
    3.08: 'W',
    2.59: 'U',
    2.48: 'G',
    2.42: 'F',
    2.19: 'B',
    2.18: 'M',
    2.02: 'Y',
    1.58: 'C',
    1.08: 'P',
    0.84: 'K',
    0.59: 'V',
    0.17: 'Q',
    0.07: 'J',
    0.07: 'X',
    0.03: 'Z'
}

frequency = {}
char_percent = {}
decoder = {}

punctuation = '\":;,.-+=/\\|[]\{\}()*^&!?'

def find_char_frequency(s):
    for key, char in enumerate(s):

        # check if character is a letter
        if not char.isalpha():
            continue
        
        # remove a-circumflex that slips through letter check
        if char is "â":
            continue

        # seed character in frequency dictionary
        if char not in frequency:
            frequency[char] = 0

        frequency[char] += 1
    

def calculate_char_percentage():
    num_chars = 0
    for letter in frequency:
        num_chars += frequency[letter]

    for letter in frequency:
        char_percent[letter] = round((frequency[letter] / num_chars) * 100, 2)


def build_decoder():
    for percent in sorted(char_percent.items()):
        if percent[1] in ref:
            decoder[percent[0]] = ref[percent[1]]
            del ref[percent[1]]


def decode(s):
    deciphered = ""
    for key, char in enumerate(s):

        if char in decoder:
            deciphered += decoder[char]
        else:
            deciphered += char
    
    print(deciphered)

        

# Read in all the words in one go
with open("ciphertext.txt") as f:
    s = f.read()
    print(s)

find_char_frequency(s)

calculate_char_percentage()

build_decoder()

decode(s)
