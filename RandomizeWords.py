from random import shuffle
__author__ = 'saipc'

def RandomizeWords(string):
    newStringList = []
    for word in string.split(" "):
        # print word
        newStringList.append(word)
    shuffle(newStringList)
    # print(newStringList)
    # shuffledWordList =["".join(shuffle[word]) for word in newStringList]

    newString = ""
    newString = " ".join(newStringList)
    print newString
    # print shuffledWordList


RandomizeWords("hello im sai and my name is also sai and this dummy text is also sai")
RandomizeWords("Hello this is a random string for a push")
