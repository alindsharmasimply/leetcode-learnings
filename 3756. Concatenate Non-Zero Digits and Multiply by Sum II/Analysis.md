# [DSA / Leetcode / Concatenate Non-Zero Digits and Multiply by Sum II]

## 1. The Core Concept (What is this?)
> This is a prefix sum based problem.

## 2. Architectural Trade-offs
* **Approach A:** My initial naive appraoch was to iterate through the substring for every query, sum it up and then convert the substring to integer, multiply it with the sum and return. This would result in O(n^2) time complexity.
* **Approach B:** Another approach is to first store 3 things:
    - One array of prefix sum upto every index
    - One array of valid number upto every index
    - One array of count of valid number digits upto every index
    - Then we need to extract everything based on the upper query index and (lower query index - 1).

## 3. Insights
* **Insight A:** We can use ```sys.set_int_max_str_digits(0)``` if we want to remove the restriction of number of digits/characters of a string that the int() method can take to convert into a number.
* **Insight B:** The pow() method in python has a third argument for modulus => ```pow(base, exponent, modulus=None)```

## 4. The Pitfall Log
* **Gotcha 1:** In the initial approach I didn't take into consideration that the concat_str string can be empty also.
* **Gotcha 2:** One has to take into consideration the use of MOD here. It isn't just supposed to be a part of the final result appending. It needs to be present during the calculation too.

## 5. Deep-Dive References
* [https://www.youtube.com/watch?v=wikD48h_hjQ]