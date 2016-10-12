import msvcrt
import time
 
f1=5
f2=10
f3=5
count=0
count1=0
print "Press key 'd' to move right and key 's' to move downwards"
print " Press enter key to get started!"

raw_input()
s_time=time.time()

while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print "-->" ,
		if count==f1:
			print "Turn down."
			break
	else:
		print "You lost the game!"
		exit(1)
while(1):
	key1=msvcrt.getch()
	if key1=='s':
		count=count+1
		print "                  "
		print "                 |"
		print "                 v"
		if count==f2:
			print "                 Turn right." ,
			break
	else:
		print "You lost the game!"
		exit(1)     
while(1):
	key2=msvcrt.getch()
	if key2=='d':
		count1+=1
		print "-->" ,
		if count1==f3:
			break
	else:
		print "You lost the game!"
		exit(1)

time_elapsed=time.time()-s_time
print "Congrats you have finished the game!"
print "Time taken is "+str(time_elapsed)


'''
1. Mention controls for the game.	
'''
