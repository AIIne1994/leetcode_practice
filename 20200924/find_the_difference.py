def findTheDifference(s, t):
    total = 0
    for i, ch in enumerate(s):
        total += ord(t[i])
        total -= ord(s[i])
    total += ord(t[-1])
    return chr(total)

if __name__ == '__main__':
    pass
