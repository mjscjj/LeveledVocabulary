f = open("./capital.txt", "r")



def changge(content, spl):
    arr = []
    for a in content.split(spl):
        if a.__len__() > 2:
            a = a[0].upper() + a[1:]
        arr.append(a)
    return spl.join(arr)


content = f.read().lower()

content = changge(content, ". ")
content = changge(content, ".\n")
content = changge(content, "? ")
content = changge(content, "?\n")

# chose
content = changge(content, "\n")

# chose
content = content.replace("chinese", "Chinese")

f = open("./lowecase.txt", "w")

f.write(content)


