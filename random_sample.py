
import Pmf
import Cdf
import myplot
import random
import numpy as np
import matplotlib.pyplot as plt

def doCDF(sampl):
		
	#pmf = Pmf.MakePmfFromList(sampl,'random_pdf')
	cdf = Cdf.MakeCdfFromList(sampl,'random_cdf')
	
	#myplot.Pmf(pmf)
	myplot.Cdf(cdf)
	myplot.Show()


def main():

	sampl = [0]*1000
	for i in range(0,1000):
		sampl[i] = random.random()

	doCDF(sampl)
	
	


main()



