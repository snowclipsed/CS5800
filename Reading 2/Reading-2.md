# Reading 2

## Problem 1) Provide a summary of your understanding of recurrence ( what recurrence is, how to solve recurrences and give an example).


Recurrence implies repetition. In algorithms, recurrence is the process of repeatedly applying a function to break down a problem into smaller sub-problems till a *base case* is reached. A base case is the point where the recurrence terminates ; i.e.; the recurrence function does not call itself anymore. It *usually* is represented by a case that is elementary in nature and cannot be further broken down into sub-cases.

A recurrence equation is a mathematical representation of a recurrence condition. This equation defines a function which is defined in terms of their previous values. Recurrence equations are widely used during algorithmic analysis of recurrence based algorithms, specially divide and conquer algorithms.

It is necessary to determine whether the problem can be broken down into smaller instances of the same problem in order to formulate a recursive problem.
Conquer the subproblems by solving them recursively. Solve the subproblem on reaching the base case, then combine the subproblem solutions to get the answer to the original problem.

An example of a recurrence equation is $T(n) = 2T(n/2)$. This equation is balanced, as in it divides the input problem into an equal number of subproblems. We can visualize this through a recurrence tree which are the same in value.

As we can see, each node is divided into 2 child nodes

However, recurrence equations can also be 'unbalanced' or produce subproblems that are inequal. An example of such an equation is S

## Problem 2) Give an example of a recurrence equation from a problem that you have studied (e.g Convex Hull, Quicksort, Matrix Multiplication etc) and show how this is solved using:

 ###  	1. Recursion tree

Let's consider merge sort, whose recurrence equation we are familiar with : 

$T(n) = 2T(n/2) + O(n)$

This means the tree has a branching factor of 2 (splits into 2 parts on each level) and splits into children of n/2 the original parent. We can draw the tree as following:

![image-20231010190132162](C:\Users\harry\AppData\Roaming\Typora\typora-user-images\image-20231010190132162.png)

Now, we can see that at level k, we reach our base case.

Hence :
$$
\frac{n}{2^k} = 1 \\ 
\Rarr n = 2^k \\
k = log_2n\\
$$
$T_c = I_c+L_c$ Where $I_c$ = branch complexity and $L_c$ = leaf node complexity.
$$
I_c = \sum_{i=0}^{k = log(n)-1} 2^i(\frac{n}{2^i}) = n(logn-1) = nlogn - n \\
L_c = 2^k(\frac{n}{2^k}) = n\\
T_c = nlogn - n +n = nlogn\\\\
T(n) = O(nlogn)
$$


### 	2. Master Theorem

Let us consider merge sort for this problem.

From Page 74 of CLRS, we know the recurrence equation for merge sort is : 
$$
T(n) = 2T(\frac{n}{2})+O(n)
$$
We have a generalized recurrence equation of the form : 
$$
T(n) = aT(n/b) + f(n)
$$
To apply master theorem we must find out the variables $a$ and $b$ as well as $f(n)$.

Comparing our recurrence equation for merge sort we can identify $a=2$, $b =2$, and $f(n) = n$.

Now applying master theorem, we have $log_ba = log_2(2) = 1$

Since $n^{log_ba}= n^{log_2(2)} = n$, which is also equal to $f(n)$.

Hence case 2 of the master theorem applies and $T(n) = \Theta(nlogn)$.

## Problem 3) Provide a quick review of Selection, Insertion, Merge sort and quick sort and provide a summary of the O, Omega and Theta asymptotic running times. These could come from your reading , you do not need to compute them.

The O-notation indicates an upper bound on a function's asymptotic behavior. Implying that a function's growth rate is constrained and cannot surpass a certain level. The rate is determined by its highest-order term.
The Ω notation represents a lower bound on the asymptotic behavior of a function. In other words, the notation indicates that a function grows at least as fast as a specific rate. The rate is based on the highest-order term.
The θ notation describes a tight bound on a function's asymptotic behavior. It indicates that a function grows exactly at a particular rate, which is determined by the highest-order term.
