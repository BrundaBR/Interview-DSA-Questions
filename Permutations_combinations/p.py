result=[]
def func(arr,pattern):
    
    if arr == []:
        
        return result.append(pattern)
    

def perm_iterative(arr):
    pattern=[]
    for x in range(len(arr)):
       
        func(arr[:x]+arr[x+1:],pattern+[arr[x]])
        
    print(result)         

perm_iterative([1,2,3])






# class Solution:
#     def base(self,s):
#         arr=list(s)
#         self.result=[]
#         self.helper(arr,[])
#         return sorted(self.result)


#     def helper(self,arr,pattern):
#         if arr==[]:
#             a=''.join(pattern)
#             self.result.append(a)

#         for x in range(len(arr)):
#             self.helper(arr[:x]+arr[x+1:],pattern+[arr[x]])

# instance=Solution()
# print(instance.base("ABC"))
