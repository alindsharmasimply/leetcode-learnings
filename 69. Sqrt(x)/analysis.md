## 1. The Core Concept (What is this?)
    Use of Binary Search.

## 2. Architectural Trade-offs
* **Approach A:** Since guessing every number as the square root is not optimal hence we use binary search method. The root would exist only between numbers `1` and `x`. We can find out if `mid * mid` equals `x`, less than `x` or greater than `x`. Since we need a floor value (rounded down) we'll always keep the `ans` stored when we see that the mid-product is less than `x`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(log x); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember the edge case when `x` is less than 2. Return `x` itself in this case.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 