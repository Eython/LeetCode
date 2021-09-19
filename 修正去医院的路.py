# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 21:41:13 2021

@author: CSM
"""


A = [1,6,6,3,0,5]
B = [6,2,0,0,4,0]


def solution(A,B):
    
    def traversal(K,path):
        if 0 in links[K]:
            path.append(0)
            return 1
        for city_num in links[K]:
            if city_num not in path:
                path.append(city_num)
                if traversal(city_num,path):
                    return 1
                else:
                    path.pop()
        return 0
    
    links = {}
    for K in range(len(A)):
        if A[K] in links:
            links[A[K]].append(B[K])
        else:
            links[A[K]] = [B[K]]
        if B[K] in links:
            links[B[K]].append(A[K])
        else:
            links[B[K]] = [A[K]]

    reoriented = []
    
    for K in range(1,len(links)):
        path = [K]
        traversal(K,path)
        for ix in range(len(path) - 1):
            for road in zip(A,B):        
                if path[ix+1] == road[0] and path[ix] == road[1]:
                    if road not in reoriented:
                        reoriented.append(road)
                    break

    return len(reoriented)

print(solution(A,B))






