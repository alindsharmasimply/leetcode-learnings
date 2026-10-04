## 1. The Core Concept (What is this?)
    This problem is a simple use of sliding window.

## 2. Architectural Trade-offs
* **Approach A:** 
    Initialize a dictionary and start traversing the list of `fruits`. This dictionary will keep on storing the count of the fruits per category. As soon as a the number of categories exceeds 2 we ensure that we move the `left` pointer forward. But in order to do that we first remove atleast one fruit type from the dictionary. This reduction is done by reducing the count one by one as we move the `left` pointer forward. As soon as any category's count reaches 0, delete that category from the dictionary.
    Keep recording the max number of fruits at every iteration.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n). The Space Complexity would become O(1) becuase the dictionary only stores at max 3 elements at a time hence constant space.
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 