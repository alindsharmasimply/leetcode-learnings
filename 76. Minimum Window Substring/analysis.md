## 1. The Core Concept (What is this?)
    This one is not intuitive at all. Just a two pointer sliding window problem.

## 2. Architectural Trade-offs
* **Approach A:** First there should be a dictionary that stores the count of all the characters in `t`. There should also be a `required` counter that stores the count of valid characters inclusion in a certain substring. The concept is to decrement both the dictionary and counter everytime a needed character is traversed.
When the `required` counter becomes equal to zero then the need arises to start shifting the `left` pointer forward hence we start a `while` loop. The first thing we do is check if the current length is less than the `min_length` and assign it accordingly. This is also the place where we assign the `best_left` index. Now, we increment the dictionary with the character count of the `left` pointer. 
Next we check if the `left` pointer is pointing to a needed character, if yes then we have to increment the `required` counter. (Remember earlier we 'decremented' and now we are incrementing)
Lastly we just increment the `left` pointer.
During returning the string we return a substring starting from the `best_left to (best_left + min_length)`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(m + n) and Space Complexity: O(128)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** The `best_left` is only used because we need to return the minimum string itself and not just the minimum length.
* **Gotcha 2:** Remember the edge case when `best_left` is -1. That only means that there was not a single valid string present.

## 5. Deep-Dive References
* 