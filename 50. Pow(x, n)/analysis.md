## 1. The Core Concept (What is this?)
    The concept is to follow recursion.

## 2. Architectural Trade-offs
* **Approach A:** We have to handle four cases in total:
    1. The base case when `n` becomes zero. Here we just return 1.
    2. The case where `n` can be a negative number. Here we just do what a negative power signifies, an inverse and again recursively call the function with a positive value of `n` this time.
    3. The case where `n` may be an odd number. Here we multiply the recursive call with one instance of `x` and hence we've used one power. So we now recursively call the function with a the reduced value of `n` by 1.
    4. The case where `n` would be an even number. Here we send the square value of `x` in the recursive call and the value of `n` is divided by 2 because one power of 2 is
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(log n), Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Because the exponent `n` is divided by 2 at each major step, the number of operations needed is proportional to the number of times we can divide `n` by 2 until it reaches 0. This growth rate is log_2(n), giving a O(log n) time.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 