## 1. The Core Concept (What is this?)
    Everything depends on the index of the number `0`.

## 2. Architectural Trade-offs
* **Approach A:** 
    • Case 1: Array is Cyclically Increasing (is_inc)
        • Direct Rotate (index_of_zero ops): Left-rotating index_of_zero times moves 0 from index index_of_zero to index 0.
        • Reverse-Rotate-Reverse (2 + n - index_of_zero ops): Reversing once flips the order. Rotating aligns it, and a second reversal restores the increasing order.
    • Case 2: Array is Cyclically Decreasing (is_dec)
        • Rotate-Reverse ((index_of_zero + 1) % n + 1 ops): Move 0 to the last position of the array via left rotation, then reverse once to sort it.
        • Reverse-Rotate (n - index_of_zero ops): Reversing first moves 0 to n - 1 - index_of_zero. Then, rotating brings 0 directly to index 0.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 