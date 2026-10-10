## 1. The Core Concept (What is this?)
    Concept of Binary Search suits appropriately here.

## 2. Architectural Trade-offs
* **Approach A:** Consider choosing which weight capacity would be the most appropriate by going through the binary search way rather than guessing linearly. Obviously the possibility lies only between the max value in the weights list and the total sum of weights.
    Everytime we get the `mid` we just check if we can ship with this weight. If we can then all the weight capacities beyond this weight capacity will also work. Since the question is about to find the least possible weight capacity hence we would reduce the `high` pointer to `mid - 1`. Otherwise increase the `low` pointer to `mid + 1`.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(Nlog(S)), where N is the number of packages and S is the sum of all weights. Space Complexity: O(1) extra space.
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** The `low` weight measure would not be `1`, rather it would be the max value in the `weights` list.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 