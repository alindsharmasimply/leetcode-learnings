## 1. The Core Concept (What is this?)
    Not intuitive at all. 

## 2. Architectural Trade-offs
* **Approach A:** Let's try to understand it step by step:
-- It's understood that the prefix sums would be needed. 
-- Then we also have to hash those prefix sums and store the count of how many times a particular sum appeared.
-- Now, finally the tough part:
    -- At every index, its prefix_sum minus the target 'k' will give us a count from the dictionary of:
        - whether it has happened before, and if yes then
        - how many times it has happened before.
        - Each time we found it, it means a valid subarray ending at the current index adds up to 'k'.
-- Just keep adding these 'times' and we get the final answer.
* **Approach B:** 

## 3. Insights
* **Insight A:** The 'why' of this approach is still hazy in my head. It would take a few revisions before understanding this approach.
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** The Sliding Window approach won't work here since the approach works only for non-negative integers.
* **Gotcha 2:** 

## 5. Deep-Dive References
* https://www.youtube.com/watch?v=WpHt8KW02jg