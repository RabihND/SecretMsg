# Introduction
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
## What you will make

In this resource you will learn how to create and use an encryption technique known as the one-time pad. This method of encryption will allow you to send secret messages to your friends and, as long as you’re careful, the messages will be **unbreakable**.

## What you will learn

By writing the secret agent chat program, you will learn:

- How random numbers can be used to encrypt messages
- How iteration can be used to encrypt individual characters
- Why techniques such as the Caesar cipher are insecure
- Why it’s important to keep your keys a secret

## What you will need
- A computer with Python 3 installed

# Secret agent chat
![Image of OTP](https://ece.uwaterloo.ca/~ece150/Projects/C.1/img/otp.1.png)

__Cryptography__ may be a way of disguising the contents of your message, to form it harder for your enemies to read. one amongst the primary sorts of cryptography was utilized by the Roman Emperor general, and is now called the Caesar Cipher.

During World War II the German military thought they'd developed an ideal method of encrypting messages, using something called an Enigma machine.

The German military was wrong though. because of some clever Polish mathematicians and a British mathematician called Alan Turing, the Enigma messages were decrypted, and this helped the Allies win the war.

A **one-time pad (OTP)** may be a different method of encryption. 
Imagine *Alice* wants to send a secret message to *Bob*, without *Eve* knowing what the message says. Alice first picks a key, which will be a number such as 3. Alice then tells Bob the key.

When using an OTP, a string of random numbers is generated and shared between Alice and Bob. Each letter of the message is then shifted by the corresponding number within the OTP, so each letter has its own individual key! As long as Eve doesn’t have the OTP, the message is **impossible** to decrypt.

# Note à bien

While a one-time pad offers perfect secrecy, you still have to be careful if you want to remain really secure, and there are some issues with this program.

- To send encrypted messages to each other, you can use email, SMS or even social media such as Facebook or Twitter. It won’t even matter if your posts are public, as the only person who could decrypt the message is your friend.
- Once you’ve generated your OTP, such as by generating 100 sheets, you need to transfer them to the person you want to communicate with. You can’t send them electronically, such as by email, as this is **insecure**.
>Probably the most secure method is giving them to your friend on a storage device, such as an SD card or USB flash memory.
- **The OTP method is only secure if you and your friend keep the OTP secure**.
- You and your friend need to be sure which OTP you’re using. The best way of doing this is by starting with otp0.txt and then deleting it when you’ve encrypted or decrypted a message. You can then progress to using otp1.txt.
- The OTP relies on the randomness of the random number generator. If the generator isn’t truly random, then the OTP could be cracked. Python’s random module is probably not the best way of generating random numbers.
- Your message can’t be longer than the length of the sheet from the OTP. If you’re not sure how long your messages will be, it’s better to generate large sheets just in case.

# What next?

- Can you alter the program so that capital letters are preserved?
- Can you alter the program so that punctuation is also encrypted?

# Using the Program
The Program is very easy to use; I write the options as a list that you can understand each one of them.

![ScreenShoot](/Data/OTP.jpg)
> The default password = '123456' (You can change it from the source code)


