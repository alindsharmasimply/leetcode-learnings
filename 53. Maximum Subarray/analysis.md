# DSA / Leetcode / Maximum Subarray

## 1. The Core Concept (What is this?)
    An array consisting of integers (including negative ones) and we have to find the maximum subarray sum.

## 2. Architectural Trade-offs
* **Approach A:** Kadane's algorithm works the best here. Iterate through the entire list while comparing the maximum of (the current number) and (the sum_till_now + the current number). Which becomes the next sum_till_now.

## 3. Insights
* **Insight A:** Takes only O(n) time complexity and O(1) space complexity.

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* https://walkccc.me/LeetCode/problems/53/?h=53.#approach-2-o1-dp