import os, sys

f = open("./wordList.txt", "r")

# f = open("./tex.txt", "r")


import  re
arr = set()
oris = []
count = 0
for line in f.readlines():
    line = ''.join(re.findall(r'[A-Za-z]', line))
    print(line.encode("utf-8"))
    orin = line
    orin = orin.replace("\n", "")
    line = line.lower().replace("\t", "")
    line = line.replace("*", "")
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    line = line.replace("\r\n", "")
    print(line)

    if arr.__contains__(line):
        orin += "=== 删除  ===="
        count += 1
        # print("删除 " + orin)
    arr.add(line)

    orin += "\n"
    print(orin)
    oris.append(orin)

f = open("./res.txt", "w")

for line in oris:
    f.write(line)

f.write("一共{}个词， 重复{} 个词".format(oris.__len__(), count))


