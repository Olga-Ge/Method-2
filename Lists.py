# find a book in txt (2-3)
# count different words in the books
# remove the punctuation (only count words) - define the list of punctuation and remove them

fp = open("harry_potter.txt", "r")
fp2 = open("results2.txt", "w")
punct = ("-","?", "!", ":", ";", ",", '.','"', "'")

for line in fp:
    for p in punct:
        line =line.replace(p," ")
for line in fp:
    fp2.write(line)
fp.close()
fp2.close()
