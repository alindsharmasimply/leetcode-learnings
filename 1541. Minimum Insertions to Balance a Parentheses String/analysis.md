## 1. The Core Concept (What is this?)
    Simple counting of left and right parenthesis.

## 2. Architectural Trade-offs
* **Approach A:** There would be 3 variables to store counts: `needed_right`, `missing_right` and `missing_left`. 
    1. The `needed_right` would be incremented by 2 when we encounter a `(`.
    2. The `missing_right` would be incremented by 1 for each missing `)`.
    3. The `missing_left` would be incremented by 1 for each missing `(`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 