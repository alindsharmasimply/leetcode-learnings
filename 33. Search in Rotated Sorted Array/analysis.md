## 1. The Core Concept (What is this?)
    Simple use of binary search but keeping in mind only the sorted section of the array and not the one where the pivot is situated.

## 2. Architectural Trade-offs
* **Approach A:** The conditions for incrementing or decrementing the `left` and `right` pointers would become a subsection for the sections when `nums[left...mid] are sorted` and when `nums[mid...right] are sorted`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(log(n)); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 