## 1. The Core Concept (What is this?)
    The most intuitive solution for this should be using backtracking via recursion.

## 2. Architectural Trade-offs
* **Approach A:** The approach is to remember that the `opened_parenthesis` count can never exceed the number of pairs `n` and the `closed_parenthesis` count can never exceed the `opened_parenthesis` count. We start the recursion by keeping the opened and closed parenthesis count as `0` and by keeping the combination as an empty string. Inside the `backtracking()` function we just put two separate conditions to increment the count with the respective parenthesis. The base case is when both the opened and closed parenthesis counts reach the number of pairs `n`.
* **Approach B:** 

## 3. Insights
* **Insight A:** The upper bound of a brute force approach would be O(2^2n) because at each of the 2n positions, we have up to 2 choices: an opening or a closing parenthesis. However, because our backtracking algorithm actively prunes invalid paths early, we only generate valid combinations. Still, rather than telling the Time complexity to be the Catalan's number simply assume it to be O(2^2n).
* **Insight B:** Space Complexity would be O(n) to accomodate for the recursion stack.

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 