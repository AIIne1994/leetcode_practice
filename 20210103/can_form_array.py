# def connected_in_arr(arr, piece):
#     if piece[0] in arr:
#         head = arr.index(piece[0])
#         for i, num in enumerate(piece):
#             if (i+head) >= len(arr):
#                 return False
#             if arr[i + head] != num:
#                 return False
#         return True
#     else:
#         return False


def canFormArray(arr, pieces):
    def connected_in_arr(arr_part, piece):
        if piece[0] in arr_part:
            head = arr_part.index(piece[0])
            for i, num in enumerate(piece):
                if (i+head) >= len(arr_part):
                    return False
                if arr_part[i + head] != num:
                    return False
            return True
        else:
            return False


    for piece in pieces:
        if connected_in_arr(arr, piece):
            for num in piece:
                arr.remove(num)

    return arr == []


if __name__ == '__main__':
    print(connected_in_arr([91, 4, 64, 78], [4, 64]))
