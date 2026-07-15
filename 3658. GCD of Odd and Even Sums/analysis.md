# DSA / Leetcode / GCD of Odd and Even Sums

## 1. The Core Concept (What is this?)
  This is a series based question. Also uses the Eucledean principle of calculating the Greatest Common Divisor.

## 2. Architectural Trade-offs
* **Approach A:** One way could be to use the built-in math.gcd() method in Python
* **Approach B:** Another way would be to use the Eucleadean Theorem by recursively interchanging the numbers with their remainder until the remainder reaches zero.

## 3. Insights
* **Insight A:** Formula for sum of an A.P. series: ```(n/2) * ((2 * a) + (n - 1) * d)```