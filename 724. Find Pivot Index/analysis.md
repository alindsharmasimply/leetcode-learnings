## 1. The Core Concept (What is this?)
    The concept is to balance the left and right sums using prefix sum.

## 2. Architectural Trade-offs
* **Approach A:** The first approach that comes to mind is that we maintain two lists of prefixes, one from the left and one from the right: `left_prefix` & `right_prefix`. Then traversing once and comparing the elements of the corresponding indexes will let us know which ones are equal. The first equality from the left is the correct answer.
* **Approach B:** The optimized and recommended approach is to keep the total sum of the entire list handy. Now at every point keep calculating the `prefix_sum` from the left. Here at every point the right sum would be `total_sum - prefix_sum - current_element`, hence we just have to check for that equality. [Recommended]

## 3. Insights
* **Insight A:** First approach is not to be used.
* **Insight B:** Second approach has time complexity: O(n) and space complexity: O(1)

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 