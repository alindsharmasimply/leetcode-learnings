## 1. The Core Concept (What is this?)
    

## 2. Architectural Trade-offs
* **Approach A:** The first approach is more intuitive but uses extra space. We take a stack and initiallize its first element as `-1`. Now while we are traversing through the array when we encounter a `(` we push its index to the stack. When we encounter a `)` we check two conditions & act accordingly:
    - If stack is empty:
        - Push the current index. It means the current `)` has no matching `(`. This point marks a new boundary's beginning.
    - Else:
        - Record the `max_length` by subtracting the last index on the stack from the current index `i`. This indicates that a valid substring has been formed.
* **Approach B:** The second approach is a two-pass approach which doesn't use any extra memory. First pass is from left to right, second is the opposite:
    - Have two counters `left` and `right`.
    - In the first pass:
        - If current character is `(` then increment left by one else increment right by one.
        - If left becomes equal to right during any iteration then this means a valid string is complete hence store  twice of `right` in the `max_length`.
        - If `right` ever becomes greater than `left` then reset these variables to zero.
    Before starting the second pass, reset both counting variables.
    - In the second pass:
        - If current character is `(` then increment left by one else increment right by one. [Same as previous]
        - If left becomes equal to right during any iteration then this means a valid string is complete hence store  twice of `left` in the `max_length`. [minor change from previous]
        - If `left` ever becomes greater than `right` then reset these variables to zero. [stark opposite of previous]

## 3. Insights
* **Insight A:** First approach has both time and space complexity as O(n).
* **Insight B:** Second approach has time complexity as O(n) and space complexity as O(1).

## 4. The Pitfall Log
* **Gotcha 1:** Remember the edge case that if the string's length is less than 2 it becomes invalid automatically.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 