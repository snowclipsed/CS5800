We can multiply $T(n)$ by the constant c and find the recursion tree without including the C(n) term everytime.

![image-20230929220703789](C:\Users\harry\AppData\Roaming\Typora\typora-user-images\image-20230929220703789.png) 

For each level, we can calculate the total cost. Then, we can add the costs from all levels to find the final cost.

for the zeroeth level, the cost is $c(n)$

for first level, the cost is $c(n-a) + c(a)$

similarly,

for the k-th level, the cost is $c(n-ka)+kc(a)$

$T(n) = \sum^{i=k}_{i = 0}c(n-ia)+ic(a) = \sum^{i=k}_{i = 0}c(n) = cn^2/a - n/a = O(n^2)$

