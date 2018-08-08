#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 13:08:17 2018

@author: shuayb
<<<<<<< HEAD

Assignment:
Write a program that does the following in order:

Asks the user to enter a number “x”
Asks the user to enter a number “y”
Prints out number “x”, raised to the power “y”.
Prints out the log (base 2) of “x”.
Use Spyder to create your program, and save your code in a file named ‘ps0.py’. An example
of an interaction with your program is shown below. The words printed in blue are ones the
computer should print, based on your commands, while the words in black are an example of
a user's input. The colors are simply here to help you distinguish the two components.

Enter number x: 2
Enter number y: 3
X**y = 8
log(x) = 1
"""

#import numeric python.
import numpy

#assign user input and change it to type integer to be able to do power operation.
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

#diplay your result with print method i.e print(), and also make your calculation display along the text using string formatting
print("X**y = %d" %(x**y))
print("log(x) = %d" %(numpy.log2(x)))


