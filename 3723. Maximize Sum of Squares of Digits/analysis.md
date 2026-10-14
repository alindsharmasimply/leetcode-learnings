## 1. The Core Concept (What is this?)
    We'll use greedy approach here.

## 2. Architectural Trade-offs
* **Approach A:** 
    • A larger digit contributes exponentially more to the sum of squares (9² = 81, 8² = 64, etc.) than smaller digits combined. Thus, we should place as many '9's as possible.
    • If num * 9 < sum_val, it is impossible to form a number of length num with digit sum sum_val, so we return "".
    • We extract a quotient and remainder to find how many 9s we can make and what the remaining digit should be.
    • We fill the remaining positions with 0s to meet the exact length num while keeping the highest possible number value.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(num), Space Complexity: O(num) since we store the output string.
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember the edge case condition that the `sum` should lie under the max 9's quotient limit.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 