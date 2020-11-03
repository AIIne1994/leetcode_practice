def max_power(s):
    pre = ''
    max_num = 0
    num = 1
    for ch in s:
        if ch == pre:
            num += 1
        else:
            max_num = max(num, max_num)
            num = 1
        pre = ch
    return max(num, max_num)


if __name__ == '__main__':
    pass
