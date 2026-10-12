## 1. The Core Concept (What is this?)
    There is a usage of Binary Search but it is not intuitive at all.

## 2. Architectural Trade-offs
* **Approach A:** The median splits a single sorted array into two equal halves: a Left Half (smaller elements) and a Right Half (larger elements).
    When we have two sorted arrays, nums1 `size(m)` and nums2 `size(n)`, our goal is to split both arrays simultaneously into a combined Left Part and a combined Right Part such that:
    1. Equal Size: The total number of elements in the Left Part equals the total number of elements in the Right Part (or is exactly one greater if the total count is odd).
    2. Perfect Ordering: Every element in the Left Part is less than or equal to every element in the Right Part.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(log(min(m, n))); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 