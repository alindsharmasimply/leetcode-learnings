## 1. The Core Concept (What is this?)
    The idea is of a bucket sort. 

## 2. Architectural Trade-offs
* **Approach A:** Create multiple buckets(lists) within one list. The indices of these buckets are supposed to be the counts of the numbers. Just iterate this list from the back and stop when the 'k' threshold is crossed.
* **Approach B:** 

## 3. Insights
* **Insight A:** In worst case, the max length of the buckets' list would be of the length of the entire 'nums' array.
* **Insight B:** Time and Space Complexities will be both O(n).

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 