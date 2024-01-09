from urllib.request import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # print(word)
    print(word.decode())
    test = word.decode()
    print(test)
    WORDS.append(word.decode().strip()) # replace strip() with decode()
    
print(WORDS)
