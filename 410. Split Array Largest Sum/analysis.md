## 1. The Core Concept (What is this?)
    Using the Binary Search Concept.

## 2. Architectural Trade-offs
* **Approach A:** For a given `mid`, we iterate through nums and greedily pack elements into the current subarray. If adding the next element exceeds `mid`, we start a new subarray and increment our count. If the total number of subarrays needed is `<=k`, then `mid` is feasible, and we can try searching for a smaller maximum sum. Otherwise, `mid` is too small, and we must increase our lower bound.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(nlog(sum(nums) - max(nums))) where `n` is the length of nums. Binary search takes logarithmic steps and the greedy check takes O(n) time.
* **Insight B:** Space Complexity: O(1)

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 