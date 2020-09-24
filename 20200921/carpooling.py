def carPooling(trips, capacity):
    start_points = {}
    end_points = {}
    success = True
    for num, start, end in trips:
        start_points.setdefault(start, 0)
        start_points[start] += num
        end_points.setdefault(end, 0)
        end_points[end] += num

    for i in range(max(max(start_points), max(end_points))):
        if capacity < 0:
            success = False
            break
        if i in start_points:
            capacity = capacity - start_points[i]
        if i in end_points:
            capacity = capacity + end_points[i]

    return success


if __name__ == '__main__':
    pass
    