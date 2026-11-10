## 1. The Core Concept (What is this?)
    Two pointer approach would be used.

## 2. Architectural Trade-offs
* **Approach A:** First let the `fast` pointer reach the nth point. Then traverse both `slow` and `fast` pointers simulataneously in order to make `slow` pointer reach the node just before the node to be deleted.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(1)
* **Insight B:** In Python, our code is actually complete and correct as written because Python handles memory management automatically. We do not need to explicitly delete the node or free memory. Python's garbae collector automatcally frees the memory behind the scenes.

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 