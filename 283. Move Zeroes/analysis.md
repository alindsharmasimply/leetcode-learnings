## 1. The Core Concept (What is this?)
    Simple swap_pointer strategy.

## 2. Architectural Trade-offs
* **Approach A:** Use Slow Pointer and Fast Pointer. Swap everytime a non-zero element is encountered and increment the `swap_pointer`. Everything gets completed in a single pass.
* **Approach B:** There is also a two-pass approach given online which first assigns non-zero numbers to the initial part of the array and then assigns zeros to the remaining places in the second pass.

## 3. Insights
* **Insight A:** Time Complexity: O(n), Space complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 