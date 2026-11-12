## 1. The Core Concept (What is this?)
    Simple counting of max length.

## 2. Architectural Trade-offs
* **Approach A:** Everytime a particular element is not greater than the previous element, reset the `increasing_count` and similarly everytime a particular element is not less than the previous element, reset the `decreasing_count`. In case of equality reset both the counts.
    On every iteration, keep recording the max value of the either of the counts.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 