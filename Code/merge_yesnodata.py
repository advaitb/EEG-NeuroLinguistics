inp = open('inputvalyn_landec.txt', 'w')
Arr=[]
with open('inputval_landec.txt') as f:
	lines=f.readlines()
	length=len(lines)
	for i in range(length/2):
		yline=lines[i]
		nline=lines[(length/2)+i]
		inp.write("%s" % yline)
		inp.write("%s" % nline)
inp.close()
