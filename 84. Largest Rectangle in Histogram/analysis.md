## 1. The Core Concept (What is this?)
    The idea is, the moment we see a dip in the heights, we process the top of stack item in backward direction.

## 2. Architectural Trade-offs
* **Approach A:** 
    1. On the stack we're going to place tuples of (index, height).
    2. We're only trying to see that if we have a height then how far can we extend that height. Obviously a certain height can't be extended if its next height is less than itself, which is when we start a `while` loop and process backward by popping the stack.
    3. Once the entire traversal is over, we make sure that any remaining heights in the stack also get considered for the `max_area`. It's important to remember that at this point the current index would be considered equal to `n` because we've reached the end of the `heights` list.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n); Space Complexity: O(n);
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* https://www.youtube.com/watch?v=ZGMw8Bvpwd4