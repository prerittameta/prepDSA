

def bubble_sort(arr):

    for i in range(len(arr)):
        swapped = False
        for j in range(1,len(arr) -i):
            if(arr[j] < arr[j-1]):
                arr[j],arr[j-1] = arr[j-1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# arr = [5,4,3,2,1]
# arr1 = [1,2,3,4,5]
# print(bubble_sort(arr1))

def maxvalue(arr, start, end):
    maxindex = start
    for i in range(start, end+1):
        if(arr[maxindex] < arr[i]):
            maxindex = i
    return maxindex
            

def selection_sort(arr):

    for i in range(len(arr)):
        end = len(arr) - i - 1
        maxindex = maxvalue(arr,0,end)
        #swap maxv with last index value
        arr[maxindex], arr[end] = arr[end], arr[maxindex]
    return arr

# arr = [5,4,3,2,1]
# arr1 = [4,5,1,2,3]
# print(selection_sort(arr))


def insertion_sort(arr):
    
    for i in range(1,len(arr)): 
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key
    return arr
     

# arr1 = [5,9,1,4,3]
# print(insertion_sort(arr1))

def quick_sort(arr):
    i = 0
    while(i<len(arr)):
        correct_index = arr[i] - 1
        if(arr[i] != arr[correct_index]):
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i+=1
    return arr

#  


# def quick_sort_q1(nums):
#     i = 0
#     n = len(nums)
#     while(i<n):
#         correct_index = nums[i]
#         if(nums[i] < n and nums[i]!=nums[correct_index]):
#             nums[i], nums[correct_index] = nums[correct_index], nums[i]
#         else:
#             i+=1
#     for i in range(n):
#         if(nums[i]!=i):
#             return i
#     return n
#     # return ((n*(n+1))//2)-(sum(nums))


# # arr = [4,0,2,1] 
# # print(quick_sort_q1(arr))

# def quick_sort_q2(nums):
#     i = 0
#     l = []
#     while(i<len(nums)):
#         correct_index = nums[i] - 1
#         if(nums[i] != nums[correct_index]):
#             nums[i], nums[correct_index] = nums[correct_index], nums[i]
#         else:
#             i+=1
#     for i in range(len(nums)):
#         if(nums[i]!=(i+1)):
#             l.append(i+1)

#     return l

# # arr = [4,3,2,7,8,2,3,1] 
# # print(quick_sort_q2(arr))


# def quick_sort_q3(nums):
#     i = 0
#     while(i<len(nums)):
#         if(nums[i]!= i+1):
#             correct_index = nums[i] - 1
#             if(nums[i] != nums[correct_index]):
#                 nums[i], nums[correct_index] = nums[correct_index], nums[i]
#             else:
#                 return nums[i]
#         else:
#             i+=1
#     return -1

# # arr = [1,3,4,2,2] 
# # print(quick_sort_q3(arr))


# def quick_sort_q4(nums):
#     i = 0
#     l = []
#     while(i<len(nums)):
#         correct_index = nums[i] - 1
#         if(nums[i] != nums[correct_index]):
#             nums[i], nums[correct_index] = nums[correct_index], nums[i]
#         else:
#             i+=1
#     for i in range(len(nums)):
#         if(nums[i]!=(i+1)):
#             l.append(nums[i])

#     return l

# # arr = [4,3,2,7,8,2,3,1] 
# # print(quick_sort_q4(arr))


# def quick_sort_q5(nums):
#     i = 0
#     n = len(nums)
#     while(i<n):
#         correct_index = nums[i] - 1
#         if(nums[i]!=nums[correct_index]):
#             nums[i], nums[correct_index] = nums[correct_index], nums[i]
#         else:
#             i+=1

#     for i in range(n):
#         if(nums[i]!=i+1):
#             return [nums[i],i+1]
#     return n

# # arr = [2,1,4,2,6,5] 
# # arr2 = [3,1,1]
# # print(quick_sort_q5(arr2))



# def quick_sort_q6(nums):
#     i = 0
#     n = len(nums)
#     while(i<n):
#         correct_index = nums[i] - 1
#         if(nums[i]> 0 and nums[i] <= n and nums[i]!=nums[correct_index]):
#             nums[i], nums[correct_index] = nums[correct_index], nums[i]
#         else:
#             i+=1

#     for i in range(n):
#         if(nums[i]!=i+1):
#             return i+1
#         elif i==(n-1):
#             return n+1 
#     return -1

# # arr = [3,4,-1,1] 
# # arr2 = [1]
# # print(quick_sort_q6(arr2))


def q1_missing_n(arr):
    i = 0
    n = len(arr)

    while(i<n):
        c_i = arr[i]
        if(arr[i]<n and arr[i]!=arr[c_i]):
            arr[i], arr[c_i] = arr[c_i], arr[i]
        else:
            i+=1
    for i in range(n):
        if(arr[i]!=i):
            return i
    return arr

# arr = [4,3,0,1] 
# print(q1_missing_n(arr))

def q2_all_missing_n(arr):
    i = 0
    n = len(arr)
    l = []
    while(i<n):
        c_i = arr[i]-1
        if(arr[i]!=arr[c_i]):
            arr[i], arr[c_i] = arr[c_i], arr[i]
        else:
            i+=1
    for i in range(n):
        if(arr[i]!=i+1):
            l.append(i+1)
    return l

# arr = [4,3,2,7,8,2,3,1] 
# print(q2_all_missing_n(arr))

def q3_duplicate_n(arr):
    i = 0
    n = len(arr)
    l = []
    while(i<n):
        if(arr[i]!=i+1):
            c_i = arr[i]-1
            if(arr[i]!=arr[c_i]):
                arr[i], arr[c_i] = arr[c_i], arr[i]
            else:
                return arr[i]
        else:
            i+=1
    return -1

# arr = [1,3,4,2,2] 
# print(q3_duplicate_n(arr))


def q4_duplicate_all_n(arr):
    i = 0
    n = len(arr)
    l = []
    while(i<n):
        c_i = arr[i]-1
        if(arr[i]!=arr[c_i]):
            arr[i], arr[c_i] = arr[c_i], arr[i]
        else:
            i+=1
    for i in range(n):
        if(arr[i]!=i+1):
            l.append(arr[i])
    return l

# arr = [4,3,2,7,8,2,3,1]
# print(q4_duplicate_all_n(arr))

def q5_set_mismatch(arr):
    i = 0
    n = len(arr)
    while(i<n):
        c_i = arr[i]-1
        if(arr[i]!=arr[c_i]):
            arr[i], arr[c_i] = arr[c_i], arr[i]
        else:
            i+=1
    for i in range(n):
        if(arr[i]!=i+1):
            return [arr[i],i+1]
    return [-1,-1]

# arr = [2,1,4,2,6,5] 
# arr2 = [1,1]
# print(q5_set_mismatch(arr2))


def q6_first_missing_positive(arr):
    i = 0
    n = len(arr)
    while(i<n):
        c_i = arr[i]-1
        if(arr[i]<=n and arr[i]>0 and arr[i]!=arr[c_i]):
            arr[i], arr[c_i] = arr[c_i], arr[i]
        else:
            i+=1

    for i in range(n):
        if(arr[i]!=i+1):
            return (i+1)
        elif i==(n-1):
            return n+1
    return -1

# arr = [3,4,-1,1] 
# arr2 = [1]
# arr3 = [1,2,3,4,5]
# print(q6_first_missing_positive(arr3))









