def fibon (n):
    n1=0
    n2=1
    if n < 0:
        print("Try another number")
    elif n==1:
        return 1
    else:
        count=0
        sum=0
        while count <n:
            print(n1,end='')
            nth = n1+n2
            n1=n2
            n2=nth
            count+=1
            sum+=n1
        return sum
print ("Sum of the first 5 terms of the Fibonacci series:",fibon(5))
print("Sum of the first 10 terms of Fibonacci series:",fibon(10))