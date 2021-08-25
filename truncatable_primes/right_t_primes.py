# First digit must be single digit prime {2, 3, 5, 7}
# Other digits must be {1, 3, 7, 9}
#4260

digits = [1, 3, 7, 9]
digits2 = [1,2,3, 7, 9]
lista = [2,3,5,7]
R_T_Primes = [2,3,5,7]
L_T_Primes = [2,3,5,7]

def isPrime(n):
	if n==2 or n==3: return True
	if n%2 == 0 or n%3 == 0: return False
	
	for i in range(5, int(n**0.5)+1, 6):
		if n%i == 0 or n%(i+2) == 0: return False
	return True

# for x in R_T_Primes:
# 	for d in digits:
# 		if isPrime(x*10 + d):
# 			R_T_Primes.append(x*10 + d)

# print(R_T_Primes)

def nDigits(p):
	k=0
	while p>=1:
		p = p/10
		k+=1
	return k

# u = 0
# for x in L_T_Primes:
# 	for d in range(1,10):
# 		m = d*(10**nDigits(x)) + x;
# 		if isPrime(m):
# 			L_T_Primes.append(m)
file = open("log.txt", "w")
file.writelines(str(L_T_Primes))
file.close()
# print(L_T_Primes)