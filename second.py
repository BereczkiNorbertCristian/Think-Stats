
import first
import math
import thinkstats

def ExtractPregLength(pregnancies):

	n = len(pregnancies)
	ret = [0] * n
	for i in range(0,n):
		ret[i] = pregnancies[i].prglength
	return ret

def SecondMain():

	firsts,others = first.GetFirstsOthers()

	firsts,others = ExtractPregLength(firsts),ExtractPregLength(others)

	varF,varO = thinkstats.Var(firsts),thinkstats.Var(others)

	stdF,stdO = math.sqrt(varF),math.sqrt(varO)

	print 'Firsts std:',stdF
	print 'Others std:',stdO


SecondMain()

