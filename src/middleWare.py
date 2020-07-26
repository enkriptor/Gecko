import getCipher as gc
import getMessage as gm
import workflowUtils as wu
import os, glob 

def cipherMessage(securityKey, receiversKey):
	message = input('Enter your message: ')
	open('messageCopy.txt', 'w').write(message)
	encrKey = gc.getCipher()
	os.system('del public.key')
	securityKeyWithEncr = wu.getPrintables(wu.embedKeyIntoMessage(int(encrKey), wu.getBitMessageDirect(receiversKey)))
	open('public.key','wb').write(securityKeyWithEncr.encode('utf-8'))

def decipherCipher(yPhase):
	fileCipher = open("finalMessage.txt", 'rb').read().decode('utf-8')
	message = gm.getMessageFromCipher(fileCipher, yPhase)
	print(message)

def checkForKey():
	newkeyStatus = False
	getKeyVector = glob.glob('*.key')
	if("private.key" in getKeyVector):
		print('Reading existing unique key!')
		with open("private.key",'r') as keyFile:
			securityKey = keyFile.read()
	else:
		print('Generating new key!')
		securityKey = wu.getAddressKey(47)
		with open('private.key', 'w') as keyFile:
			keyFile.write(securityKey)
			newkeyStatus = True
	return securityKey, newkeyStatus

def manageKey():
	useCLI = False
	securityKey, newkeyStatus = checkForKey()
	while(True):
		if(newkeyStatus):
			print("Private key generated")
		choice = input("Do you want to continue? Enter y to continue or n to exit: ")
		if(choice == "y"):
			print("Enter the key of the recipient or leave it blank if you're the recipient!")
			receiversKey = input("Enter receiver's unique key: ")
			if(receiversKey == ""):
				print("Assigning key to self!")
				receiversKey = securityKey
			print("Enter \'Enc\' to encrypt a message and \'Dec\' to decrypt an existing cipher!")
			useCLI = True
			break
		elif(choice == "n"):
			print("Aborting the application!")
			os.system('pause')
			break
		else: 
			print("Please enter right choice!")
	return securityKey, receiversKey, useCLI