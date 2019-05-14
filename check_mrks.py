# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:18:28 2019

@author: behal
"""
def check_marks(a,b):
    from nltk import ConditionalFreqDist, FreqDist
    s = a.split()
    c=0
    fd = FreqDist(s)
    for i in range(0,len(b)):
        if fd.get(b[i]) != None : 
            c=c+0.5
    return c
    
