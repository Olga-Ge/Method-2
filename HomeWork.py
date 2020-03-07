fp= open("harry_potter.txt")
fp2 = open ("harry_potter_2.txt", "w")
list =[]
fp.contents = fp.read()
punct = "/!£$%&()=?^*+§°ç><,;:.-_{}"
line = fp.contents.split()
for line in fp:
    for p in punct:
        line =line.replace(p," ")
        fp.write(line)
for x in line:
    if x not in list:
        list.append(x)
        fp2.write(str(x)+"\n")
