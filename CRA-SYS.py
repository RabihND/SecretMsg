import secrets
from random import randint
import os
import time
import sys
import getpass
#Copyright (c) 2017 Rabih ND, Lebanon

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
secretsGenerator = secrets.SystemRandom()

print('                          >>>]] RABIH-SYS [[<<<    ')
def generate_otp(sheets, length):
	for sheet in range(sheets):
		with open("otp" + str(sheet) + ".txt","w") as f:
			for i in range(length):
				f.write(str(secretsGenerator.randint(0,26))+"\n")

def load_sheet(filename):
	with open(filename, "r") as f:
		contents = f.read().splitlines()
	return contents

def get_plaintext():
	plaintext = input('Please type your message :   ')
	return plaintext.lower()

def load_file(filename):
	with open(filename, "r") as f:
		contents = f.read()
	return contents

def save_file(filename, data):
	with open(filename, 'w') as f:
		f.write(data)

def encrypt(plaintext, sheet):
	ciphertext = ''
	for position, character in enumerate(plaintext):
		if character not in ALPHABET:
			ciphertext += character
		else:
			encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
			ciphertext += ALPHABET[encrypted]
	return ciphertext

def decrypt(ciphertext, sheet):
	plaintext = ''
	for position, character in enumerate(ciphertext):
		if character not in ALPHABET:
			plaintext += character
		else:
			decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
			plaintext += ALPHABET[decrypted]
	return plaintext
def dangerfile(filename):
        
        return filename


def menu():
        password = '123456'
        inp = str ( getpass.getpass('Enter the password: ') )
        if inp == password:
                print ('welcome to the program\n'+'>>')
        else:
                print ('Wrong Password...\n')
                print ('Please try again later...')
                time.sleep(3)
                exit()
                        
        choices = ['1', '2', '3', '4' , '5']
        choice = '0'
        while choice not in choices:
                print('What would you like to do?')
                print('1. Generate OTP')
                print('2. Encrypt a message')
                print('3. Decrypt a message')
                print('4. Quit the program')
                print('5. Delete all OTP files')
                choice = input('Please type 1, 2, 3,4 or 5 and press Enter >> ')
                if choice == '1':
                        sheets = int(input('How many one-time pads would you like to generate? '))
                        length = int(input('What will be your maximum message length? '))
                        print('\n'+'>>')
                        generate_otp(sheets, length)
                elif choice == '2':
                        filename = input('Type in the filename of the OTP you want to use (otp__.txt):  ')
                        dangerfile(filename)
                        sheet = load_sheet(filename)
                        plaintext = get_plaintext()
                        ciphertext = encrypt(plaintext, sheet)
                        filename = input('What will be the name of the encrypted file? (enc__.txt):     ')
                        print('\n'+'>>')
                        save_file(filename, ciphertext)
                elif choice == '3':
                        filename = input('Type in the filename of the OTP you want to use (otp__.txt):  ')
                        sheet = load_sheet(filename)	
                        filename = input('Type in the name of the file to be decrypted (enc__.txt):     ')
                        ciphertext = load_file(filename)
                        plaintext = decrypt(ciphertext, sheet)
                        print('The message reads:')
                        print('__________________________')
                        print(plaintext)
                        print('__________________________\n'+'>>')
                elif choice == '4':
                        os.remove(dangerfile(filename))
                        print('>>THE SYSTEME IS SECURED....')
                        time.sleep(2.5)
                        exit()
                elif choice == '5':
                        inp = str ( getpass.getpass('Please enter the password: ') )
                        if inp == password:
                                for sheet in range(1000):
                                        try:
                                                os.remove("otp" + str(sheet) + ".txt")
                                        except:
                                                print('>>THE SYSTEME IS SECURED....')
                                                time.sleep(2.5)
                                                exit()
                        else:
                                print('Please try again later...')
                                print('>>THE SYSTEME IS  NOT TOTALY SECURED....')
                                time.sleep(2.5)
                                exit()
                                
                choice = '0'


menu()
