#Authors: Keshav Patil and Advait Balaji(@advaitb)
import pyeeg
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat("/home/advaitb/Documents/LRI-Shubham-Hindi-Feb1_20170201_121230_fil_seg.mat")

var = sio.whosmat("/home/advaitb/Documents/LRI-Shubham-Hindi-Feb1_20170201_121230_fil_seg.mat")

x=[i for i in range(2250)]
y=[np.zeros(9) for i in range(2250)]	
def Window(d,n):
	relev=[11,13,15,5,7,1,27,2,3,17,4]	
	tpower=[[0,0,0,0,0] for i in relev]
	avpower=[[0,0,0,0,0] for i in relev]
	print 'window size: ',n
	curry=[]	
	for i in range(0,len(d[0])-n):
		window=d.T[i:i+n].T
		cpower=Power(window)
		curry.append(cpower[0][2])				
		for j in range(0,len(tpower[0])):
			for ind in range(len(relev)):
				tpower[ind][j]+=cpower[ind][j]
	print 'total number of windows: ',i
	for j in range(0,len(tpower[0])):
		for ind in range(len(relev)):
			avpower[ind][j]=tpower[ind][j]/i		

	return avpower,curry
		
def Power(d):
	Band=[0.5,4,8,13,30,40]
	relev=[11,13,15,5,7,1,27,2,3,17,4]
	power=[np.zeros(len(Band) -1) for i in relev]
	count=0
	for ind in range(len(power)):
		da=d[relev[ind]]
		C=np.fft.fft(da)
		C=abs(C)
		for FI in range(0,len(Band) -1):
			F=float(Band[FI])
			NF=float(Band[FI+1])
			power[ind][FI]=sum(C[int(np.floor(F/250*len(da))):int(np.floor(NF/250*len(da)))])
			Power_Ratio = power[ind] / sum(power[ind])
	return power			

#x = [i for i in range(1,19)]
#y=[]
yes=[18,19,21,26,28,29,30,31]
for que in range(len(yes)):
	d =data[var[yes[que]][0]]
	print var[yes[que]][0]
	cwin,cy = Window(d,250)
	for i in range(2250):
		y[i][que]=cy[i]
	print cwin
	#y.append(cwin[0][2:])


plt.plot(x,y)	
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()	

	





