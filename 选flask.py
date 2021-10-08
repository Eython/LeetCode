# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:11:18 2021

@author: CSM
"""

requirements = [4,6]

flaskTypes = 3

markings = [
            [0,5],[0,7],[0,10],
            [1,4],[1,10],
            ]


def chooseFlask(requirements,flaskTypes,markings):
    
    min_waste = float('inf')
    min_index = -1
    
    index = 0
    mk = []

    max_requirements = max(requirements)

    for i in markings:
        if i[0] == index:
            mk.append(i[1])
        else:
            if max(mk) >= max_requirements:
                waste = sum(min(j for j in mk if j >= req) - req for req in requirements)

                if waste < min_waste:
                    min_waste = waste
                    min_index = index

            mk = [i[1]]
            index += 1

    if max(mk) >= max_requirements:
        waste = sum(min(j for j in mk if j >= req) - req for req in requirements)

        if waste < min_waste:
            min_waste = waste
            min_index = index

    return min_index


print(chooseFlask(requirements,flaskTypes,markings))




