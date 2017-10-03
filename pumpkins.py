
from thinkstats import *

def Pumpkin():
	pumpkins = [1]*3 + [3]*2 + [591]

	mu,var = MeanVar(pumpkins)

	print 'Mean',mu
	print 'Var',var

Pumpkin()

