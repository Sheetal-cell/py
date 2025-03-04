# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

import string
import random

def encode(normal_lang):
    '''Converts your code to secret code'''
    if (len(normal_lang)<3):
        print(normal_lang[::-1])
    elif (len(normal_lang)>=3):
        letter = normal_lang[1:]+normal_lang[0]
        word_end = "".join(random.choices(string.ascii_lowercase, k=3))
        word_begin = "".join(random.choices(string.ascii_lowercase, k=3))
        secret_code = word_begin + letter + word_end
        print(f"Your secret code is: {secret_code}")
    
def decode(normal_lang):
    '''Converts your secret code to code'''
    if (len(normal_lang)<3):
        print(normal_lang[::-1])
    elif (len(normal_lang)>=3):
        word = normal_lang[3:-3]
        letter = word[-1]+word[:-1]
        print(f"Your code is {letter}")

print("Hey! Do you want to encode or decode?")
choice = int(input("1 for encode and 2 for decode: "))

match choice:
    case 1:
        normal_lang = input("Enter you word to convert: ")
        encode(normal_lang)
    case 2:
        normal_lang = input("Enter you word to convert: ")
        decode(normal_lang)