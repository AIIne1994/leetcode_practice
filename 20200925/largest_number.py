def largestNumber(nums):
    str_nums = [str(num) for num in nums]
    str_nums.sort(reverse=True)
        
    flag = False
    while not flag:
        flag = True
        i=0
        while i < len(str_nums) - 1:
            if str_nums[i] + str_nums[i+1] < str_nums[i+1] + str_nums[i]:
                str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                flag = False
            i += 1
                
    re_str = "".join(str_nums)
        
    if re_str[0] == '0':
        return str(0)
        
    return re_str  


if __name__ == "__main__":
    pass