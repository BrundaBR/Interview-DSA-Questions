



class Solution:
    def base(self,s):
        arr=list(s)
        self.result=[]
        self.helper(arr,[])
        return sorted(self.result)


    def helper(self,arr,pattern):
        if arr==[]:
            a=''.join(pattern)
            self.result.append(a)

        for x in range(len(arr)):
            self.helper(arr[:x]+arr[x+1:],pattern+[arr[x]])

instance=Solution()
print(instance.base("ABC"))
