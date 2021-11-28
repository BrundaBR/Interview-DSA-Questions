def reverse_kth(arr,k):
    
    result=[]  # space comp: O(n)
    for i in range(k-1,-1,-1):  # time O(n)
        result.append(arr[i])
    result.extend(arr[k:])    # time O(n)==
    # total time comp =O(n)
    print(result)

reverse_kth([4,3, 2, 1],4)