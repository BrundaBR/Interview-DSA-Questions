def merge_sort(l,r):
    result=[]
    i=0
    j=0
    #handle for none
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            
           
            i+=1
        else:
            result.append(r[j])
           
            j+=1

    while i <len(l):
        result.append(l[i])
        i+=1

    while j <len(r):
        result.append(r[j])
        j+=1
    
             
result=[]

def merge(arr):

    if len(arr)>=1:
        return arr
    else:
        l=merge(arr[:len(arr)//2])
        r=merge(arr[len(arr)//2:])

        
       
arr=[5,2,3,1]
(merge(arr))