#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:54:45 2018

@author: robson
"""

epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while (abs(guess**2 - y) >= epsilon):
    numGuesses+=1
    guess = guess - (guess**2-y)/(2*guess)
print('numGuesses = ' + str(numGuesses))
print('Square root of {} is about {}'.format(y, guess))
