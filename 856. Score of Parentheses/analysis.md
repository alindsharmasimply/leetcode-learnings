## 1. The Core Concept (What is this?)
    Just keep track of the depth of the parenthesis.

## 2. Architectural Trade-offs
* **Approach A:** Instead of keeping track of sub-expressions, we only need to track the current nesting `depth` as we walk through the string from left to right.
    1. When we see an opening bracket `(`, we go one level deeper: increment depth `depth += 1`.
    2. When we see a closing bracket `)`, we step back out: decrement depth `depth -= 1`.
    3. The Aha! Moment: If the closing bracket `)` immediately matches an opening bracket `(` right before it (i.e., we just finished an actual `()`), that base unit sits at the current depth d. We immediately add `2^depth` to our total score.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n), Space Complexity: O(1)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 