""" 
TLDR : 
My approach is based off of sorting the array first using quicksort
Then I find the critical events by comparision


"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def critical(arr, t):
    count = 0
    for i in range (0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i] > arr[j] * t):
                count +=1
    return count



arr = [100, 1, 100, 1]
sorted_arr = quicksort(arr)
print("Unsorted : ", arr)
print("Sorted : ", sorted_arr)

multi = critical(sorted_arr, 0)
print(multi)
