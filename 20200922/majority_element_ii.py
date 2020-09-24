def majorityElement(nums):
    num_judge = len(nums) // 3
    num_dict = {}
    for num in nums:
        num_dict.setdefault(num, 0)
        num_dict[num] += 1

    return [num for num in num_dict if num_dict[num] > num_judge]


if __name__ == '__main__':
    pass