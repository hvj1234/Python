def fib(n):
    a=0
    b=1
    while(a < n):
        print(a)
        c=b+a
        a=b
        b=c
fib(10)
input("Press enter to exit...")