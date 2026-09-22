## 1. The Core Concept (What is this?)
    Use of prefixes and suffixes only. Because obviously the numbers can be 0 or less than 0.

## 2. Architectural Trade-offs
* **Approach A:** Create two lists of prefix and suffix products. Which means that every index will store the product of the elements to its left(prefix array) or the product of the elements to its right(suffix array). Finally return a list of all the synonymous indexed products of both lists.
* **Approach B:** Create just one list, the 'result' list. This would itself store all the prefix products in the first pass. Next, instead of storing the suffixes in a fresh array, just maintain one variable that would keep on storing the suffix product and will keep on multiplying it with the result array elements starting from the end.

## 3. Insights
* **Insight A:** The first approach offers both time and space complexity as O(n).
* **Insight B:** The second approach has O(n) time complexity and O(1) space complexity.

## 4. The Pitfall Log
* **Gotcha 1:** We must remember that the output array does not count as extra space per typical interview rules.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 