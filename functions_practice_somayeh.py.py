# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 14:32:45 2025

@author: somayeh doosti"""


#sum-of-two-user-inputs

def sumation():
    num1=int(input("please enter number 1:"))
    num2=int(input("Plese enter number 2:"))
    x= num1+num2
    return x
print(sumation())


#recursive-factorial-function

def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return(x*factorial(x-1))
num=int(input("Please enter a number: "))
print(factorial(num))

#degree-to-radian-converter

import math

def degree_to_radian():
    degree1=int(input("please enter your degree: "))
    teta1=degree1*(math.pi/180)
    return teta1
print(degree_to_radian())

#even-or-odd-checker

def even_odd_checker(x):
    if x%2==0:
        return "even"
    else:
        return"odd"
num=int(input("please enter a number :"))
print(even_odd_checker(num))

#fibonanchi_domain

def fibonanchi(x):
    if x <=1:
        return x
    else:
        return fibonanchi(x-1)+fibonanchi(x-2)
num=int(input("please enter fibonanchi step: "))
print(fibonanchi(num))
    
#means

def mean(x):
    sums = 0
    for i in x:
        sums += i
    return sums / len(x)
numbers = input("Enter a list of numbers separated by space: ")
num_list = [int(n) for n in numbers.split()]
print("Mean is:", mean(num_list))

#lenth of a string

def matn(x):
     return len(x)
sentenses=input("enter a sentenses :")
print("lenth of sentenses is" , matn(sentenses))


#check of  prime number 

import math
def check_of_prime(x):
    if x<=1:
        return "the number is not prime"
    else:
        for i in range(2,(int(math.sqrt(x)+1))):
            if x%i==0:
                return "the number is not prime"
    return "the number is prime"
num=int(input("enter a number :"))
print(check_of_prime(num))

# Check if a given number exists in a list

def existing_parameter(lists , item):
    if item in lists:
        return "the item exsists in list"
    return"the item is not in list"
list1=input("enter a list of number :")
list1 = [int(x) for x in list1.split()]
items=int(input("please enter a number that you want chck exsisting in list :"))
print(existing_parameter(list1, items))

#reverse string

def reverses(x):
     return x[::-1]
matn=input("enter a string :")
print(reverses(matn))

#upper case of string

def uppercase(x):
     return x.upper()
matn=input("enter a string :")
print(uppercase(matn))


#Check if a word exists in a sentence
 
def check_word_in_text(text, word):
    if word in text:
        return f'"{word}" exists in the text.'
    else:
        return f'"{word}" does not exist in the text.'
text_input = input("Please enter a text: ")
word_input = input("Please enter a word to check: ")
print(check_word_in_text(text_input, word_input))

#Concatenate two strings

def match(x,y):
    return x + " " + y
sentenses1=input("please enter a sentences1:")
sentenses2=input("please enter a sentences2:")
print(match(sentenses1,sentenses2))

#Count number of words in a sentence

def counting_word(x):
    x=len(x.split())
    return x 
sentences=input("please enter your sentence:")
print(counting_word(sentences))    

#Replace one character with another in a string

def replace_char(text,char1,char2):
    text=text.replace(char1,char2)
    return text
text1=input("please enter a sentence :")
char_1=input("please enter character that you want replace:")
char_2=input("please enter new character :")
print(replace_char(text1,char_1,char_2))

#Return first and last character of a string

def function1(x):
    c=x[0]
    y=x[-1]
    return c , y
sentence=input("please enter a text :")
print(function1(sentence))

#Check if two strings are equal

def function2(x,y):
    if x==y:
        return"this two strings are equal."
    else:
        return "this two strings are not equal."
string1=input("please enter text1:")  
string2=input("please enter text2:")  
print(function2(string1, string2))

#Reverse word order in a sentence

def reverse(sentence):
    words = sentence.split()
    reversed_words = reversed(words) 
    return " ".join(reversed_words)

sentence = input("Please enter a text: ")
print(reverse(sentence))

#Remove extra spaces from a sentence

def remove_space(x):
    return " ".join(x.split())
sentence = input("Please enter a text: ")
print(remove_space(sentence))

#Convert string to title case

def title_mod(x):
    x=x.title()
    return x
sentence=input("plese enter your text:")
print(title_mod(sentence))

#Generate a strong random password

import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation

def password(length):
    return "".join(random.choices(all_chars, k=length))

password_length = int(input("Please enter number of characters in password: "))
print(password(password_length))

# Convert sentence to secret code (Caesar cipher +1)

def secret_language(text):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        else:
            result += char
    return result

text = input("Please enter your text: ")
print(secret_language(text))

#Convert date format from yyyy_mm_dd to dd/mm/yyyy

def convert_time(date_time):
    time=date_time.split("_")
    time=time[2]+"/"+time[1]+"/"+time[0]
    return time
date=input("please enter your date:")
print(convert_time(date))

#Text summarization (show only N words)

def summariz(text,N):
      # N is the maximum number of words to include in summary
    text=text.split()
    text=text[:N:]
    text=" ".join(text)
    return text
text1=input("please enter a text :")
N1=int(input("enter summerizing limit :"))
print(summariz(text1, N1))

#Count occurrences of a character in a string

def count_char(text,char):
    result=text.count(char)
    return result
text1=input("please enter a text:")
char1=input("please enter a character:")
print(count_char(text1, char1))   