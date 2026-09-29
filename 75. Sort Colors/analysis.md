## 1. The Core Concept (What is this?)
    The concept is of a three way partition.

## 2. Architectural Trade-offs
* **Approach A:** Just swapping the `0` element's positions and the `2` element's positions with the start and end pointer.
* **Approach B:** 

## 3. Insights
* **Insight A:** 
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember not to switch for element `1`. It will get auto-sorted.
* **Gotcha 2:** Also don't increment the `i` pointer when swapping for `2`. There's a chance that we maybe swapping back `0`, hence we need to ensure that this swapped-back `0` also gets registered in the next iteration.

## 5. Deep-Dive References
* 