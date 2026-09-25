## 1. The Core Concept (What is this?)
    The concept revolves around intelligent reversal of the array in-place.

## 2. Architectural Trade-offs
* **Approach A:** First reverse the entire array. Then reverse the first part starting from 0 till `k - 1`. Lastly, reverse the second part, starting from `k` till the end.
* **Approach B:** 

## 3. Insights
* **Insight A:** 
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember to take a modulus of `k` by the length of the array. This is to ensure that the rotation covers the entire array in multiple loops.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 