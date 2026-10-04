## 1. The Core Concept (What is this?)
    The approach here requires prefix sum.

## 2. Architectural Trade-offs
* **Approach A:** Use a dictionary which will store the `prefix % k` as key and the current index as the value. It is initialized with `{0: -1}` so as to signify that there is no fully divisible prefix available yet at any index.
    Traverse the list and keep adding up the prefix. If `k == 0` make sure to make `prefix = prefix % k` and check for its existence in the dictionary. If present and the `current_index - the dictionary_returned_index > 1` then it's confirmed that there is a multiple of `k` between these two indices as well as the number of elements is 2 or more than 2.
    Otherwise just keep storing the key-value of the prefix-mod and current index.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time complexity: O(n) and Space Complexity: O(n)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 