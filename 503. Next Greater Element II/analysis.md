## 1. The Core Concept (What is this?)
    A stack would be used to store indices.

## 2. Architectural Trade-offs
* **Approach A:** 1. First this needs to be a double-pass algorithm hence we need to iterate the entire list twice.
    2. We need to ensure that we access the list items by taking a modulus of the range by the total length `n` of the list. Any elements' indices would be popped from the stack only when the topmost is less than the current one. We would use this popped index as the current number.
    3. Then lastly, we only push to the stack if the current range is less than `n` which means that we push only during the first pass.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(n)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember that the output array should be initialized with `-1`. This would take care of the items for whom there is nothing greater.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 