def convert_to_Bin(n):
    result=[]
    rem=[]
    s=""
    for num in range(1,n+1):
        while num>0:
            re=num%2
            rem.append(int(re))
            num=int(num/2)
        while rem!=[]:
            ele=rem.pop()
            s+=str(ele) 
        result.append(s)
        s=""
        rem=[]
    print(result)
                          
N=2
convert_to_Bin(N)