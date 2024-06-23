def recur(n):
    if n<1:
        print(f'{n} is less than 1')
    else:
        recur(n-1)
        print(f'Number is : {n}')
        
a= recur(4)