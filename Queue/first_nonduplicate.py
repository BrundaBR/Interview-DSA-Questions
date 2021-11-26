
def first_non_dup(s):
    dic={}

    for i in range(len(s)):
        ele=s[i]
        for j in range(i+1,len(s)):
            if ele==s[j]:
                continue
            else:
                return i

        
    # idx=0
    # while idx<len(s):
    #     ele=s[idx]
    #     for j in range(idx+1,len(s)):
    #         if ele==s[j]:
    #             idx+=1
    #         else:
    #             return idx
        
                

s="leetcode"
print(first_non_dup(s))