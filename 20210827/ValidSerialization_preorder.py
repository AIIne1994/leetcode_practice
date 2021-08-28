def isValidSerialization(preorder):
    preoder_list = preorder.split(",")
    node_list = [[preoder_list[0], 2]]
    for i in range(1, len(preoder_list)):
        node_list[-1][1] -= 1
        if node_list[-1][1] == 0:
            node_list.pop()
        if preoder_list[i] != "#":
            node_list.append([preoder_list[i], 2])

        print(node_list)
                
    return node_list == []

if __name__ == '__main__':
    isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")