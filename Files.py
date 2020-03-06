# find a book and replace characters - text format

fp=open("harry_potter.txt")
fp2 = open("result.txt", "w")

## read the file line by line

for each_line in fp:
    fp2.write(each_line[:-1]+" Bob\n")
                             # \n means add the enter

fp.close()
fp2.close()
