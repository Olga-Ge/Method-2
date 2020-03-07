fp= open("harry_potter.txt")
list =[]
punct = "/!£$%&()=?^*+§°ç><,;:.-_{}"
for line in fp:
    for p in punct:
        line =line.replace(p," ")
        
