# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 01:13:25 2021

@author: CSM
"""

from random import randint

A = list(range(1000)) + [randint(1002,100000) for _ in range(10000)] + [1002]

def Solution(A):    
    #排列好的数组
    sorted_array = sorted(set(i for i in A if i > 0))
    
    #没有1则返回1
    if 1 not in sorted_array:
        return 1
    
    #只有一个数则必然是只有1，返回2
    if len(sorted_array) == 1:
        return 2
    
    #全是连续返回最后一个数+1
    if sorted_array[-1] == len(sorted_array):
        return sorted_array[-1] + 1
    
    left = 0
    right = len(sorted_array)

    while 1:
        ix = int(left + (right - left) / 2)
        #索引和值相差1则前面所有数都连续
        if sorted_array[ix - 1] == ix:
            #当前值不是，则返回当前值的索引+1
            if sorted_array[ix] != ix + 1:
                return ix + 1
            #当前值也是，则范围从左侧缩窄
            else:
                left += int((right - left) / 2)
        #否则前面缺少了某个数，范围从右侧缩窄
        else:
            right -= int((right - left) / 2)
        

print(Solution(A))








