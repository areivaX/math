# -*- coding: utf-8 -*-
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''
from math import floor


def flop(x, new) : # x < t ≤ new, where t is a multiple of 10 ("skips a 10")
    return (floor(new/10.0)>floor(x/10.0))&(new%10 != 0)

def flip(x, new) : # t < x < t+5 < t+10  ("skips a 5")
    # assume done after flop, so we're within same multiple of 10
    return ((x%10) < 5) and ((new%10) > 5)

def add_s():
    numL = [] 
    ss = 3  
    new = 3
    while new < 997 : 
        x = new 
        new += 3
        if flop(x,new) : 
            ss += floor(new/10.0)*10 # skipped a multiple of 10, add back in 
        elif flip(x, new) :
            ss += floor(x/10.0)*10 + 5
        
        ss += new 
    return ss

print add_s()
            

