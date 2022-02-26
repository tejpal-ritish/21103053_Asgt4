#Q1. wap to solve the tower of hanoi for three disks

def hanoi(n,first,extra,last):
    if n>0:
        hanoi(n-1,first,last,extra)
        print('Transfer disk from',first,'to',last)
        hanoi(n-1,extra,first,last)
        
hanoi(3,'A','B','C')
