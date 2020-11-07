import math

def smallest_divisor(nums, threshold):
    compute_sum = lambda x : sum([math.ceil(n / x) for n in nums])
    left, right = 1, nums[-1]
    while left <= right:
        pivot = (right + left) >> 1
        num = compute_sum(pivot)
        if num > threshold:
            left = pivot + 1
        else:
            right = pivot - 1
    return left


if __name__ == "__main__":
    pass
    