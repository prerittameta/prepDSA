def printn(n):
    
    if(n==5):
        return
    else:
        print(n)
        printn(n+1)

# printn(1)


def fibonacci(n):

    if n in (0,1):
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(5))






