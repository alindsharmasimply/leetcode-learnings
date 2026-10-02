## 1. The Core Concept (What is this?)
    This is a very intuitive & interesting problem. A fixed-size window will traverse here.

## 2. Architectural Trade-offs
* **Approach A:** First, ensure that all characters of `s1` and the same length initial characters of `s2` are hashed in separate dedicated lists of size 26 (default value `0`). Now check if these lists match now. If they don't, then we start traversing the remaining characters of `s2`. Now we insert one and remove the first character of the window from the `s2` list. After every insertion-removal we compare the two frequency lists again. The moment these list become equal we return `True`. In the end we return `False`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n). Space Complexity: O(26)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Must handle the edge case where the length of `s1` is greater than that of `s2`.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 