class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


def head_list_generater(head_list):
    pre_node_num = 0
    pre_node = None
    node_list = []
    for val in head_list:
        if pre_node_num != 0:
            new_node = ListNode(val=val)
            pre_node.next = new_node
        else:
            new_node = ListNode(val=val)
        node_list.append(new_node)
        pre_node = new_node
        pre_node_num += 1
    return node_list


def get_decimal_value(head):
    val = 0
    while head.next != None:
        val = val * 2 + head.val
        head = head.next
    val = val * 2 + head.val
    return val


if __name__ == "__main__":
    pass
