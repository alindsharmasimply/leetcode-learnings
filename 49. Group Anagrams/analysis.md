## 1. The Core Concept (What is this?)
    This is the use of a canonical key in a dictionary.

## 2. Architectural Trade-offs
* **Approach A:** Iterate through all the characters in every word. During iteration just increment the count of the alphabet index of every character. This count is a list of zeroes & will only have limited number of keys i.e., 26. Later, this count can be converted into a tuple and used as a key for the final dictionary. The final dictionary only stores lists as values. Hence the list will have all the words for a particular count of occurrences.
* **Approach B:** Sorting every word and then storing them as the canonical keys. (Not Optimal)

## 3. Insights
* **Insight A:** Time Complexity: O(n.k) where k is the length of each word.
* **Insight B:** Space Complexity: O(n.k) to store the frequency-signature keys and assuming the worst case of no string are an anagram of each other.

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 