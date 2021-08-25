import numpy

res12 = [[5,1],[4,4],[1,8],[3,3],[7,2],[6,5],[2,6],[8,7]]
res = [5,16,8,9,14,30,12,56]
FIN = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

names = ['GARNBRET','NOGUCHI ','MIROSLAW','NONAKA  ','RABOTOU ','PILZ    ','JAUBERT ','SEO     ']

for G in range(8):
	for N in range(8):
		if N==G:
			continue
		for M in range(8):
			if M==N or M==G:
				continue
			for K in range(8):
				if K==M or K==N or K==G:
					continue
				for R in range(8):
					if R==K or R==M or R==N or R==G:
						continue
					for P in range(8):
						if P==R or P==K or P==M or P==N or P==G:
							continue
						for J in range(8):
							if J==P or J==R or J==K or J==M or J==N or J==G:
								continue
							for S in range(8):
								if S==J or S==P or S==R or S==K or S==M or S==N or S==G:
									continue

								results = numpy.array([5*(G+1),16*(N+1),8*(M+1),9*(K+1),14*(R+1),30*(P+1),12*(J+1),56*(S+1)])
								sort_index = numpy.argsort(results)
								#print(sort_index)
								for j in range(8):
									for i in range(8):
										if sort_index[i]==j:
											FIN[i][j] += 1
print('\n')
print('\n')
somma = numpy.sum(numpy.array(FIN[0]))
fin = numpy.array(FIN)
for i in range(8):
	print(names[i], numpy.multiply(FIN[i],100)//somma)
										
print('\n')
print('\n')

					
					
					
