## 1. The Core Concept (What is this?)
    Simple sliding window problem. A dictionary is not required here.

## 2. Architectural Trade-offs
* **Approach A:** Here we optimize for length of the shortest subarray whose sum is >= `k`. Declare a `left` pointer and the `right` pointer would be the iterator in the `for` loop. A variable `current_sum` would keep the count of the sum at every iteration. The moment this variable's value comes out to be >= `k` we start decrementing the `left` pointer. Also decrement the value at the `left` index. We keep doing this till the `current_sum` doesn't become less than the value of `k`. During this process only we have to first and foremost record the `min_length` at the beginning.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n), Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** The edge case where there is no possibility of the `current_sum` becoming greater than or equal to `k` would leave the `min_length` as infinity or whatever number we initialized it with.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 