def rec(n,arr,sum):
    if n==len(arr):
        return sum
    else:
        return rec(n+1,arr,sum+arr[n])


arr=[1,2,3,4]
print(rec(0,arr,0))