## 1. The Core Concept (What is this?)
    The concept is that of Binary Search only.

## 2. Architectural Trade-offs
* **Approach A:** Finding the first index and the last index would be taken as two separate operations.
    1. Finding the first index would ensure that we try to keep moving the `mid` towards the left direction.
    2. Finding the last index would ensure that we try to keep moving the `mid` towards the right direction.

    In both the cases, whenever we encounter equality with the `target` we just store the index.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(log(n)), Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 