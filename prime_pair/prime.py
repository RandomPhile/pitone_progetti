n = 15
cifre = list(range(1,n+1))
file = open("log.txt", "w")

def isPrime(n):
	if n==2 or n==3: return True
	if n%2 == 0 or n%3 == 0: return False
	
	for i in range(5, int(n**0.5)+1, 6):
		if n%i == 0 or n%(i+2) == 0: return False
	return True

def recursion(alist, remaining):
	if len(remaining)==0:
		file.writelines(str(alist))
		file.writelines("\n")
		print(alist)
	for r in remaining:
		if isPrime(alist[-1]+r):
			alist_ = alist[:]
			alist_.append(r)
			remaining_ =remaining[:]
			remaining_.remove(r)
			recursion(alist_, remaining_)

for ii in cifre:
	print("\n","Solutions starting with", ii,":")
	digits = cifre[:]
	digits.remove(ii)
	recursion([ii], digits)

file.close()