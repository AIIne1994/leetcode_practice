def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    ans = left = 0
    prod = 1
    for right, val in enumerate(nums):
        prod = prod * val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans


if __name__ == "__main__":
    pass
    