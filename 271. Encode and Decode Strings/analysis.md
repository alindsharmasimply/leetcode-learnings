## 1. The Core Concept (What is this?)
    The ask is very simple and straightforward.

## 2. Architectural Trade-offs
* **Approach A:** In such scenarios, one has to involve the length of every individual string.
* **Approach B:** 

## 3. Insights
* **Insight A:** Both Time and Space complexities would be O(n).
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** Using something like ":;" and appending it at the end of every word to encode a string will backfire quickly when any word itself contains this particular delimiter. As soon as we split during decoding, the word itself would get split too.
* **Gotcha 2:** 

## 5. Deep-Dive References
* 