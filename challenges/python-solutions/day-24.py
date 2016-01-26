class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def remove_duplicates(self, head):
        current_node = head
        while current_node:
            next_node = current_node.next
            if next_node and current_node.data == next_node.data:
                current_node.next = next_node.next
                if current_node.next and current_node.data != current_node.next.data:
                    current_node = current_node.next
            else:
                current_node = current_node.next
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.remove_duplicates(head)
mylist.display(head)
