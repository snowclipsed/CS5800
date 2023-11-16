Starting with vertex s, we can use a search algorithm to pass through all nine vertices in this graph.  Whenever we have more than one option, we always pick the vertex that appears earlier in the alphabet.

For example, from vertex s, we go to a instead of c, since the letter a appears before the letter c in the alphabet.

<img src="C:\Users\harry\AppData\Roaming\Typora\typora-user-images\image-20231028223539007.png" alt="image-20231028223539007" style="zoom:50%;" />

Determine the order in which the nine vertices are reached using Depth-First Search (DFS)

First, we start from the node S. 

Then in the next step, we will visit a since it is alphabetically smaller than c. 

Then, we visit b since it is alphabetically smaller than d (b<d).

Then, we visit e. After that, we visit d since d<h. 

Then, we visit c since c<g. 

Then we visit f since S is already visited. 

Then we visit g because that is the only path ahead.

Similarly we visit h.

Hence the answer is **s,a,b,e,d,c,f,g,h**.