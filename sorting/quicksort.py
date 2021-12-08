

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        i=-1
        j=0
        pivot=len(arr)-1
        #getting pivot element
        while j != pivot:
            if arr[j] > arr[pivot]:
                j+=1
            else:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        pivot=i+1
     
        return  quick_sort(arr[:pivot]) + quick_sort(arr[pivot:])

  
   

arr=[4,3,5,2,1]
print(quick_sort(arr))