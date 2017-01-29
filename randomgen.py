import random
import socket
from time import sleep
from subprocess import call
import atexit

list1 = random.sample(range(1,11),10)
list2 = random.sample(range(1,11),10)
print list1
print list2
def closed():
    s.close()

atexit.register(closed)

TCP_IP = '10.10.10.45'
TCP_PORT = 6666
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
sleep(1)

s.send("STRT")

i=0
j=0
while i<9 or j<9:
	randno = random.randint(1,10)
	if randno%2==0:
		if i==9:
			continue
		s.send('EY'+str(list1[i]))
		call('play '+str(list1[i])+'.wav',shell=True)
		sleep(2)
		s.send('QEND')
		call('play 1.wav',shell=True)
		i +=1
	else:
		if j==9:
			continue
		s.send('EN'+str(list2[j]))
		call('play '+str(list1[j])+'.wav',shell=True)
                sleep(2)
                s.send('QEND')
                call('play 1.wav',shell=True)
                j +=1
s.end()
closed()
