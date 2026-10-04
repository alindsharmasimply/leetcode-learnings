## 1. The Core Concept (What is this?)
    This one is very similar to other sliding window problems.

## 2. Architectural Trade-offs
* **Approach A:** Just use left and right pointer to ensure the window size. Here a dictionary is not needed since only two numbers(0 & 1) are needed to be counted, hence take only two count variables. Increment their values on conditional basis while traversing the `right` pointer in a loop. Whenever the sum of the above counts becomes greater than `k` it's time to move the `left` pointer. Keep moving it and reducing the respective counts of ones and zeros as long as it takes to have enough for a valid window size.
    And finally we just keep track of the `max_length`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n) and Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 