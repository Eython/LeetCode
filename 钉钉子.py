def solution(A,K):
    n = len(A)
    best = 0
    count = 0
    for i in range(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
            count = 0
        best = max(best,count)
        
    result = best + 1 + K
    result = min(result,n)
    
    return result




A = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5]
K = 0




