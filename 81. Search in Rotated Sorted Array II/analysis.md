## 1. The Core Concept (What is this?)
    When we pick a midpoint in a rotated sorted array, the pivot point (where the rotation happened) can only exist in one of the two halves. The other half must be cleanly sorted.

## 2. Architectural Trade-offs
* **Approach A:** Comparing `nums[low]` and `nums[mid]` easily tells us which side is sorted. But duplicates introduce ambiguity.
    In the following two examples, it is mathematically impossible to know which half contains the sorted sequence and which contains the target:
    • Scenario A: [1, 0, 1, 1, 1] — Target is 0. The pivot is in the left half, and the right half is sorted.
    • Scenario B: [1, 1, 1, 0, 1] — Target is 0. The pivot is in the right half, and the left half is sorted.
    When we hit this wall of ambiguity `(nums[low] == nums[mid] == nums[high])`, we cannot eliminate half of the array at once. Instead, we must shrink the search space linearly. Hence we increment `left` and decrement `right`, both by one.
* **Approach B:** 

## 3. Insights
* **Insight A:** Average Case: O(log n). When duplicates are sparse, we almost always eliminate half the array in each step.
* **Insight B:** Worst Case: O(n). If the array consists entirely of duplicates (e.g., [1, 1, 1, 1, 1]) and the target is 0, we will have to step inward one element at a time, turning the binary search into a linear scan.

## 4. The Pitfall Log
* **Gotcha 1:** Remember that there are two kinds of complexities to be discussed.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 