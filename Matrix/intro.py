def matrix_intro(m,t):
    
   for row in matrix:
       for col in range(len(row)):
           if col==0 and col==len(row)-1:break

matrix=[[1,4,5],[9,7,4],[10,11,12]]
matrix_intro(matrix,6)
'''

adding diagonal elements 

def matrix_intro(m,t):
    sum=0
    row=0
    col=0
    while row<len(m) or col<len(m):
        sum+=matrix[row][col]
        row+=1
        col+=1
    print(sum)
'''
