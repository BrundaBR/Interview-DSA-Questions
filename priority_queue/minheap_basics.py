import heapq

arr=[1,7,8,9,5,6,0]
hp=[]
for i in arr:
    heapq.heappush(hp,i)
print(hp)