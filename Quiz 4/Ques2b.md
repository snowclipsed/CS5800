Starting with vertex s, we can use a search algorithm to pass through all nine vertices in this graph.  Whenever we have more than one option, we always pick the vertex that appears earlier in the alphabet.

For example, from vertex s, we go to a instead of c, since the letter a appears before the letter c in the alphabet.

<img src="C:\Users\harry\AppData\Roaming\Typora\typora-user-images\image-20231028223539007.png" alt="image-20231028223539007" style="zoom:50%;" />

Determine the order in which the nine vertices are reached using Breadth-First Search (BFS)

First, we start from the node S. 

We initialize queue Q:
$$
[A]
$$


Then, we visit A. We push C,B,D to the queue:
$$
[C,B,D]
$$
We visit C, popping it from queue. We add F since it shares an edge with C.
$$
[B,D,F]
$$
We visit b, popping it. We add E to queue.
$$
[D,F,E]
$$
We visit D, popping it. We add g to the queue.
$$
[F,E,G]
$$
We visit F, popping it.
$$
[E,G]
$$
We visit E, popping it, We add h to the queue.
$$
[G,H]
$$
We visit G and H, popping them.
$$
[empty]
$$
The order is :
$$
s,a,c,b,d,f,e,g,h
$$
