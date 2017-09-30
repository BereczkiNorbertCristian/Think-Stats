import survey
table = survey.Pregnancies()
table.ReadRecords()
for i in range(0,100):
	print table.records[0].outcome
print 'Number of pregnancies', len(table.records)
