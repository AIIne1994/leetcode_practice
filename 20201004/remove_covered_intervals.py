def remove_covered_intervals(intervals):
    intervals.sort(key=lambda interval: (interval[0], -interval[1]))
    maximum = -1
    removed = 0
    for interval in intervals:
        if interval[1] <= maximum:
            removed += 1
        else:
            maximum = interval[1]

    return len(intervals) - removed


if __name__ == "__main__":
    pass
