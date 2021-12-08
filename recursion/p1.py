def fun(arr,r):
    if arr!=[]:
       x=arr.pop()
       r.append(x)
       fun(arr,r)
    return r
    
      

arr=[1,2,3]
print(fun(arr,[]))
