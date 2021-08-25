import pickle

with open('out', 'rb') as fr:
	out = pickle.load(fr)

for d in out:
	if(d[1] == 0):
		print(d[0], end =" ")

