#Q2. wap to print pascal's triangle using recursion and iteration

from math import comb
n = int(input('Enter the number of rows you want -> '))

print("The Pascal's Triangle using recursion is as shown ->")
def recur(num):
    if num==1:                                                                                        
        return [[1]]
    else:
        result=recur(num-1)                                                                  
        row=[1]                                                                               
        lastrow=result[-1]                                                                       
        for i in range(len(lastrow)-1):                                                          
            row.append(lastrow[i] + lastrow[i+1])
        row+=[1]                                                                              
        result.append(row)                                                                    
    return result
for i in recur(n):
    print((n-len(i))*' ',end='')                                                              
    for j in i:
        print(j, end =' ')
    print()


print("The Pascal's Triangle using iteration is as shown ->")
for i in range(n):
    print((n-i)*' ',end='')
    for j in range(n):
        if comb(i,j) != 0:
            print(comb(i,j),end=' ')
    print()                                                                                         
