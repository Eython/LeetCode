# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:30:34 2021

@author: CSM
"""

#comparatorValue代表：
#a中有多少个数，与b中的数的差的绝对值的最小值大于d

#思路：
#通过二分查找，先找出对于a中每一个来说，在已排列好的b中与哪个数最接近，差的绝对值最小，
#然后对比差的绝对值和d，大于d则计数+1

# 1
a = [7,5,9,1,999,750,600,12,988,4]
b = list(range(0,1000,8))
d = 3

##2
#a = [3,1,5]
#b = [5,6,7]
#d = 2


def comparatorValue(a:list,b:list,d:int) -> int:
    comparator_value = 0
    
    b = sorted(b)
    last_index = len(b) - 1
    
    for num_a in a:
        
        if num_a < b[0]:
            min_abs_diff = b[0] - num_a
        elif num_a > b[-1]:
            min_abs_diff = num_a - b[-1]
        else:
            left = 0
            right = last_index
            
            while 1:
                ix = int(left + (right - left) / 2)
                if b[ix] > num_a:
                    right -= int((right - left) / 2)
                else:
                    if b[ix+1] < num_a:
                        left += int((right - left) / 2)
                    else:
                        min_abs_diff = min(b[ix+1] - num_a,num_a - b[ix])
                        break

        if min_abs_diff > d:
            comparator_value += 1

    return comparator_value
                
print(comparatorValue(a,b,d))
    



