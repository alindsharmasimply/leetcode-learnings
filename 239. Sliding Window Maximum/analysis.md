## 1. The Core Concept (What is this?)
    The intuition of using a deque is very unclear but still we have to go with it.

## 2. Architectural Trade-offs
* **Approach A:** 
    Declare a `deque()` which will be storing the indices in a monotonic decreasing format i.e., the index on the 0th element will be the largest. There should be two pointers initially pointing at `0`. Now traverse the entire array one by one. First step is to ensure that we remove(pop) all the indices whose elements are less than the current element from the `deque()`, starting from the end of the `deque()`. Then append the current element's index in the `deque()`. Now check for the out-of-bounds index in comparison to the `left` pointer and popleft(). Finally if the window is complete for the first time then add the 0th element to the `results` list and increment the `left` pointer.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n), Space Complexity: O(k)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 