## 1. The Core Concept (What is this?)
    This looks very simple but need to watch out on the edge conditions.

## 2. Architectural Trade-offs
* **Approach A:** The approach is to sort, then fix one point and incorporate 2-pointer sliding window in the remaining elements.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n^2) and Space Complexity: O(n) [Since, Python's Timsort uses up to O(n) space]
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember to skip the iteration where the current element is equal to the previous (for `i` and `left`) or next (for `right`) element. Because that would already have been counted and hence will result in duplicate lists in the final list.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 