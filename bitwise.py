import math

def q1_even_odd(n):
    return n&1==0       #true if even else odd

# print(q1_even_odd(52))
    

def q2_unique_number(arr):
    unique = 0
    for number in arr:
        unique ^= number
        print(number, unique)
    return unique

# print(q2_unique_number([2,3,4,1,2,1,3,6,4]))


def q3_ith_bit_number(n):
    return n&1<<4       # for 5th bit

# print(q3_ith_bit_number(182))


def q9_magic_number(n):
    ans = 0
    base = 5
    while(n>0):
        last = n&1
        n = n>>1
        ans += last*base
        base = base*5
    return ans

# print(q9_magic_number(6))

def q10_number_digits_base_b(n):
    b = 10

    return int((math.log(n)/math.log(b))+1)


# print(q10_number_digits_base_b(5469))



def q_13_base(base, power):

    ans = 1
    while(power>0):
        if(power&1==1):
            ans*=base
        base*=base
        power=power>>1
    return ans

# print(q_13_base(3,6))


def q14_count_set_bits(n):
    count = 0
    while(n>0):
        count+=1
        n -= (n & (-n))

    return count

# print(q14_count_set_bits(127))

def q15_xor(a):
    
    if (a%4==0):
        return a
    if (a%4==1):
        return 1
    if (a%4==2):
        return a+1
    return 0

def q16_xor_all(a,b):
    ans = q15_xor(b)^q15_xor(a-1) 
    return ans


# print(q16_xor_all(3,9))


def q17_flipping_image(matrix):

    for row in matrix:
        for i in range((len(row)+1)//2):
            row[i], row[len(row)-i-1] =  row[len(row)-i-1]^1, row[i]^1
    
    return matrix

# print(q17_flipping_image([[1,1,0],[1,0,1],[0,0,0]]))


def is_prime(n):
    if n<=1:
        return False
    
    i = 2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True

# print(is_prime(44))


def prime_nos(n):
    c = 0
    for i in range(n):
        if is_prime(i):
            c+=1
    return c

# print(prime_nos(40))


def prime_nos_optimize(n):

    i=2
    primes = [True for k in range(n+1)]    
    while(i*i<=n):
        if(primes[i]):
            for j in range(i*i,n+1,i):
                primes[j] = False
        i+=1
    for i in range(2, n+1):
        if primes[i]:
            print(i)
    return primes


# print(prime_nos_optimize(13))


def sqrt_binary_search(n,p):
    s = 0
    e = n
    root = 0
    while(s<=e):
        m = s + (e-s)//2
        if(m*m==n):
            return m
        if m*m>n:
            e = m-1
        else:
            s = m+1
    root = e
    incr = 0.1
    for i in range(p):
        while(root*root<n):
            root+=incr
        root-=incr
        incr/=10
        
    return "%0.4f" % root

# print(sqrt_binary_search(40,4))

def nrm_sqrt(n):
    x = n 
    while(True):
        root = 0.5 * (x+(n/x))
        if(abs(root-x)<1): #this 1 if reduced will give more closer results
            break
        x = root

    return "%0.4f" % root


# print(nrm_sqrt(40))


def factors(n):
    l1 = []
    l2 = []
    for i in range(1,round(math.sqrt(n))+1):
        if(n%i==0):
            if(n//i==i):
                l1.append(i)
            else:
                l1.append(i)
                l2.append(n//i)
    l2 = l2[::-1]
    for i in range(len(l2)):
        l1.append(l2[i])

    return l1

# print(factors(36))

def gcd(a,b):

    if(a==0):
        return b
    
    return gcd(b%a,a)    


# print(gcd(5,10))


def lcm(a,b):
    return int((a*b)/gcd(a,b))  #lcm = a*b/GCD

print(lcm(9,18))

















