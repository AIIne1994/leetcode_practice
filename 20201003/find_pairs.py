def find_pairs(nums, k):
    num_dict = {}
    pairs_quant = 0
    for num in nums:
        num_dict.setdefault(num, 0)
        num_dict[num] += 1

    if k == 0:
        for num in num_dict.keys():
            if num_dict[num] > 1:
                pairs_quant += 1
    elif k > 0:
        for num in num_dict.keys():
            if num + k in num_dict.keys():
                pairs_quant += 1

    return pairs_quant


if __name__ == "__main__":
    pass
