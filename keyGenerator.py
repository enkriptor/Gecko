import random

def getKey():
	msg = ""
	state = True
	while(state):
		asciiNum = random.randint(65, 122)
		if(asciiNum!=92 and asciiNum!=96 and asciiNum!=91):
			msg += chr(asciiNum)
		if(len(msg) == 25): 
			state = False 
		else: 
			state = True
	return msg
