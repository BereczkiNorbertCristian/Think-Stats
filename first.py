import survey


def getPregnancyLengths(lst):
	return [el.prglength for el in lst]

def mean(lst):
	return float(sum(getPregnancyLengths(lst)))/len(lst) 

def GetFirstsOthers():
	table = survey.Pregnancies()
	table.ReadRecords()
	firsts,others = [],[]
	
	for preg in table.records:
		if preg.outcome!= 1:
			continue
		if preg.birthord == 1:
			firsts.append(preg)
		else:
			others.append(preg)
	
	return firsts,others

def main():

	table = survey.Pregnancies()
	table.ReadRecords()
	print 'Number of pregnancies', len(table.records)
	ans = 0
	for preg in table.records:
		if preg.outcome == 1:
			ans+=1
	print 'Number of live pregnancies', ans	

	firsts,others = GetFirstsOthers()
	
	print 'Firsts Len', len(firsts)
	print 'Others Len', len(others)

	print 'Firsts Mean', mean(firsts)
	print 'Others Mean', mean(others)

main()
