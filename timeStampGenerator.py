import time

def getTimeStamp():
	localtime = time.localtime()
	timeStampDate = str(localtime.tm_year) +'-'+ str(localtime.tm_mon) +'-'+ str(localtime.tm_mday)
	timeStampTime = str(localtime.tm_hour) +':'+ str(localtime.tm_min) +':'+ str(localtime.tm_sec)
	timeStamp = timeStampDate +'T'+ timeStampTime
	return timeStamp
