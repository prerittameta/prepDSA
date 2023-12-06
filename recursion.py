import math

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

# print(fibonacci(5))


def q2_1_to_n(n):
    if(n==0):
        return
    q2_1_to_n(n-1)
    print(n) 
     
# print(q2_1_to_n(5))


def q3_factorial(n):
    if n==1 or n==0:
        return 1
    return n*q3_factorial(n-1)

# print(q3_factorial(5))


def q4_sum(n):
    if n==1 or n==0:
        return 1
    return n+sum(n-1)


def q5_sum_of_digits(n):
    if n==0:
        return 0
    return n%10 + q4_sum_of_digits(n//10)

# print(q5_sum_of_digits(1342))


def q6_product_of_digits(n):
    if n==0:
        return 1
    return n%10 * q6_product_of_digits(n//10)

# print(q6_product_of_digits(504))


def q7_reverse_number(n):
    digits = int(math.log10(n) + 1)
    return helper(n, digits)

def helper(n, digits):
    if n==0:
        return n
    rem = n%10
    return rem * int(math.pow(10, digits-1)) + helper(n//10, digits-1)

# print(q7_reverse_number(1342))


def q8_palindrome(n):
    digits = int(math.log10(n) + 1)
    return helper(n, digits)==n

# print(q8_palindrome(120021))


def q9_count_zeroes(n):
    return helper2(n,0)


def helper2(n,c):
    if(n==0):
        return c
    rem = n%10
    if (rem==0):
        return helper2(n//10,c+1)
    return helper2(n//10,c)

# print(q9_count_zeroes(50102)


def q1_array_sorted(arr, index):
    if index == len(arr)-1:
        return True
    return arr[index] < arr[index+1] and q1_array_sorted(arr, index+1)

arr = [1,2,1,8,9,12]
# print(q1_array_sorted(arr,0))

def q2_linear_search(arr, target, index):
    if index == len(arr)-1:
        return False
    if arr[index] == target:
        return index
    return q2_linear_search(arr, target, index+1)

# print(q2_linear_search(arr,1,0))


def q2b_linear_search(arr, target, index):
    if index == -1:
        return False
    if arr[index] == target:
        return index
    return q2b_linear_search(arr, target, index-1)

# print(q2b_linear_search(arr,8,len(arr)-1))


result_list = []

def q3_linear_search(arr, target, result_index):
    if result_index == len(arr)-1:
        return False
    if arr[result_index] == target:
        result_list.append(result_index)
    return q3_linear_search(arr, target, result_index+1)

# arr = [1,2,3,9,5,7,8,1,2,8,6,3,1]
# q3_linear_search(arr,8,0)
# print(result_list)


def q4_linear_search(arr, target, result_index, result_list):
    if result_index == len(arr)-1:
        return result_list
    if arr[result_index] == target:
        result_list.append(result_index)
    return q4_linear_search(arr, target, result_index+1, result_list)

# arr = [1,2,3,9,5,7,8,1,2,8,6,3,1]
# result_list= []
# print(q4_linear_search(arr,8,0, result_list))


def q4_linear_search(arr, target, result_index):
    result_list = []
    if result_index == len(arr)-1:
        return result_list
    if arr[result_index] == target:
        result_list.append(result_index)
    ans_below_calls = q4_linear_search(arr, target, result_index+1)
    result_list.extend(ans_below_calls)
    return result_list

# arr = [1,2,3,9,5,7,8,1,2,8,6,3,1]
# print(q4_linear_search(arr,8,0))


def q5_r_binary_search(arr,target,s,e):
    if s>e:
        return -1
    m=s+(e-s)//2
    if(arr[m] == target):
        return m
    if arr[s] <= arr[m]:
        if target >= arr[s] and target <= arr[m]:
            return q5_r_binary_search(arr, target, s, m-1)
        else:
            return q5_r_binary_search(arr, target, m+1, e)
    if target >= arr[m] and target <=arr[e]:
        return q5_r_binary_search(arr, target, m+1, e)
    return q5_r_binary_search(arr, target,s, m-1)

arr = [5,6,7,8,9,1,2,3]
target = 3
# print(q5_r_binary_search(arr, target, 0, len(arr)-1))


def q1_pattern(r,c):
    if (r==0):
        return
    if c<r:
        print("*", end = "")
        q1_pattern(r,c+1)
    else:
        print("")
        q1_pattern(r-1,0)

# q1_pattern(4,0)

def q2_pattern(r,c):
    if (r==0):
        return
    if c<r:
        q2_pattern(r,c+1)
        print("*", end = "")
    else:
        q2_pattern(r-1,0)
        print("")

# q2_pattern(4,0) 

def q3_bubble_sort(arr, r, c):      # r = i and c = j
    if (r==0):
        return
    if c<r:
        if arr[c] > arr[c+1]:
            arr[c], arr[c+1] = arr[c+1], arr[c]
        q3_bubble_sort(arr,r,c+1)
    else:
        q3_bubble_sort(arr,r-1,0)

# arr = [5,6,7,8,9,1,2,3]
# q3_bubble_sort(arr,len(arr)-1,0)
# print(arr)


def q4_selection_sort(arr, r, c, max):
    if (r==0):
        return
    if c<r:
        if arr[c] > arr[max]:
            q4_selection_sort(arr,r,c+1,c)
        else:
            q4_selection_sort(arr,r,c+1,max)
    else:
        arr[r-1], arr[max] = arr[max], arr[r-1]
        q4_selection_sort(arr,r-1,0,0)

# arr = [5,1,10,8,9,4,2,3]
# q4_selection_sort(arr,len(arr),0,0)
# print(arr)

def merge(first, second):
    i = 0
    j = 0
    k = 0
    mix = [None]*(len(first)+len(second))
    while(i<len(first) and j<len(second)):
        if (first[i] < second[j]):
            mix[k] = first[i]
            i+=1
        else:
            mix[k] = second[j]
            j+=1
        k+=1

    while(i<len(first)):
        mix[k] = first[i]
        i+=1
        k+=1

    while(j<len(second)):
        mix[k] = second[j]
        j+=1 
        k+=1
    return mix

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left  = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    return merge(left, right)

# arr = [5,1,10]
# arr = merge_sort(arr)
# print(arr)


def merge_in_place(arr, s, mid, e):
    i, j, k = s, mid, 0

    mix = [None]*(e-s)

    while(i<mid and j<e):
        if (arr[i] < arr[j]):
            mix[k] = arr[i]
            i+=1
        else:
            mix[k] = arr[j]
            j+=1
        k+=1

    while(i<mid):
        mix[k] = arr[i]
        i+=1
        k+=1

    while(j<e):
        mix[k] = arr[j]
        j+=1 
        k+=1

    for i in range(len(mix)):
        arr[s+i] = mix[i]


def merge_sort_in_place(arr,s,e):
    if e-s == 1:
        return
    mid = (s+e)//2
    merge_sort_in_place(arr,s,mid)
    merge_sort_in_place(arr,mid,e)

    merge_in_place(arr, s, mid, e)

arr = [5,1,10,8,9,7,15]
merge_sort_in_place(arr,0,len(arr))
print(arr)


















