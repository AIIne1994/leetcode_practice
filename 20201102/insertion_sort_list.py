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


def insertion_sort_list(head):
    if not head or not head.next: return head
    res = ListNode(0, head)
    cur, nxt = head.next, head.next.next
    head.next = None
    pre_pre = res
    while cur:
        pre = pre_pre.next if cur.val > pre_pre.next.val else res
        while pre.next and cur.val > pre.next.val: 
            pre = pre.next
        cur.next, pre.next = pre.next, cur
        cur, pre_pre = nxt, pre
        nxt = nxt.next if nxt else nxt
    return res.next





if __name__ == '__main__':
    head_input_list = [4,2,1,3]
    head_list = head_list_generater(head_input_list)
    head = head_list[0]
    p = dummy = ListNode()
    print(p.val, dummy.val)
    dummy.next = head_list[0]
    p.next = head_list[1]
    p = p.next
    p.next = None
    print(p.val, dummy.next.val)
