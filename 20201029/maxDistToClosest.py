def maxDistToClosest(seats):
    max_space = 0
    space = 0
    for people_on_seat in seats:
        if people_on_seat:
            max_space = max(max_space, space)
            space = 0
        else:
            space += 1

    front_max_space = seats.index(1)
    seats.reverse()
    end_max_space = seats.index(1)
    mid_max_space = (max_space - 1) // 2 + 1

    return max(front_max_space, mid_max_space, end_max_space)

if __name__ == "__main__":
    pass
