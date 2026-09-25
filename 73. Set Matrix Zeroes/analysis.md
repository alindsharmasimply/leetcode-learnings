## 1. The Core Concept (What is this?)
    The idea is to use the first row and column of the matrix for storing/marking which row and column has a zero.

## 2. Architectural Trade-offs
* **Approach A:** First check if there is even a single zero in the first row and column and accordingly store this knowledge in boolean variables. Then go through the entire matrix but the first row and column. While traversing keep checking for a zero. When found, mark the particular first row's column as well as first column's row as zero too. Traverse once again the entire matrix except the first row and column and this time update the value of every cell which has either the first row's column or first column's row as zero. Finally, using the earlier stored boolean flags either fill or don't fill the first row or column or both with zeros.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time complexity is O(m*n) and Space Complexity is O(1).
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 