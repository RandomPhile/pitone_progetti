import numpy as np
d = 10

for num in range(10**(d-1),10**d):
	res = [int(x) for x in str(num)]
	go=True
	for i in range(0,d):
		if go==False:
			break
		else:
			if res.count(i)!=res[i]:
				go=False
	if go==True:
		print(res)
