# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 02:08:10 2021

@author: CSM
"""

#表示有向图
#A列表的i位置代表边[i]的起点
#B列表的i位置代表边[i]的终点

#A = [0,2,2,3]
#B = [1,1,4,4]

A = [1,6,6,3,0,5]
B = [6,2,0,0,4,0]

#A = [0,1,1,1,1]
#B = [1,2,3,4,5]

#目标节点
destination_node = 0

#links表示value里所有节点都与key节点相连
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

#总节点数
n_node = len(links)

#dp[i]表示从i节点出发到目标节点的路径
dp = [[_] for _ in range(n_node)]
#已遍历的节点的集合(所有已遍历节点同时也是已找到到达目标节点最短路径的节点)
checked = {destination_node}
#一个队列维护待扩展的节点
to_extend = [destination_node]

while 1:
    #如果已遍历所有节点，则退出循环
    if len(checked) == n_node:
        break
    else:
        i = to_extend.pop(0)
        #遍历一个需要扩展的节点的所有相连节点
        for j in links[i]:
            #如果这个相连节点是新节点，则路径是：
            #该节点+最早触达该节点的已遍历节点到达目标节点的路径
            #并将其标记为已遍历节点
            #并将其放入待扩展的队列
            if j not in checked:
                dp[j].extend(dp[i])
                to_extend.append(j)
                checked.add(j)

#需要重定向的边
reoriented = []

#遍历各个其他节点去目标节点的路径
for K in range(1,len(dp)):
    path = dp[K]
    #遍历路径经过的每一条边
    for ix in range(len(path) - 1):
        #找到这条边原本的方向表示
        for road in zip(A,B):  
            #如果方向相反，则需要重定向
            if path[ix] == road[1] and path[ix+1] == road[0]:
                #排除重复添加
                if road not in reoriented:
                    reoriented.append(road)
                break

#返回需要重定向的边数量
print(len(reoriented))





