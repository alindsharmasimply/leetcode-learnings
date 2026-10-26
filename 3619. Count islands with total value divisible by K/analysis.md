## 1. The Core Concept (What is this?)
    Simple use of DFS to traverse the graph.

## 2. Architectural Trade-offs
* **Approach A:** Use directions in all four coordinates. The total sum calculation is done using recursively calling the `dfs_sum()`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(m x n); Space Complexity: O(m x n) in the worst-case scenario for the recursion stack if a single island covers the entire grid.
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember to mark the visited cell as `0` during the traversal.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 