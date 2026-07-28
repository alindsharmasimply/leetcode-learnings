# DSA / Leetcode / Smallest Palindromic Rearrangement I

## 1. The Core Concept (What is this?)
    String manipulation

## 2. Architectural Trade-offs
* **Approach A:** Sort the first half and then return a joined string of the sorted first half, middle elment as it is (if length of string is odd) and the reverse of the sorted first half.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity would be O(nlogn) & Space Complexity would be O(n)
* **Insight B:** A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References