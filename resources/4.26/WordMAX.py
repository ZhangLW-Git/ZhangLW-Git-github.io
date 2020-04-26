text = open("abc.txt").readlines()

lineall = ""
for line in text:
    lineall += line    #输出信息

lettertable = []
for i in range(65,91):
    lettertable.append(chr(i))
    j = i-65+97
    lettertable.append(chr(j))
lettertable.append(["'", "-"])     #字母表

words = []
word = ""
for letter in lineall:
    if letter in lettertable:
        word += letter
    else :
        if word != "":
            words.append(word)
        word = ""                  #存储单词

k = 0
for i in words:
    for j in words:
        if words.count(i) >= words.count(j):
            k += 1
        if k == len(words):
            print(i, words.count(i))             #记数