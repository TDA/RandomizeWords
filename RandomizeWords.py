from random import shuffle
__author__ = 'saipc'

def RandomizeWords(string):
    newStringList = []
    for word in string.split(" "):
        # print word
        newStringList.append(word)
    shuffle(newStringList)
    # print(newStringList)
    newString = ""
    newString = " ".join(newStringList)
    print newString


RandomizeWords("hello im sai and my name is also sai and this dummy text is also sai")