count=0
sum=0
while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        fval=print('Invalid input')
        continue
    print(fval)
    count=count+1
    sum=sum+fval
    print(count,sum,fval)
print('All done')
print('After',count,sum,sum/count)
