## 1. The Core Concept (What is this?)
    The concept is of a sliding window and a look-up memory. There are two methods of this look-up memory.

## 2. Architectural Trade-offs
* **Approach A:** In this approach we simply use a `set()` which only let us know if a certain character at the `right` pointer index has been seen before. On the basis of that, a while loop will run till the point where it arrives and keep incrementing `left` pointer to that point.
* **Approach B:** In the second approach instead of a set we use a dictionary that stores the character's last seen index. Hence now there is no need to run the while loop everytime a character has been seen earlier. Now we can just set `left` as the found `index + 1` thereby optimizing the algorithm. [Recommended]

## 3. Insights
* **Insight A:** First Approach: Time Complexity: O(n) and Space Complexity: O(26)
* **Insight B:** Second Approach: Time Complexity: O(n) and Space Complexity: O(26)

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 