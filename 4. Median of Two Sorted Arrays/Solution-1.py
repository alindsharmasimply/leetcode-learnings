class Solution:
    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float | None:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        high = m
        low = 0

        half_len = (m + n + 1) // 2

        while low <= high:
            i = low + (high - low) // 2
            j = half_len - i

            # Boundary values for nums1
            maxLeft1 = float("-inf") if i == 0 else nums1[i - 1]
            minRight1 = float("inf") if i == m else nums1[i]

            # Boundary values for nums2
            maxLeft2 = float("-inf") if j == 0 else nums2[j - 1]
            minRight2 = float("inf") if j == n else nums2[j]

            # Check if partition is correct
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # If total length is even
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0

            elif maxLeft1 > minRight2:
                high = i - 1  # Move left in nums1
            else:
                low = i + 1  # Move right in nums1
