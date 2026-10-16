## 1. The Core Concept (What is this?)
    This is quite non-intuitive and the need for a stack is just not necessary.

## 2. Architectural Trade-offs
* **Approach A:** Sort by position because we want to process the cars that are closest to the target first.
    For each car calculate the time it would take to reach the target alone.
    Iterate, and if a car behind takes longer to reach the target than the car (or fleet) ahead of it, it cannot catch up. Thus, it forms a new fleet.
    If a car behind takes less time or equal time, it will catch up to the car ahead before or at the target, meaning it merges into the existing fleet and does not increase the total fleet count.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(Nlog N), dominated by sorting the `N` cars by position. The subsequent linear pass through the sorted cars takes O(N) time.
* **Insight B:** Space Compleity: O(N) to store the cars pairs and the stack. (Note: Space can be optimized to (O(1) by tracking only a `max_time` variable instead of a full stack).

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 