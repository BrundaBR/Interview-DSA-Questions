def first_Nonrepeating(s):
    dict={}
    for i in range(len(s)):
        if s[i] in dict:
            n=dict[s[i]][0]
            
            dict[s[i]]=[n+1,i]
        else:
            dict[s[i]]=[1,i]
    
  
    for key,value in dict.items():
        if value[0]==1:
            return value[1]
        else:
            continue
    return -1
    
s="leetcode"
print(first_Nonrepeating(s))

