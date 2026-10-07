## 1. The Core Concept (What is this?)
    Although we have to use the obvious solution of 'Sieve of Eratosthenes' but I still tried the approach that was in my mind as Solution-1.

## 2. Architectural Trade-offs
* **Approach A:** First approach which gives TLE is the use of a loop but we only check numbers till the square of every element.
* **Approach B:** The second approach uses 'Sieve of Eratosthenes' where we first initialize an array `is_prime` considering all the indices(representing the numbers) are prime. For numbers `0` and `1` we know that they're not prime hence we establish that. Then, from number `2` onwards we just run a loop till the `(square root of n) + 1`. Inside the loop when a number is prime indeed, we run another loop from its square till `n` with a step of that number itself. The idea is to mark all the multiples after the square as non-prime. Lastly the sum of this array `is_prime` is all that the question is looking for. [Recommended]

## 3. Insights
* **Insight A:** Time Complexity: O(n * (n^0.5)) which is bad.
* **Insight B:** Time Complexity: O(nloglogn), Space Complexity: O(n)

## 4. The Pitfall Log
* **Gotcha 1:** Remember that the loop doesn't run just till `n^0.5`. It actually runs till `n^0.5 + 1`.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 