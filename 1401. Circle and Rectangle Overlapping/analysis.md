## 1. The Core Concept (What is this?)
    Simple observation is needed.

## 2. Architectural Trade-offs
* **Approach A:** First find out the closest point of the rectangle to the center of the circle. Now just get the pythagorean distance of that point from the center of the circle. If it goes beyond the radius then there is no overlap.
* **Approach B:** 

## 3. Insights
* **Insight A:** 
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Remember that it's given that x2 >= x1 hence we have to fetch the minimum out of the center's x-coordinate and x2.
* **Gotcha 2:** Using x1 instead of x2 would always return x2 as a final result of `max(min(xCenter, x1), x2)`

## 5. Deep-Dive References
* 