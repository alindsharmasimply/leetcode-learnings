## 1. The Core Concept (What is this?)
    Use the Binary Search Pattern.

## 2. Architectural Trade-offs
* **Approach A:** Although the approach is that of Binary Search but the determination of the row and column is something worth paying attention to. `left` would be 0 and `right` would be the last element in the last row of the last column. Now, just to determine the comparison position we need to divide `mid` by `n` for row and mod `mid` by `n` for column.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(mxnlog(mxn)); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 