#Q3. wap to perform various operations on 2 integers

int1=int(input('Enter first integer -> '))
int2=int(input('Enter second integer -> '))

quo=int1//int2
rem=int1%int2

print('\nPart A) -> ')
print('Quotient callable ? ->',callable(quo))
print('Remainder callable ? ->',callable(rem),'\n')

print('Part B) -> ')
if quo == 0:
    print('The quotient is zero \n')
if rem == 0:
    print('The reminder is zero \n')
if quo != 0 and rem != 0:
    print('All the values are non zero \n')

print('Part C) -> ')
list1=[quo+4,rem+4,rem+5,quo+5,rem+5,quo+6,rem+6]

result = []
for i in range(len(list1)):
    if list1[i]>4:
        result.append(list1[i])
print(f'Filtered out numbers: {result} \n')

print('Part D) -> ')
setresult=set(result)
print('Set -> ',setresult,'\n')

print('Part E) -> ')
setfrozen=frozenset(setresult)
print('Immutable set ->',setfrozen,'\n')

print('Part F) -> ')
print('Hash value of the max value from the above set -> ', hash(max(setfrozen)))
