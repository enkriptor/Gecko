# Encrypter
An encryption daemon used to convert a message into a unique cipher using a generated unique key and which can be deciphered to the original message using the key existing on the system.

[![Generic badge](https://img.shields.io/badge/Release-v1.3.2-<COLOR>.svg)](https://shields.io/)

# Prerequisites
* Download and setup python from (www.python.org)
* Download or clone the repository to your system

# What's new feature in v1.3.2?
* Unique key feature added
* Receiver's key can be added for the receiver to decipher the cipher.

# How to run the daemons?
## Encryption of text
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
* The daemon will generate a unique key if not already present on the system otherwise will read the existing key.
* The daemon will prompt for the receiver's unique key, if left blank and `Enter` receiver's key will be the existing unique key from the system.
* The daemon will prompt you to enter your choice of `Enc` and `Dec` to enter
* `Enc` is for encrypting a message
* Enter `Enc` and hit `Enter`
* The daemon will prompt you to enter your message
* Enter your message and hit `Enter`
* The cipher will be stored in a file with extension `.enc` with a `25` character file name
* The original message will be stored in `messageCopy.txt`
* You can now share this cipher with your friends

## Decryption of cipher
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
* The daemon will generate a unique key if not already present on the system otherwise will read the existing key.
* The daemon will prompt for the receiver's unique key, if left blank and `Enter` receiver's key will be the existing unique key from the system.
* The daemon will prompt you to enter your choice of `Enc` and `Dec` enter
* `Dec` is for decrypting the existing cipher
* Enter `Dec` and hit `Enter`
* You will get your original message 