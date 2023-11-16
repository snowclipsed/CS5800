## Q3

5 Points

Grading comment:

A binary heap is called a `max heap` if it has the property that for every node �*i* other than the root, the value of the node is at most the value of its parent. 

Here is an example of a max heap with 1010 nodes (i.e., 1010 elements), presented both as a binary tree and as an array.

![binaryHeap_example.png](https://production-gradescope-uploads.s3-us-west-2.amazonaws.com/uploads/text_file/file/265924628/binaryHeap_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAV45MPIOW3AZKGYPQ%2F20231029%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231029T015946Z&X-Amz-Expires=10800&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDne5TB1Z%2FmKkoeOSILV5sc0ykh%2Fc0jcqqkAeHHcsu42AiBARvKXQ1P0b0eyDJEQn03Yc58U9fUxZHpLgzrutFCrEyrDBQiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDQwNTY5OTI0OTA2OSIMqQX3O4EBLvU2rAijKpcFROh0%2F7HiHjRSl0waBBfQRANTWWc2Y4f6o1ZVda85LQWeoxTMMfQWl56QZfvYw2oIOs06Nyx2i7eof3RSal3fnQ1cVrnTaO81pLLEHBmm4H7C1c4MgV7bELmQfu3%2BljtA%2Bv9%2BFLPpty0cd8MmaZRUxAEW3YK0RtmG9dgOI8FpZCWHcQQn4J9gLd621kjZQMFDxYPkawjTO1JUDTaDxHPCDsPC5BRA9v98Lko4L2tMntCRwzDqOZm3n8HnBax5B6iSTFPnQ%2F1ZbKU%2BJbbG%2B4zNghSSmGXkGu8UsB%2BONU1Y5s%2FWmiX5UK%2FZXCNFkt7DB84NX95THy6R7mkUfNuHSouG6JpAR6u4To6HDeVC%2BY9E%2Bj4ol7tsbd0xc6gf1gbfJ8eyQwJubGnc1tRCQv08Rq%2B1rzZn1iA3rouM0cPxE%2BbI5c0vlv6l9xoTeMYv4dZMOf6lJp8bi8CJQWxk4coIrJlKsv2q5fpB2bF5pRFXgDLlMIJ%2FWyVtrEWiaWOx5Q9FBLXVp22SP86y%2FH8vrYZfSoMOrpVnr0GPRWYa3h1gu0MKBk8JDN055oIevlEntM%2BM8pB0qHObvfS25athf0XgYTrSMC7gLhbnR72QYHbXQEvgu6I89y07WMOxpL1p4sD2WREXdRvQNuDf7iDyyQdNocK1Jxu5Rkftom5%2FUGXLRNJ5lUc0SXQ2%2FBxW8HBAiOIXJlMHPS%2FZIs7JRehTh%2B7IgbV9iOLl5VqwQ6GcGgXy9dtZdiqPxbFKkM3eQ9TU6HIozNtyP9zfGx8C8PHbiRbxb%2FLkp8O8xZYWW55fC2ndZS65hPW1zR6BvRn%2F5%2BWN%2FhK%2FxGWPhPLqeOesXKD4Mbndynz1dndgpNStYQg8fE9yvRqHmAy0lZnuNXj1MJ%2Ft9qkGOrIBhk1%2BSdNBnIsAideK3mqKQacLCrCTnpOb904YL%2BrAtp6K%2B6sqJPorRM%2B13obMm2GD2j7dA%2FvfMO6ghQr2uf0fNkF3zOqPF99o%2BPivQpfU%2Fbta85ulHNJblRzaoIefoL5Yzz1sWn0x5XpyuF7fKoBKdc9tRGaedOM1X%2Bzo9LNMdTGZlruXRkSWoeLFCaxZNwbtIRECShFJc%2FXgDTyAX55l37Qy55%2Byy2Hnw9yxuA8%2B3uYmuA%3D%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=d2c9a2f2252f2112763576c62e30de455b2212799be9f316cb36cc43e77f6d4d)



The height of a heap is defined to the number of edges on the longest downward path from the root node to a leaf node.  Thus, in the example above, the height of the heap is ℎ=3. 

If a (binary) heap has height ℎ=6, determine the minimum number and maximum number of elements that can be in this heap.  Clearly justify your answer.

**Solution 3(a):**

Since the heap is a binary tree, a perfect binary tree will be the condition when a heap contains the maximum amount of nodes. Number of nodes in a perfect binary tree are $2^{h+1}-1$.

Since $h=6$, this is equal to $2^7 - 1= 127$

Hence the maximum number of nodes in a heap of height 6 is 127.

The minimum number of nodes must be when there is 1 leaf in the last level. This equals to the height of a perfect tree with $h-1$ leaves -1 +1 = height of a tree with $h-1$ leaves, which is equal to $2^h-1$.

Hence, when h = 6, the minimum number of leaves is $2^6 -1 = 64$.

 

