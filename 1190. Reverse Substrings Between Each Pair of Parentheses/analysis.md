## 1. The Core Concept (What is this?)
    Use of stack would be needed at all costs. The Brute force solution looks more intuitive.

## 2. Architectural Trade-offs
* **Approach A:** Here we play with lengths of the answer list. Which means that these lengths would become the starting index of the elements of the list to be reversed. First, traverse through the string. On encountering a `(`, push the current length of the `ans` list. On encountering a `)`, pop the stack and this popped value becomes the starting index for reversal. On encountering anything else, just append that character at the end of the `ans` list.
* **Approach B:** The optimized approach is usage of Wormhole strategy. Here we maintain indices of the `(` in order to record the teleport opening:
- When we are walking through the string and hit an opening parenthesis `(`, we instantly teleport to its matching closing parenthesis `)`.
- When we teleport, our walking direction reverses (if we were moving forward, we now move backward, and vice versa).- We only record normal lowercase characters when you encounter them.

## 3. Insights
* **Insight A:** First approach is brute force and requires Time Complexity: O(n^2) and Space Complexity: O(n).
* **Insight B:** Second approach is optimal and requires Time Complexity: O(n) and Space Complexity: O(n).

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 