## 1. The Core Concept (What is this?)
    Onion layer peeling is the more intuitive solution.

## 2. Architectural Trade-offs
* **Approach A:** Start with top and bottom layers. The outer loop will be responsible for reducing the layer from the outside, iteration by iteration. The inner loop will circle around the outer layer element by element. First iteration -> corner elements, second iteration -> adjacent corner elements, third iteration -> adjacent to adjacent corner elements and so on. An extra variable is used to store the first element. Once the outer layer is covered then the layer is shrinked to the penultimate layer and so on. [Recommended Solution]
* **Approach B:** The second approach is a little bit rote learnt one. First get the transpose of the matrix and then reverse every row of the transposed matrix. 

## 3. Insights
* **Insight A:** Time Complexity is O(m.n).
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 