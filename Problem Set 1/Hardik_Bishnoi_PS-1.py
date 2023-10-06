""" 
TLDR : 
My approach is based off of sorting the array first using quicksort. 
I try to build the comparision logic into quicksort itself.
Since counting is constant time, it won't affect the partition process in quicksort.

The idea of quicksort is based on divide and conquer, just like other fast sorting algos. 
The algo works by selecting a pivot and elements less than the array go on the left and the rest go on the right
You keep doing quicksort on the left and right arrays till the array is completely sorted.

Best complexity of quicksort : O(nlogn)
Worst complexity of quicksort: O(n^2)

I was inspired by the implementation of this question on leetcode by coolhike, who used merge sort.
https://leetcode.com/discuss/interview-question/3061799/Is-it-possible-to-solve-this-array-algorithms-question-in-time-complexity-lesser-than-O(n2)

I wanted to see if the implementation would work with quicksort, which lies below.


"""


def criticalsort(arr, t):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        count = 0
        
        for j in range(low, high):
            if arr[j] > t * pivot: # I implement the count here. 
                count += 1
                arr[i + 1], arr[j] = arr[j], arr[i + 1]
                i += 1
            else:
                arr[j], arr[i + 1] = arr[i + 1], arr[j]
                i += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1, count

    def quicksort(arr, low, high):
        count = 0
        if low < high:
            pivot_index, events = partition(arr, low, high)
            count += events
            count += quicksort(arr, low, pivot_index - 1)
            count += quicksort(arr, pivot_index + 1, high)
        return count

    return quicksort(arr, 0, len(arr) - 1)

A = [1,2,3,4,3,2,1]

threshold = 1
result = criticalsort(A, threshold)
print("Array A : ", A)
print("Number of critical events for array A : ", result, "\n \n ")

B = [3, 6, 2, 9, -12, 4]

threshold = -1
result = criticalsort(B, threshold)
print("Array B : ", B)
print("Number of critical events for array B : ", result)



