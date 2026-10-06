## 1. The Core Concept (What is this?)
    Simple concept of counting the left and right parenthesis.

## 2. Architectural Trade-offs
* **Approach A:** Whenever we encounter `(` it means that we now await a closing parenthesis so we increment the `left` counter. But whenever we encounter `)` it means that we can either close an existing open parenthesis or, if there's none available, just increment the `right` counter. Hence the condition of checking `if left == 0`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n) and Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 