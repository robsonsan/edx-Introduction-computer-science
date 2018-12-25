# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.



"""

def toChar(s):
    s = s.lower()
    ans = ''
    for c in s:
        if (c in 'abcdefghijklmnopqrstuvwxyz'):
            ans = ans + c
    return ans


def isPalindrome(frase):
    f = toChar(frase)
    
    if(len(f)<=1):
        return True
    else:
        return f[0]==f[-1] and isPalindrome(f[1:-1])

print(isPalindrome('Are we not drawn onward to new era?'))