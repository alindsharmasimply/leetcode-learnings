## 1. The Core Concept (What is this?)
    We need to peel every layer of the matrix like that of an onion.

## 2. Architectural Trade-offs
* **Approach A:** Take four variables that will always define which is the next layer to peel from top, right, bottom and left (clockwise). Then we traverse across all 4 layers in order to peel them. Everytime we traverse one layer we either increment or decrement the variable whose layer just got peeled. While we traverse we also keep appending the visited matrix element into a result list.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity = O(m.n) while Space Complexity is (1).
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** The last two layer traversals (right -> left & bottom -> top) are important. They can get traversed more than one time hence resulting in duplicated element-reading. We need to avoid that by putting the respective boundary conditions on these two traversals.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 