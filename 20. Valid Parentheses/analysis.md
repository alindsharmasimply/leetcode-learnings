## 1. The Core Concept (What is this?)
    This is a simple problem but only have to be careful about the edge cases.

## 2. Architectural Trade-offs
* **Approach A:** Simply append every opening parenthesis to a stack one by one. If ever encounter a closed parenthesis then pop from the stack and compare it. A good way to compare is to use a constant dictionary for the parenthesis. In the end return True/False based on the final length of the stack.
* **Approach B:** 

## 3. Insights
* **Insight A:** 
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** If length of the string is less than 2 then obviously it's not a valid one because the constraints tell that the length of the string will be atleast 1.
* **Gotcha 2:** Another edge case is when the stack is empty and the current character being read is not an opening parenthesis. Here too we'll return `False`.

## 5. Deep-Dive References
* 