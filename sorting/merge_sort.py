def merge_sort(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]

        #recurrsion
        merge_sort(left)
        merge_sort(right)

        #merge
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    
arr=[5,6,7,8,9,23,4,5,0]
merge_sort(arr)
print(arr)