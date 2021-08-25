import numpy as np
possible_numbers = [1,2,3,4,5,6,7,8,9]


def solve(somma, cifre):
	for i in [x for x in possible_numbers if x<(somma/cifre)]:
		
		for j in possible_numbers:
			if i!=j:
				if cifre>2:
					for k in possible_numbers:
						if k!=i and k!=j:
							if i+j+k==somma:
								print(i,'+',j,'+',k,'=',somma)	

				else:
					if i+j==somma:
						print(i,'+',j,'=',somma)	

solve(7,3)
solve(5,2)



#https://app.crackingthecryptic.com/sudoku/6D4r2QfF7N











































#somma = 5
# cifre = 2

# def solve(c,s,p,sol):
# 	if len(sol)==cifre-1:
# 		if s in p:
# 			sol.append(s)
# 			print(sol)
# 			sol = []
# 	else:
# 		solve()

# solve(cifre,somma,possible_numbers,[])


# somma = 5
# cifre = 2

# def solve(s,c,p,sol):
# 	if c==1:
# 		if s in p:
# 			sol.append(s)
# 			print(sol)
# 			#sol = []
# 		#print(s,c,p)
# 	else:
# 		for n in p:
# 			p_ = [x for x in p if x != n]
			
# 			s_ = s-n

# 			sol.append(n)
# 			if s_ >= min(p_):
# 				solve(s_,c-1,p_,sol)

# solve(somma, cifre, possible_numbers,[])
