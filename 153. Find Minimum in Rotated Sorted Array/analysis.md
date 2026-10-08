## 1. The Core Concept (What is this?)
    Concept of Binary Search.

## 2. Architectural Trade-offs
* **Approach A:** We need to ensure that our comparisons of `mid` are always with `right` pointer to figure out which half of the array is "broken" (unsorted) and where the pivot/minimum must live.
    1. Case 1: `nums[mid] > nums[right]`
        This means that because the middle element is greater than the rightmost element, the "drop" (pivot/minimum) must be in the right half. [Here we discard the `mid` element.]
    2. Case 2: `nums[mid] <= nums[right]`
        This means the elements from `mid` to `right` are sorted in ascending order. This means the minimum is either at mid itself or somewhere to its left. [Here we keep the `mid` element.]
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(log(n)); Space Complexity: O(1);
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** It's important to note when to include the `mid` element and when to discard it.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 