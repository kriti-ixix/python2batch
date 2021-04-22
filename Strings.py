#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:17:35 2021

@author: kritixblaze
"""

example = "Hello World!"
tweet = "Hi #Twitter #Nice"

#Length of a string
print(len(example))

one = "Hello"
two = "World"
three = one + two

#Concatenation
print(one + " " + two + "!")
print((one + " ") *10)

#Converting to upper or lower case
print(one.lower())
print(one.upper())

#Splitting
print(example.split())
print(example.split("o"))
print(tweet.split("#"))

#Slicing
print(example[8])
print(example[1:5:2])
print(example[::-1])
