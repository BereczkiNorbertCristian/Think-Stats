
import operator
import myfirst
import math
import thinkstats
import Pmf
import descriptive

from copy import deepcopy

def ExtractPregLength(pregnancies):

	n = len(pregnancies)
	ret = [0] * n
	for i in range(0,n):
		ret[i] = pregnancies[i].prglength
	return ret

def SecondMain1and2():

	firsts,others = myfirst.GetFirstsOthers()
	firsts,others = ExtractPregLength(firsts),ExtractPregLength(others)
	varF,varO = thinkstats.Var(firsts),thinkstats.Var(others)
	stdF,stdO = math.sqrt(varF),math.sqrt(varO)

	print 'Firsts std:',stdF
	print 'Others std:',stdO

def MostFrequent(hist):

	maxVal,maxFreq = 0,0
	for val in hist.Values():
		if maxFreq < hist.Freq(val):
			maxFreq = hist.Freq(val)
			maxVal = val
	return maxVal

def compTuple(a,b):
	if a[1] > b[1]:
		return 1
	return -1

def AllMode(hist):

	items = deepcopy(hist.Items())
	return sorted(items,key = operator.itemgetter(1),reverse = True)

def SecondMain3():

	hist = Pmf.MakeHistFromList([1,2,2,3,5])
	
	print 'Most Freq Value' , MostFrequent(hist)
	print 'All Mode', AllMode(hist)

def PmfMean(hist):

	mu = 0
	for val in hist.Values():
		mu+=val*hist.Prob(val)
	return mu	

def PmfVar(hist):

	mu = PmfMean(hist)
	var = 0
	for val in hist.Values():
		var+=hist.Prob(val)*((val - mu)**2)
	return var

def SecondMain5():

	hist = Pmf.MakePmfFromList([1,2,2,3,5])
	
	assert hist.Total() 	== 1
	assert hist.Mean() 	== PmfMean(hist)
	assert hist.Var() 	== PmfVar(hist)
	print 'HistMean:',hist.Mean()
	print 'PmfMean:',PmfMean(hist)
	print 'HistVar:',hist.Var()
	print 'PmfVar:',PmfVar(hist)

def probRange(pmf,low,high):

	ans = 0.0
	for tm in range(low,high+1):
		ans += pmf.Prob(tm)
	return ans


SecondMain1and2()
SecondMain3()
SecondMain5()
