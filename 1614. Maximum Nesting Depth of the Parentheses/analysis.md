## 1. The Core Concept (What is this?)
    Simple usage of keeping track of the number of open brackets at a time.

## 2. Architectural Trade-offs
* **Approach A:** This was the first approach that came to mind. Use stack to push `(` into it (whenever encountered). When `)` comes then get the size of the stack and use it for max_depth. But this approach uses unnecessary space.
* **Approach B:** In this approach we just maintain the count of open brackets by incrementing by 1 everytime `(` is encountered and decrementing by 1 everytime `)` is encountered.

## 3. Insights
* **Insight A:** First approach, time complexity: O(n) and space complexity: O(n)
* **Insight B:** Second approach, time complexity: O(n) and space complexity: O(1)

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 