# Encrypter
An encryption daemon used to convert a message into a unique cipher which can be deciphered to the original message.

[![Generic badge](https://img.shields.io/badge/Release-v1.2.0-<COLOR>.svg)](https://shields.io/)

# Prerequisites
* Download and setup python from (www.python.org)
* Download or clone the repository to your system

# How to run the daemons?
## Encryption of text
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
* The daemon will prompt you to enter your choice of `A` and `B` to enter
* `A` is for encrypting a message
* Enter `A` and hit `Enter`
* The daemon will prompt you to enter your message
* Enter your message and hit `Enter`
* The cipher will be stored in a file with extension `.enc` with a `25` character file name
* You can now share this cipher with your friends

## Decryption of cipher
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
* The daemon will prompt you to enter your choice of `A` and `B` to enter
* `B` is for decrypting the existing cipher
* Enter `B` and hit `Enter`
* You will get your original message 


# What's new feature in v1.2.0?
* Matrix operation for handling the cipher and decipher workflows
* Message input length now extended but limited to `300` per use for ciphering and deciphering workflows
* Code cleaning methodologies in use. `Will produce better code for readability!`
* Created a common CLI daemon for encryption and decryption
* Cipher stored in a random generated named file with `.enc` extension