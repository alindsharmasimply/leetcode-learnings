## 1. The Core Concept (What is this?)
    The approach is to have maximum heights from the left as well as the maximum heights from the right. The max heights are supposed to show the maxes at every point.

## 2. Architectural Trade-offs
* **Approach A:** Traverse the heights and at every point fetch the minimum out of the left_max and right_max and then subtract the height at that point.
* **Approach B:** In the second approach, instead of taking two arrays we can just take two variables that will track the tallest bar so far.

## 3. Insights
* **Insight A:** Time and Space Complexity: O(n) and O(n)
* **Insight B:** Time and Space Complexity: O(n) and O(1)

## 4. The Pitfall Log
* **Gotcha 1:** In the second approach it's important to remember that there is an edge case of no heights to handle as well.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 