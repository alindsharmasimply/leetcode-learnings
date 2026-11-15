## 1. The Core Concept (What is this?)
    The concept is not at all intuitive. One can understand that prefix sum is to be used but the parity concept is difficult to grasp and understand.

## 2. Architectural Trade-offs
* **Approach A:** Any subarray sum from index `i` to `j` can be expressed as the difference between two prefix sums. Basic arithmetic rules for parity tell us when this difference is odd:
    • Even − Odd = Odd. If our current running prefix sum is even, subtracting any earlier odd prefix sum leaves an odd subarray sum.
    • Odd − Even = Odd. If our current running prefix sum is odd, subtracting any earlier even prefix sum leaves an odd subarray sum.
    This is the reason why we add the opposing counts to the `total_subarrays`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** One needs to remember the count of `0` in the `even_count`.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 