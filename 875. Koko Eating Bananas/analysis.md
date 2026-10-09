## 1. The Core Concept (What is this?)
    If we look at this closely, it's a Binary Search Problem.

## 2. Architectural Trade-offs
* **Approach A:** We need to think about what is the lowest rate Koko can eat the bananas i.e., `1` and the highest rate i.e., `max(nums)`. Now these two become the low and high points of the binary search space.
    If Koko is able to eat the bananas in `k=5` then she will be able to eat them in `k=6,7...` as well. Hence we'll need to go towards the left search space to find out the minimum number of hours possible.
    The ceiling value should be taken when we divide every pile with the `mid` element.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(nlog(m)), where `n` is the number of piles and `m` is the maximum number of bananas in a single pile. The binary search takes `log m` steps. In each step, we iterate through all `n` piles to calculate the total hours.
    Space Complexity will be just O(1).
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember that here the starting index (low) should be 1 and not 0.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 