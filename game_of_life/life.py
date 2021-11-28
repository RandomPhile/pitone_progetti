import numpy as np
import os
from patterns import *

sizer = 30#MAX 58
sizec = 80#MAX 119
def aggiungi(M_figura,riga,colonna):
	M[riga:riga+M_figura.shape[0], colonna:colonna+M_figura.shape[1]] += M_figura

M = np.zeros((sizer,sizec))

aggiungi(M_glider,5,5)

def stampa():
	for r in range(sizer):
		for c in range(sizec):
			if M[r][c]==0:
				print('  ', end="", flush=True)
			else:
				print('■ ', end="", flush=True)
		print('\n', end="", flush=True)
	print('\n', end="", flush=True)

def stato(r,c,somma):
	if M[r][c]==0:
		if somma==3:
			M[r][c] = 1
	else:
		if somma != 2 and somma != 3:
			M[r][c] = 0

def update():
	M2 = np.copy(M)
	for r in range(sizer):
		for c in range(sizec):
			#angoli
			if r==0 and c==0:
				somma = M2[r][c+1] + M2[r+1][c+1] + M2[r+1][c]
				stato(r,c,somma)
			if r==0 and c==sizec-1:
				somma = M2[r][c-1] + M2[r+1][c-1] + M2[r+1][c]
				stato(r,c,somma)
			if r==sizer-1 and c==0:
				somma = M2[r][c+1] + M2[r-1][c+1] + M2[r-1][c]
				stato(r,c,somma)
			if r==sizer-1 and c==sizec-1:
				somma = M2[r][c-1] + M2[r-1][c-1] + M2[r-1][c]
				stato(r,c,somma)

			#spigoli
			if r==0 and c!=0 and c!=sizec-1:
				somma = M2[r][c-1] + M2[r][c+1] + M2[r+1][c-1] + M2[r+1][c] + M2[r+1][c+1]
				stato(r,c,somma)
			if r==sizer-1 and c!=0 and c!=sizec-1:
				somma = M2[r][c-1] + M2[r][c+1] + M2[r-1][c-1] + M2[r-1][c] + M2[r-1][c+1]
				stato(r,c,somma)
			if c==0 and r!=0 and r!=sizer-1:
				somma = M2[r-1][c] + M2[r+1][c] + M2[r-1][c+1] + M2[r][c+1] + M2[r+1][c+1]
				stato(r,c,somma)
			if c==sizec-1 and r!=0 and r!=sizer-1:
				somma = M2[r-1][c] + M2[r+1][c] + M2[r-1][c-1] + M2[r][c-1] + M2[r+1][c-1]
				stato(r,c,somma)

			#altro
			if r!=0 and r!=sizer-1 and c!=0 and c!=sizec-1:
				somma = M2[r-1][c-1] + M2[r-1][c] + M2[r-1][c+1] + M2[r][c-1] + M2[r][c+1] + M2[r+1][c-1] + M2[r+1][c] + M2[r+1][c+1]
				stato(r,c,somma)

go = ""
while go == "":
	os.system('cls' if os.name == 'nt' else 'clear')
	stampa()
	update()
	go = input()
	#print(M)
