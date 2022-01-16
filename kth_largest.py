def kth_largest(arr, k):
    for i in range(k - 1):
        arr.remove(max(arr))
    return max(arr)
#O(n)

def kth_largest(arr,k):
    l = len(arr)
    arr.sort()
    return arr[l - k]
#O(nlogn)

import heapq

def kth_largest(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
#O(nlogn)