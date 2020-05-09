import getCipher as gc
import keyGenerator as kg
import os
import glob
import getMessage as gm
import fileManager as fm

def cipherMessage():
	message = input('Enter your message: ')
	fm.createFile(message, 'messageCopy', '.txt', 'w')
	if(len(message)<=300):
		fm.createFile(gc.getCipher(), kg.getKey(), '.enc', 'w')
	else:
		print("Enter message of length less than 300")

def decipherCipher(getFileName):
	fileCipher = fm.getFile(getFileName, 'r')
	message = gm.getMessageFromCipher(fileCipher)
	print(message)

print("Enter \'Enc\' to encrypt a message and \'Dec\' to decrypt an existing cipher!")
while(True):
	userInfo = input('Enter your choice: ')
	if(userInfo == 'Enc'):
		cipherMessage()
		break
	elif(userInfo == 'Dec'):
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