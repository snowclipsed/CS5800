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

At the first step, we have A = [3,1,5,7,6,2,4]

We set high as the 6th index, we set low as the 0th index.

We set i = 0, and j = 0. Pivot is denoted by $p$. I will denote these iterating pointers in subscript. The array looks like this
$$
3_{ij},1,5,7,6,2,4_p
$$

### **First Recursive Iteration:**

As the for loop begins, we encounter $A[j] < pivot$, hence we swap $i$ and $j$. However, since $i$ and $j$ are on the same index, the same element will get swapped with itself. We increment $i$ and move to the next iteration in the for loop, so $i = j=1$
$$
3,1_{i,j},5,7,6,2,4_{p}
$$
Again, we find that 1 < 4, hence $A[j] < pivot$. Since $i$ and $j$ are at the same index nothing happens and we move to the next index, where $i=j=2$
$$
3,1,5_{i,j},7,6,2,4_{p}
$$
Now, since $A[j] > pivot$, $i$ is not incremented. We, move on to the next index for $j$ but $i$ stays at the 2nd index.
$$
3,1,5_{i},7_j,6,2,4_{p}
$$
Again, since $A[j] > pivot$, we do not increment $i$ and instead move to the next index for $j$ through the for loop.
$$
3,1,5_{i},7,6_j,2,4_{p}
$$
Now, we encounter $A[j]>pivot$ again because $6>4$. So $i$ is not incremented. The for loop will progress and j is incremented to 5.
$$
3,1,5_{i},7,6,2_j,4_{p}
$$
We encounter $A[j] < pivot$, and hence the if statement is proved true. Hence, we swap $A[j]$ and $A[i]$, then we increment $i$, and $j$ is incremented to 7 in the next loop iteration.
$$
3,1,2,7_{i},6,5_j,4_{p}
$$
Next, we exchange $A[i]$ and $A[p]$ which leads to the division of the array into two subarrays, while 4 finds its correct place in the subarray.
$$
3,1,2 \ | \ 4 \ | \ 6,5,7
$$

### **Second Recursive Iteration**

In the second iteration, we consider the left subarray from the original array.

According to lomuto's method, we put pivot = 2.

We put index $i = j = 0$ and this is the resultant array:
$$
3_{ij},1,2_p
$$
Now, we compare the pivot with $A[j]$. Since $A[j] > pivot$, we do not increment i, and we move to the next loop iteration where we increment j :
$$
3_{i},1_j,2_p
$$
We compare $A[j]$ and pivot again, and we satisfy the if condition for $A[j]<pivot$. Hence, we increment swap $A[j]$ and $A[j]$. Next, we increment $i$ and then increment $j$ at the start of the next loop iteration.
$$
1,3_i,2_{jp}
$$
Since we are at the end of the subarray, we swap $A[i]$ with $A[j]$.

The resultant subarray is:
$$
1\ | \ 2 \ | \ 3
$$
The current resultant full array is:
$$
[1]|2|[3]|4|[6,5,7]
$$
Where 2 and 4 have found their correct positions.

Now, let's move to the next iteration where we consider the left subarray of this subarray.

### **Third Recursive Iteration**

We will now consider the left subarray of the previous subarray. Here, we initialize $i=j=0$ again. We also initialize $pivot$ as the last element, which is also $0$. Since $i = j = pivot = 0$, we swap $A[i]$ with $A[p]$ and we have 1 at the same spot.
$$
1_{ijp}
$$
 Hence 1 is at its correct position now and we have our current full array as :
$$
1|2|[3]|4|[6,5,7]
$$

### **Fourth Recursive Iteration**

We will now consider the right subarray split from setting 2 at its correct position.

We will now consider the left subarray of the previous subarray. Here, we initialize $i=j=0$ again. We also initialize $pivot$ as the last element, which is also $0$. Since $i = j = pivot = 0$, we swap $A[i]$ with $A[p]$ and we have 3 at the same spot.
$$
3_{ijp}
$$
Since 3 is at its correct position now, we will have our current full array arranged as :
$$
1|2|3|4|[6,5,7]
$$


## **Fifth Recursive Iteration**

Now, all the elements to the left of the the first pivot **4** have been sorted, so we move to the right subarray $[6,5,7]$

Here, we initialize $i=j=0$ again. We also initialize $pivot$ as the last element which is 7. We have our subarray as :
$$
6_{i,j},5,7_p
$$


Next, we will compare pivot with $A[j]$. Since $A[j]<pivot$, we swap $A[i]$ and $A[j]$. Since $i$ and $j$ are at the same index, we swap 6 with 6. Next, we increment $i$ and increment $j$ at the start of the next iteration.
$$
6,5_{ij},7_p
$$
Next, we will compare pivot with A[j] again. Since $A[j]<pivot$, we increment $i$ and increment $j$ at the start of the next iteration.
$$
6,5,7_{ijp}
$$
Since we have reached at the end of the array, we will swap $A[i]$ with pivot. Since $i = j = p$, 7 stays at its position and has found its correct position in the main array. Hence, we get a resultant array as :
$$
1\ | \ 2 \ | \ 3 \ | \ 4 \ |[6,5] \ | \ 7
$$

### **Sixth Recursive Iteration**

We move to the next recursive iteration with the subarray created by setting 7 at its right position.

Here, we initialize $i=j=0$ again. We also initialize $pivot$ as the last element which is 5. We have our subarray as :
$$
6_{ij},5_p
$$
We compare $A[j]$ with pivot again and find that $A[j]>pivot$ hence we do not increment $i$ and increment j to reach the end of the array. Hence we will now swap $A[i]$ with pivot, resulting in :
$$
5|[6]
$$
Where 5 has found its correct place in the array. Now we are only left with the subarray [6], and the current final array looks like:
$$
1\ | \ 2 \ | \ 3 \ | \ 4 \ | \ [5] \ |\ 6 | \ 7
$$


### **Seventh Recursive Iteration**

Here, we initialize $i=j=0$ again. We also initialize $pivot$ as the last element which is 6. We have our subarray as :
$$
6_{ijp}
$$
Since $j$ is at the end of the array and $i=j=p$ we, swap $A[i]$ with pivot and we do not see any change since this is a single element. Hence 6 has found its place in the array as well.

Hence, all the elements are sorted since no subarray is left.
$$
1\ | \ 2 \ | \ 3 \ | \ 4 \ | \ 5 \ |\ 6 \ | \ 7
$$
Now, we have the resultant array sorted as [1,2,3,4,5,6,7] in 7 recursive iterations.



## 1(b) When PARTITION is called on an array with n elements, we require n − 1 comparisons, since we must compare the pivot element to each of the other n − 1 elements. If the input array is A = [1, 2, 3, 4, 5, 6, 7], show that Quicksort requires a total of 21 comparisons.

### Solution 1(b)

We are given the array A=[1,2,3,4,5,6,7]. This array is a sorted array arranged in ascending order. 

Through the Lomuto method, lets assign iterators i and j = 0 and pivot p as the last element.

Lets initialize a count = 0, which we will increase every time we make a comparision.
$$
[1_{i,j},2,3,4,5,6,7_p]
$$
We compare $A[j]$ with pivot and since $A[j]<pivot$ we swap $A[j]$ and $A[i]$ and increment i and then increment j at the start of the next for loop iteration. We also increment count.

Considering all the elements 1,2,3,4,5,6 are less than the pivot element 7, the above will happen till $j = p$.
$$
[1,2_{i,j},3,4,5,6,7_p]\\
[1,2,3_{i,j},4,5,6,7_p]\\
[1,2,3,4_{i,j},5,6,7_p]\\
[1,2,3,4,5_{i,j},6,7_p]\\
[1,2,3,4,5,6_{i,j},7_p]\\
[1,2,3,4,5,6,7_{i,j,p}]\\
$$


When $j$ reaches the end of the array, $A[i]$ is swapped with $pivot$.

Hence we end up with **6 comparisons.**

The current complete array looks like:
$$
[1,2,3,4,5,6]|7
$$


Next, we will end up with the subarray [1,2,3,4,5,6]. Again, lets assign iterators i and j = 0 and pivot p as the last element 6.

Again, we notice that 1,2,3,4,5 are all less than the pivot element 6 so the i and j will iterate through all the elements till they reach i = j = 5 or the element 6.

Hence the array will look like:
$$
[1,2,3,4,5]|6|7
$$
We have number of comparisons = 5

Similarly we will see a pattern for all the next comparisions:
$$
[1,2,3,4]|5|6|7
$$
comparisons = 4
$$
[1,2,3]|4|5|6|7
$$
comparisons = 3
$$
[1,2]|3|4|5|6|7
$$
comparisions = 2
$$
[1]2|3|4|5|6|7
$$
comparisons = 1
$$
1|2|3|4|5|6|7
$$
The total comparisons are 6+5+4+3+2+1 = 21 comparisons in total. Hence we have proved that this arrangement of elements requires 21 comparisons. 



## 1(c) Determine an input array with 7 elements for which Quicksort requires the minimum number of total comparisons. Clearly demonstrate why your input array achieves the minimum number of comparisons, and explain why there cannot exist a 7-element array requiring fewer comparisons than your array.

### Solution 1(c):

With any combination of elements, the most optimal input array for quicksort would be the one where work done is minimized. Since most of the work done is in the comparisons made, we would like to minimize the number of comparisons for an optimal sorting run. This can be achieved by allowing an equal split in the subarrays which will allow for a lower depth in the recursion tree. We can attempt to find the best case input array by considering an already sorted array first - by somewhat "unsorting" the array.
$$
[1,2,3,4,5,6,7]
$$
If we try to split this array in half and leave one element out, there is only one choice of an element : 4.
$$
[1,2,3]|4|[5,6,7]
$$
This is because any other element will result in an unequally divided array. Let us try 3 instead:
$$
[1,2]|3|[4,5,6,7]
$$
As we can observe, the left subarray is 2 elements long, but the right one has 4 elements - so they are unequal or imbalanced.

Hence 4 must always be in the end of the array.
$$
[1,2,3,5,6,7,4]
$$


Moving to the next iteration of recursion, and applying the same logic, we can see that 2 in [1,2,3] and 6 in [5,6,7] are middle elements which will divide the subarray into equal parts. Hence, we can shift 2 to the right and 6 to the left of their own subarrays so that when 4 is swapped with 6, 6 and 2 both are at the end of their subarrays, and the final array will look like this:
$$
1,3,2,6,7,5,4
$$
Notice that we did not consider the positions of either of the elements that are left : which are 1, 3, 5, 7. This is because they do not impact the number of comparisons, since both of them are always going to be compared with the pivot regardless of their position. 

Lets try to make the number of comparisons with this array:
$$
[1,3,2,6,7,5,4]
$$
We can define a function for the number of comparisons needed for the ideal case where the split is equal.

Let the number of comparisons made be a recursive function $f(n)$. Now, $f(n)$ will be equal to the comparisons for the 2 following subarrays created + the work done for the first original array in the first iteration :
$$
f(n) = 2(f(n/2)) +(n-1)
$$
Substituting n = 7 we have:
$$
f(7) = 2(f(3)) +6 \Rarr 2(2(f(1)+2)) = 10
$$
However, we must disprove that there are any other combinations of arrays aside the ones which have 2 at the 2nd index, 6 at the 3rd index and 4 at the 6th index. 

So let's take a case for all three of these:

1. If 4 was not at the end, then consider [1,3,2,4,7,6,5]
   $$
   [1_{ij},3,2,4,7,6,5_p]
   $$
   Start at i and j = 0, since 1,3,2,4 are all smaller than 5 i increments and j also increments, with 4 comparisons each time.
   $$
   [1,3,2,4,7_{ij},6,5_p]
   $$
   Next at 7 and 6 j increments but I doesn't - leading to number of comparisons to be 6

   Next, 5 is swapped with 7, leading to two subarrays [1,3,2,4] and [6,7]

   In the [1,3,2,4] subarray, we have 4 as pivot and then 3 comparisons (so comparisons = 9) and the subarray is split into [1,3] and [2,4]

   next, we have 1 comparison each in these subarrays, so total comparisons = 11

   Next, for the next subarray [6,7] we have 1 comparison again, leading to total of 12 comparisons to sort.

2. If either 2 or 6 are moved:

   Let's move 6 to the end of its subarray instead, and then we will have a subarray:
   $$
   [1_{ij},3,2,5,7,6,4_p]
   $$
   We select 4 as the pivot of the array, and iterate i and j from 0 to n-1 inclusive.

   Now, since 1,3,2 are less than 4, we will get 3 comparisons and i and j will move to the element 5
   $$
   [1,3,2,5_{ij},7,6,4_p]
   $$
   Now, since 5,7,6 are greater than 4, j will move to 4 and break the loop while i stays at 5 and pivot 4 is swapped with 5 leading to subarrays [1,3,2] and [7,6,5] - which are 3 comparisons again. Total 6 comparisons right now.

   

   Now in the left subarray, 2 is the rightmost element and hence the pivot and we initialize i and j at the position of element 1. Next, we compare with pivot 2 with 1 and since 1 is lesser, i and j move to 3. Since 3 is greater, only j moves to 2 and then the loop is broken, leading to 2 comparisons and singular elements [1] and [3] which are also already sorted. 

   Next on the right subarray, 5 is the rightmost element and since both 7 and 6 are greater than 5, 2 comparisons are made and i stays at 7 while j moves to 5. Pivot 5 is then swapped with 7 which leads to [6,7] as the subarray which is 1 comparison leading to 6 and 7 being led to their correct positions.

   Total comparisons: 3+3+2+2+1 = 11 comparisons.

   

Hence anytime we move the elements 2, 4 and 6 from their indexes, there will always be more comparisons. Hence proved.

## (d) Let A be an array with $n = 2^k − 1$ elements, where k is some positive integer. Determine a formula (in terms of n) for the minimum possible number of total comparisons required by Quicksort, as well as a formula for the maximum possible number of total comparisons required by Quicksort. Use your formulas to show that the running time of Quicksort is $O(n log n)$ in the best case and $O(n ^2 )$ in the worst case.

We are given the array :

$A[2^k-1]$, where $2^k-1 = n$  which is the number of elements.

Let us first consider the worst case scenario : where you require maximum amount of comparisons.

The maximum number of comparisons shall occur when there is the highest amount of difference between the sizes of both the subarrays. This means, the left subarray = n-1 of the previous array, and the right subarray size of 0 and it does not exist. Conversely, it may also be the left subarray not existing. 

This will happen in a case when (a) array is already sorted in a manner (b) all elements are the same. 

We can already calculate the complexity of comparing 2 elements, which is O(1). 

Suppose we have a function $F(n)$ that counts the total number of comparisons given the size of the array. In the worst case, the subarray's size is $n-1$. The total work done for comparing should be the work done in the current iteration + the work done in the next iterations.

Hence $F(n)$ becomes:
$$
F(n) = F(n-1) + (n-1)
$$
We can expand this series again:
$$
F(n-1) = F(n-2) + (n-2)\\
F(n-2) = F(n-3) + (n-3)\\
F(n) = F(n-3) + (n-3) + (n-2) + (n-1)\\
\dots\\
F(n) = (n-k-1) +...+ (n-3) + (n-2) + (n-1)
$$
 

Now, since at the elementary level, n-k-1 would be equal to 1 as our base case :
$$
n = k+2
$$
Which means the equation becomes:
$$
F(n) =  (1+2+\dots+(k+1))+((k+1)+(k+1)+...[n\ times])\\
F(n) =  (1+2+\dots+(k+1))+((k+1))*n\\
\because n = k+2, \\
\Rightarrow -(1+2+\dots+n-1)+ (n-1)*n\\
\Rarr (n-1)*n/2\\
$$


**Hence the worst case or maximum number of comparisons take $O(n^2)$ time since we compare elements approximately $n^2$ times.**



Let's calculate the best case:

For the minimum number of comparisons to be achieved the arrays should be sorted into two subarrays of size n/2 everytime.

Hence, the number of comparisons can be represented by the function $F(n)$

$F(n) = 2(n/2) + (n-1)$

We can apply advanced masters theorem since $T(n) = F(n)*O(1)$. 

Applying advanced masters theorem on this we will have $T(n) = aT(n/b) + \Theta(n^klog^pn)$

Since a = 2, b = 2, k = 1, p = 0 (since the other term is n-1),

We can apply the second case of the advanced masters theorem on this:

$F(n) = \Theta(n^{log_22}log_2n)\Rarr \Theta(nlogn)$

Hence, $T(n) = \Theta(nlogn)$ as well.

Since that is tight bound, so the minimum number of comparisons lead to $O(nlogn)$ Big-oh bound as well.

Hence proved for both conditions.



# 2(a)

![image-20231013230302932](C:\Users\harry\AppData\Roaming\Typora\typora-user-images\image-20231013230302932.png)

For the first problem I did "[4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)". ![image-20231013230427640](C:\Users\harry\AppData\Roaming\Typora\typora-user-images\image-20231013230427640.png)

For the second problem I attempted [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

# 2(b)

   Here's my solution to Count of Range sum.

```py
class Solution:
    def mergesum(self, sum, lower, upper, low, high):
        if high - low <= 1:
            return 0

        mid = (low + high) // 2
        m, n, count = mid, mid, 0

        count = (
            self.mergesum(sum, lower, upper, low, mid) +
            self.mergesum(sum, lower, upper, mid, high)
        )

        for i in range(low, mid):
            while m < high and sum[m] - sum[i] < lower:
                m += 1
            while n < high and sum[n] - sum[i] <= upper:
                n += 1
            count += n - m

        sum[low:high] = sorted(sum[low:high])

        return count

    def countRangeSum(self, nums, lower, upper):
        length = len(nums)
        sum_array = [0] * (length + 1)

        for i in range(length):
            sum_array[i + 1] = sum_array[i] + nums[i]

        return self.mergesum(sum_array, lower, upper, 0, length + 1)

        
    
```

Here, in the `mergesum` function, recursively processes the partition of the two halves, hence the complexity of this is on the order of $logn$ because of the depth of the recursive tree formed.

Within the `mergesum` function, there's a loop that iterates through the elements in the range, and for each element, there are two while loops (`while m < high` and `while n < high`). The time complexity of this part is $O(n)$. Hence it is multiplied over all the recursive calls hence it becomes $O(nlogn)$. 

For the `countRangeSum` function:

- We first calculate the prefix sum of the input array, which takes O(n) time.
- Then, we call the `mergeSort` function, which itself has a time complexity of $O(n log n)$.
- So, the overall time complexity of the `countRangeSum` function is $O(n + n log n) = O(n log n)$.

# 2(c)

For this problem I attempted [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/). This problem allowed me to stumble through the various methods I could play around with recursive calls to my function. 

Initially, on my first attempt, I tried to split up the two arrays to find the median of the subsequent subarrays - however, this proved to be futile since both the subarrays were already divided and I did not understand how to consider both the arrays medians at the same time. However, **Hakshay Sundar** helped me with the thought process behind solving this problem. Together, we understood that since both the arrays are already sorted, it is similar to the last step of merge sort. In the last step of merge sort, we merge the solutions together and both the arrays are sorted arrays. This worked however this turned a time complexity of O(m+n) and not O(log(m+n)) which is mandated for a correct solution . Hence, we had to rethink the problem again to incorporate binary search into the mix. This involves understanding that the left array or nums1, must always be smaller than the right array, nums2 - allowing us to perform binary search through 0 to n = len(nums1). This allowed for a O(log(n+m)) solution. 
