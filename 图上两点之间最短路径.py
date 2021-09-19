# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:47:54 2021

@author: CSM
"""

#BDS广度优先搜索，有环无环都通用
#广度优先搜索的扩展原则是先生成的节点先扩展，所以可以求得最短路径

#links表示value里所有节点都与key节点相连
links = {
         0: [6, 3, 4, 5],
         1: [6],
         2: [6, 4],
         3: [0, 4],
         4: [0, 3, 2],
         5: [0],
         6: [1, 2, 0],
         }

#指定起点
start_node = 1
        
#目标节点
destination_node = 4

#总节点数
n_node = len(links)

#dp[i]表示从i节点出发到目标节点的路径
dp = [[_] for _ in range(n_node)]
#已遍历的节点的集合(所有已遍历节点同时也是已找到到达目标节点最短路径的节点)
checked = {destination_node}
#一个队列维护待扩展的节点
to_extend = [destination_node]

while 1:
    #如果已触达指定起点，则退出循环
    if start_node in checked:
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

#返回最短路径
print(dp[start_node])






























