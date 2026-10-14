## 1. The Core Concept (What is this?)
    Use of stack to store the indices.

## 2. Architectural Trade-offs
* **Approach A:** Iterate through the temperatures array with index i from 0 to N - 1:
	• While the stack is not empty and the current temperature temperatures[i] is greater than the temperature at the index stored at the top of the stack (temperatures[stack.top()]):
		• Pop the index (prev_index) from the stack.
		• Set answer[prev_index] = i - prev_index.
	• Push the current index i onto the stack.
* **Approach B:** 

## 3. Insights
* **Insight A:** • Time Complexity: O(N) — Each index is pushed onto the stack at most once and popped at most once, resulting in a linear scan.
    • Space Complexity: O(N) — In the worst-case scenario (e.g., strictly decreasing temperatures), all indices are stored in the stack at the same time
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 