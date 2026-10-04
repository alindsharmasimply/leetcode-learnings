## 1. The Core Concept (What is this?)
    This one can become intuitive if tried.

## 2. Architectural Trade-offs
* **Approach A:** The concept is to have two count variables `min_open` and `max_open`. These variables are counters of possibilities that can happen at the current element while traversing the string. 
    For example, in `(*`:
        1. At the first element, `min_open = 1, max_open = 1`.
        2. At the second element, `min_open = 0, max_open = 2`. Because either we would like to have `()` or ``.
    So we have to increment both counts when we encounter `(`, decrement both counts when we encounter `)`, and decrement `min_count` and increment `max_count` when we encounter `*`.
    But we have to take care of two constraints:
        - if `max_open < 0` then we immediately return `False` because it's clear that now no matter how many `(` or `*` come the string would never have validity because by now the number of `)` have surpassed the number of `(`. Example: `())*`
        - if `min_open < 0` then we reset it immediately to zero because we over-assumed that `*` is a `(`. Example: `*()`

* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n), Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 