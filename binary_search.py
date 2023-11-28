# def fibo(n):
#     if n == 0 or n==1 or n==2:
#         return n
#     return fibo(n-1) + fibo(n-2)

# n = 30
# for i in range(n):
#     print(fibo(i))


def binary_search(arr, target):
    end = len(arr)-1
    start = 0
    while (start <= end):
        # middle = (start + end)//2 # this can exceed int size 
        middle = start + (end-start)//2
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            end = middle-1
        else:
            start = middle+1
    return -1

# l= [5,7,7,7,8,8,8,8,10]

# print(binary_search(l,7))

# def binary_search_oa(arr, target):
#     e = len(arr)-1
#     s = 0
#     is_asc = arr[s] < arr[e]
#     while (s <= e):
#         m = s + (e-s)//2
#         if arr[m] == target:
#             return m
#         if is_asc:
#             if target > arr[m]:
#                 s = m+1
#             else:
#                 e = m-1
#         else: 
#             if target > arr[m]:
#                 e = m-1
#             else:
#                 s = m+1
#     return -1

# l = [-165,-5,1,9,11,56,78,121,12569]
# print(l,"target: 78")
# print(binary_search_oa(l,78))
# l = l[::-1]
# print(l,"target: 78")
# print(binary_search_oa(l,78))

 
# def ceiling_number(arr, target):
#     end = len(arr)-1
#     start = 0
#     if target>arr[end]:
#         return "No Ceiling"
#     while (start <= end):
#         middle = start + (end-start)//2
#         if arr[middle] == target:
#             return arr[middle]
#         elif target < arr[middle]:
#             end = middle-1
#         else:
#             start = middle+1
#     return arr[start]


# l = [-165,-5,1,9,11,56,78,121,12569]
# print(l,"target: 44")
# print(ceiling_number(l, 500000))

# def floor_number(arr, target):
#     end = len(arr)-1
#     start = 0
#     if target<arr[start]:
#         return "No Floor"
#     while (start <= end):
#         middle = start + (end-start)//2
#         if arr[middle] == target:
#             return arr[middle]
#         elif target > arr[middle]:
#             start = middle+1
#         else:
#             end = middle-1
#     return arr[end]

# print(floor_number(l, 1))

# letters = ["c","f","j"]

# def nextGreatestLetter(letters, target):
#     end = len(letters)-1
#     start = 0
#     while (start <= end):
#         middle = start + (end-start)//2
#         if target > letters[middle]:
#             start = middle+1
#         else: 
#             end = middle-1
#     return letters[start%len(letters)]  

# print(nextGreatestLetter(letters,"c"))



# def binary_search34(arr, target):
#     ans = [-1,-1]
#     start = search(arr,target,find_start_index = True)
#     end = search(arr,target,find_start_index = False)
#     ans[0] = start
#     ans[1] = end
#     return ans

# this function gives the index of what we want to find for element in arr
# def search(arr, target, find_start_index):
#     end = len(arr)-1
#     ans = -1
#     start = 0
#     while (start <= end):
#         middle = start + (end-start)//2
#         if arr[middle] == target:
#             ans = middle
#             if (find_start_index):
#                 end = middle-1
#             else:
#                 start = middle+1
#         elif target < arr[middle]:
#             end = middle-1
#         else:
#             start = middle+1
#     return ans


# l= [5,7,7,7,7,8,8,10]
 
# print(binary_search34(l,7))


# def binary_search(arr, target, start, end):

#     while (start <= end):
#         middle = start + (end-start)//2
#         if arr[middle] == target:
#             return middle
#         elif target < arr[middle]:
#             end = middle-1
#         else:
#             start = middle+1
#     return -1

def binary_search(arr, target, start, end):

    while (start <= end):
        middle = start + (end-start)//2
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            end = middle-1
        else:
            start = middle+1
    return -1

def gkg_infinte_array_search(arr, target):
    start = 0
    end = 1
    
    while(target > arr[end]):
        newstart = end + 1 
        end = end + (end - start + 1)*2 
        start  = newstart
    
    print(binary_search(arr,target,start,end))
    

# arr = [3,5,7,9,10,90,100,140,160,170, 190, 2000, 201214, 2021111]


# target  = 100

# gkg_infinte_array_search(arr, target)



def binary_search_oa(arr, target, s, e):
    e = len(arr)-1
    s = 0
    is_asc = arr[s] < arr[e]
    while (s <= e):
        m = s + (e-s)//2
        if arr[m] == target:
            return m
        if is_asc:
            if target > arr[m]:
                s = m+1
            else:
                e = m-1
        else: 
            if target > arr[m]:
                e = m-1
            else:
                s = m+1
    return -1

def mountain_array(arr):
    start = 0
    end = len(arr)-1

    while (start < end):                    # it shoudl not be start <= end
        middle = start + (end-start)//2
        if arr[middle] > arr[middle+1]:     #Decreasing part of array 
            end = middle                    #not end = m-1 because m may be the possible ans
        else:                               #arr[middle] < arr[middle+1]: ascending part of array
            start = middle+1                #In the end of the loop start = end = middle since
    return start # or end                   # start and end both are finding the max elements 
                                            # in both 2 checks
                                            # hence when they are pointing to one element that is the max

def findInMountainArray(arr, target):
    start = 0
    peak = mountain_array(arr)
    first_try = binary_search_oa(arr, target, start, peak)          # searching in first half
    if first_try:
        return first_try
    return binary_search_oa(arr, target, peak+1, len(arr)-1)        # searching in second half if not found in first half


# l = [1,2,3,4,5,3,1]
# target = 3
# array = [0,1,2,4,2,1]
# target = 3
# print(findInMountainArray(array, target))

def find_pivot(arr):
    start = 0
    end = len(arr) -1
    while(start<=end):
        #4 cases
        middle = start + (end - start)//2
        if middle < end and arr[middle] > arr[middle+1]:
            return middle
        elif middle > start and arr[middle] < arr[middle-1]:
            return middle-1
        elif arr[middle] <= arr[start]:
            end = middle -1
        else:
            start = middle+1
    return -1

def find_pivot_duplicate(arr):
    start = 0
    end = len(arr) -1
    while(start<=end):
        #4 cases
        middle = start + (end - start)//2
        if middle < end and arr[middle] > arr[middle+1]:        #middle<end so out of index doesn't bother
            return middle
        elif middle > start and arr[middle] < arr[middle-1]:
            return middle-1
        if arr[middle] == arr[start] and arr[end] == arr[middle]:       #if start,middle,end are equal that is duplicates so skip them
            #check if start is pivot
            if arr[start] > arr[start+1]:
                return start
            start+=1
            if arr[end] < arr[end-1]:
                return end-1
            end-=1
        elif arr[start] < arr[middle] or (arr[start] == arr[middle] and arr[middle]>arr[end]):  
            start = middle+1
        else:
            end = middle-1
    return -1

# print(find_pivot_duplicate([2,3,9,1,1,2,2,2,2]))

def rotated_binary_search_by_pivot(arr, target):
    pivot = find_pivot_duplicate(arr)
    length = len(arr) -1 
    if pivot == -1:                                                 # array is not rotated
        return binary_search(arr, target,0,length)        #if pivot it found we have two asc sorted array
    if arr[pivot] == target:
        return pivot
    if target >= arr[0]:
        return binary_search(arr, target,0,pivot-1)
    return binary_search(arr,target,pivot+1,length)


def rotation_count(arr):
    pivot = find_pivot(arr)
    # if pivot==-1:       #array not rotated
    #     return 0
    return pivot+1         #array not rotated -> -1+1 = 0

# nums = [2,4,5,6,7,0,1,2,2,2]
# target = 0

# print(rotation_count(nums))


def split_array(nums,k):
    start = max(nums)
    end = sum(nums)

    while start < end:
        mid = start + (end-start)//2
        sums =0
        pieces = 1
        for num in nums:
            if (sums + num) > mid:
                sums = num
                pieces+=1
            else:
                sums +=num
        if pieces > k:
            start = mid+1
        else:
            end = mid
    return start


# nums = [7,2,5,10,8]
# k = 2

# print(split_array(nums,k))


def matrix_linear_search(arr, target):
    #symmetrical matrix r = c

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == target:
                return [i,j]
    return [-1,-1]



def matric_binary_search(m, target):
    r = 0
    c = len(m) - 1
    length = len(m) 

    while(r<length and c>=0):
        if(m[r][c]== target):
            return [r,c]
        if(m[r][c]<target):
            r+=1
        else:
            c-=1
    return [-1,-1]
        
# m = [[10,20,30,40],[15,25,35,45],[28,29,37,49],[33,34,38,50]]
# target = 39
# print(matric_binary_search(m,target))

# Search in the row, between the columns provided
def binary_search_sorted_matrix(m,target, r,cstart,cend):
    while(cstart <= cend):
        middle = cstart + (cend - cstart)//2
        if(m[r][middle]== target):
            return [r,middle]
        if(m[r][middle] < target):
            cstart = middle + 1
        else:
            cend = middle -1
    return [-1,-1]

def sorted_matrix(m, target):
    r = len(m)
    c = len(m[0])
    rstart = 0
    rend = len(m) -1
    cmid = c//2
    if r==1:
        return binary_search_sorted_matrix(m,target,r=0,cstart=0,cend=c-1)        
    #run the loop till two rows are remaining

    while(rstart <(rend -1)):
        rmid = rstart + (rend-rstart)//2
        if(m[rmid][cmid] == target):
            return [rmid,cmid]
        if(m[rmid][cmid] < target):
            rstart = rmid
        else:
            rend = rmid          #now we have two rows
                                #now checking the target in colums of the rows reduced

    if(m[rstart][cmid] == target):
        return [rstart,cmid]
    if(m[rstart + 1][cmid] == target):
        return [rstart+1, cmid]
    if(c>=2):
    #Search in all the 4 halves
        if (target <= m[rstart][cmid-1]):        #1st half
            return binary_search_sorted_matrix(m,target, rstart,cstart=0,cend=cmid-1)
        if (target >= m[rstart][cmid+1] and target<=m[rstart][c-1]): 
            return binary_search_sorted_matrix(m,target, rstart,cstart=cmid+1,cend=c-1)
        if (target <= m[rstart+1][cmid-1]): 
            return binary_search_sorted_matrix(m,target, rstart+1,cstart=0,cend=cmid-1)
        else:
            return binary_search_sorted_matrix(m,target, rstart+1,cstart=cmid+1,cend=cmid-1)
    elif (target >= m[rstart][0]  and  target<= m[rstart][c-1]):
        return binary_search_sorted_matrix(m,target, rstart,cstart=0,cend=c-1)
    return [-1,-1]



m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
m1=[[1]]
m2=[[1]]
target = 2
print(sorted_matrix(m2,target))


            









