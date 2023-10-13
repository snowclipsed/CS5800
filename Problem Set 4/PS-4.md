# Problem Set 4

**Solutions to Problem Set 4, submitted by Hardik Bishnoi (NUID: ) for Algorithms - CS5800 in October 2023.**



## Problem #1

## (a) Demonstrate the Quicksort algorithm on the input array A = [3, 1, 5, 7, 6, 2, 4], showing how eventually the algorithm outputs the sorted array [1, 2, 3, 4, 5, 6, 7]. Clearly show all of your steps. 



Solution (a):

We're given the input array A = [3,1,5,7,6,2,4]

Let's review the quicksort algorithm using Lomuto's method:

We input an array, $arr$. 

We also have two indices, $low$ and $high$ which are the range of the partitioned array.

- **Step 1.** Choose the last element as the pivot element, or $arr[high]$
- **Step 2.** Initialize 2 iterative pointers $i$ and $j$ to track the elements during partitioning. Set $i = low$ and $j = low$.
- **Step 3.** Now we start iterating $j$ through the elements from index $low$ to index $high - 1$ where the latter is inclusive. The goal is to move elements smaller than the pivot to the left side and elements greater than the pivot to the right side, hence partitioning the array.
- Inside the loop, compare the current element $arr[j]$ with the pivot
  - If $arr[j]$ < pivot, swap $arr[i]$ and $arr[j]$ and increment $i$ to move the smaller element to the left side of the pivot. 
  - If $arr[j]$ > pivot, do nothing and continue to the next element.
- Once the loop is finished, we have divided the original array $arr$ successfully into two subarrays. Swap the pivot element with $arr[i]$, and the pivot has found its correct position in the array. Here, the subarray on the left side of the pivot which are $low$ to $i$, will be <= pivot itself. Meanwhile, all the elements in the right subarray which are will be greater than the pivot. 
- Now, we return $i$ as it will become the new pivot.

```
function quicksort(arr, low, high)
    pivot = arr[high]  
    i = low
    j = low

    for j from low to high - 1 //high-1 is inclusive
        if arr[j] < pivot
            swap arr[i] and arr[j]
            i = i + 1
    swap arr[i] and arr[high]  

    return i  

```

Now let's apply this to our array **A = [3,1,5,7,6,2,4]**.



