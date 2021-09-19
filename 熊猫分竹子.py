# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:05:37 2021

@author: CSM
"""

#竹子长度
n = 4000

#竹子段允许的3种长度
a,b,c = 38,55,99

#问最多可以分出几段？
def func(n,a,b,c) -> int:
    min_num = min(a,b,c)
    max_num = max(a,b,c)
    mid_num = [i for i in (a,b,c) if i not in (min_num,max_num)][0]
    
    for n_min in range(n // min_num,-1,-1):
        rest_no_min = n - n_min * min_num
        
        for n_mid in range(rest_no_min // mid_num,-1,-1):
            rest_for_max = rest_no_min - n_mid * mid_num
            
            if rest_for_max % max_num == 0:
                n_max = rest_for_max // max_num
                
                print(n_min,n_mid,n_max)
                return n_min + n_mid + n_max

print(func(n,a,b,c))



















