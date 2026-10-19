## 1. The Core Concept (What is this?)
    

## 2. Architectural Trade-offs
* **Approach A:** The key idea is to iterate through the string, build multi-digit numbers, and use a stack to defer addition and subtraction while resolving multiplication and division immediately.
    • +: Push the number onto the stack.
    • -: Push the negative of the number onto the stack.
    • *: Pop the top element, multiply it by the current number, and push the result back.
    • /: Pop the top element, divide it by the current number (truncating toward zero), and push the result back.
    • Finally, sum all elements left in the stack.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(n)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 