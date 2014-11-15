searchfile = open("wordlist.txt", "r")
array = []
for line in searchfile:
    if len(line) > 4 and len(line) < 8: 
    	array.append(line)
searchfile.close()

printfile = open("newwords.txt", "w")
for i in array:
	printfile.write(i)
printfile.close()