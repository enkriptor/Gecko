import time
import random

def getTimeStamp():
	localtime = time.localtime()
	timeStampDate = str(localtime.tm_year) +'-'+ str(localtime.tm_mon) +'-'+ str(localtime.tm_mday)
	timeStampTime = str(localtime.tm_hour) +':'+ str(localtime.tm_min) +':'+ str(localtime.tm_sec)
	timeStamp = timeStampDate +'T'+ timeStampTime
	return timeStamp

def getMessage():
	msg = ""
	state = True
	while(state):
		asciiNum = random.randint(57, 123)
		msg += chr(asciiNum)
		if(len(msg) == 37): 
			state = False 
		else: 
			state = True
	timeStamp = getTimeStamp()
	msg = msg + ' @ ' + timeStamp
	return msg