fp= open("harry_potter.txt")
fp2 = open ("harry_potter_2.txt", "w")
list =[]
fp.contents = fp.read()
punct = "/!£$%&()=?^*+§°ç><,;:.-_{}"
line = ""
for p in fp.contents:
    if p not in punct:
        line =line + p

line = line.split()

for x in line:
    if x not in list:
        list.append(x)
        fp2.write(str(x)+"\n")


print(line)

