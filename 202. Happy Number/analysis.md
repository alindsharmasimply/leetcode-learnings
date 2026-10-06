## 1. The Core Concept (What is this?)
    The key is the Detection of a loop whether n is a magic number or otherwise.

## 2. Architectural Trade-offs
* **Approach A:** Take one `slow` and one `fast` pointer. The slow pointer will only do squared_sum once and the fast pointer would do it twice. Run this loop till they both become equal. Either they will end up on a number if `n` is not a magic number or they would both reach `1`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(log n), Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 