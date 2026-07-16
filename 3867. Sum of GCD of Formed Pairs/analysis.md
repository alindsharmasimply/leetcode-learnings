# DSA / Leetcode / Sum of GCD of Formed Pairs

## 1. The Core Concept (What is this?)
    This is a GCD based problem

## 2. Architectural Trade-offs
* **Approach A:** Simple approach of iterating through the entire list of nums.
* **Approach B:** The second approach is only using the ```math.gcd``` method instead of recursively calculating it.

## 3. Insights
* **Insight A:** When I use the built-in function of ```math.gcd```, I get better results on leetcode.

## 4. The Pitfall Log
* **Gotcha 1:** The use of ```sorted()``` method returns the sorted list and doesn't modify the list in-place. For that we use ```.sort()``` method.

## 5. Deep-Dive References