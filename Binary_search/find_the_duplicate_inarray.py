def binary_search(arr):
    s=0
    e=len(arr)-1
    d=0
   # or arr[mid]==arr[mid-1]
    while s <= e:
        mid=s+(e-s)//2
        if arr[mid]==arr[mid+1]:
            
            return arr[mid]
        elif d==0:
            e=mid-1
            d=1
        elif d==1:
            s=mid+1
            e=len(arr)-1
            d=0
    return -1

arr=[1,1,2,3,4]
print(binary_search(arr))
