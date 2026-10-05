## 1. The Core Concept (What is this?)
    The core concpet is Kadane's Algorithm only but with a slight twist.

## 2. Architectural Trade-offs
* **Approach A:** In Kadane's Algorithm the addition of a negative number would always bring the max_sum down but here when a negative number is multiplied it can bring the max up or down depending upon what is the sign of the product developed yet.
    So we maintain two types of products: one for `current_min` and one for `current_max`. We just have to ensure that everytime the current number is negative we swap the values of these two products. Meanwhile during this traversal loop we would also keep on maintaining the final answer max product from the `current_max`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n), Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** The initial value of the `ans` variable would be the number at the zeroth index.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 