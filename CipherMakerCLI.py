import getCipher as gc
import keyGenerator as kg
import os
import glob
import getMessage as gm
import fileManager as fm

def cipherMessage():
	message = input('Enter your message: ')
	if(len(message)<=300):
		finalCipher = gc.getCipher(message)
		fm.createFile(finalCipher, kg.getKey())
	else:
		print("Enter message of length less than 300")

def decipherCipher(getFileName):
	fileCipher = fm.getFile(getFileName)
	message = gm.getMessageFromCipher(fileCipher)
	print(message)

print("Enter \'A\' to encrypt a message and \'B\' to decrypt an existing cipher!")
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
			else:
				print('Cipher a message first!')
				break
		break
	else: 
		print('Enter correct option')

os.system('pause')