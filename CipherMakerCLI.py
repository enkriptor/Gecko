import getCipher as gc
import getKeyFunction as gkf
import os
import glob
import getCipherMessageBeta as gmb

def cipherMessage():
	message = input('Enter your message: ')
	if(len(message)<=300):
		finalCipher = gc.getCipher(message)
		gc.createFile(finalCipher, gkf.getKey())
	else:
		print("Enter message of length less than 300")

def decipherCipher(getFileName):
	fileCipher = gmb.getFile(getFileName)
	message = gmb.getMessageFromCipher(fileCipher)
	print(message)

print("Enter A to encrypt a message and B to decrypt an existing cipher!")
while(True):
	userInfo = input('Enter your choice: ')
	if(userInfo == 'A'):
		cipherMessage()
		break
	elif(userInfo == 'B'):
		getFileNameVector = glob.glob('*.enc')
		for getFileName in getFileNameVector:
			if(getFileName):
				decipherCipher(getFileName)
				break
			else:
				print('Cipher a message first!')
				break
		break
	else: 
		print('Enter correct option')

os.system('pause')