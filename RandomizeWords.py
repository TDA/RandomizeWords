from random import shuffle
__author__ = 'saipc'

def RandomizeWords(string):
    newStringList = []
    for word in string.split():
        # print word
        newStringList.append(word)
    shuffle(newStringList)
    # print(newStringList)
    shuffledWordList = [[letter for letter in word] for word in newStringList]
    newString = ""
    newString = " ".join(newStringList)
    print newString
    print shuffledWordList


RandomizeWords("hello, im sai and my name is also sai and this dummy text is also sai")
RandomizeWords("Hello this is a random string for a push")


x = [0] * 26
linearr = []

pos = ord('a') - 97
value = linearr[1]

x.insert(pos, 1)
print x
