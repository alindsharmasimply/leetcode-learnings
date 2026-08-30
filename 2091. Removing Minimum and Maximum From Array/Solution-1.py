class Solution:
  def minimumDeletions(self, nums: list[int]) -> int:
    n = len(nums)
    a = nums.index(min(nums))
    b = nums.index(max(nums))

    # Ensuring a remains smaller than b
    if a > b:
      a, b = b, a

    # Delete both from the front: To reach the further element b, we must delete b + 1 elements.
    # Delete both from the back: To reach the further element a from the right side, we must delete n - a elements.
    # Delete from both sides: Deleting a from the front costs a + 1, and deleting b from the back costs n - b. The total cost is a + 1 + n - b.
    return min(a + 1 + n - b, b + 1, n - a)