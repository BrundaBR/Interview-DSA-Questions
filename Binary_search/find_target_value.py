result=[]
def binary_search(arr,t):
    s=0
    e=len(arr)-1
    d=0
    while s <= e:
        mid=s+(e-s)//2
        if arr[mid]==t:
            print(mid)
            continue
        elif arr[mid] < t:
            s=mid+1
        else:
            e=mid-1
  
    return -1

arr=[5,7,7,8,8,10]
print(binary_search(arr,8))