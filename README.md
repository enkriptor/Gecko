# Encrypter
An encryption daemon used to convert a message into a unique cipher which can be deciphered to the original message.

[![Generic badge](https://img.shields.io/badge/Release-v1.2.2-<COLOR>.svg)](https://shields.io/)

# Prerequisites
* Download and setup python from (www.python.org)
* Download or clone the repository to your system

# What's new feature in v1.2.2?
* Created a common CLI daemon for encryption and decryption
* Cipher stored in a random generated named file with `.enc` extension
* Multiple ciphers can be decrypted
* Message copy available as messageCopy.txt

# How to run the daemons?
## Encryption of text
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
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
* The daemon will prompt you to enter your choice of `Enc` and `Dec` enter
* `Dec` is for decrypting the existing cipher
* Enter `Dec` and hit `Enter`
* You will get your original message 