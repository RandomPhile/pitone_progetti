f = open("homonyms.txt", "r")

fout = "["
for line in f:
	lout = "[\""
	spazio = 0
	for char in line:
		if char.isspace():
			if spazio == 0:
				lout = lout + "\", \""
				spazio = 1
		else:
			if '*' not in char:
				spazio = 0
				lout = lout + char
	fout = fout + lout[:-3] + "], "
fout = fout[:-2] + "]"
out = open("lista.txt", "w")
out.write(fout)

out.close()
f.close()