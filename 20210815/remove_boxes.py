def box_counter(boxes):
    counter = {}
    max_continuous = {}
    max_pos = {}
    min_continuous = {}
    min_pos = {}
    prv = 0
    count = 0

    for i, box in enumerate(boxes):
        counter.setdefault(box, 0)
        counter[box] += 1
        max_continuous.setdefault(box, 1)
        max_pos.setdefault(box, i)
        min_continuous.setdefault(box, 101)
        min_pos.setdefault(box, i)

        if box != prv and prv != 0:
            if max_continuous[prv] < count:
                max_continuous[prv] = count
                max_pos[prv] = i - count
            if min_continuous[prv] > count:
                min_continuous[prv] = count
                min_pos[prv] = i - count
            count = 0

        count += 1
        prv = box

    if box == prv:
        if max_continuous[prv] < count:
            max_continuous[prv] = count
            max_pos[prv] = i - count + 1
        if min_continuous[prv] > count:
            min_continuous[prv] = count
            min_pos[prv] = i - count + 1
        count = 0

    smallest_one = 0
    smallest_val = 101
    for i in counter:
        if counter[i] < smallest_val:
            smallest_one = i
            smallest_val = counter[i]

    data = {
        "counter": counter,
        "smallest_one": smallest_one,
        "max_continuous": max_continuous,
        "max_pos": max_pos,
        "min_continuous": min_continuous,
        "min_pos": min_pos,
        }

    return data


def remove_boxes(boxes):
    result = 0
    while boxes != []:
        print(boxes)
        data = box_counter(boxes)
        smallest_one = data["smallest_one"]
        max_term = 0
        for i in data["counter"]:
            if data["counter"][i] == data["max_continuous"][i]:
                max_term = data["max_continuous"][i] ** 2
                break

        if max_term:
            result += max_term
            left_index = data["max_pos"][i]
            right_index = data["max_pos"][i] + data["max_continuous"][i]
        else:
            smallest_one = data["smallest_one"]
            result += data["min_continuous"][smallest_one] ** 2
            left_index = data["min_pos"][smallest_one]
            right_index = data["min_pos"][smallest_one] + data["min_continuous"][smallest_one]
        boxes = boxes[:left_index] + boxes[right_index:]


    return result


if __name__ == '__main__':
    data = remove_boxes([5,8,3,8,4,8,5,7,4,2])
    print(data)

