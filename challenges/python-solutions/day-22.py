class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def get_height(self, root):
        if root is None:
            return 0
        else:
            current = root
            height_left = self.get_height(current.left)
            height_right = self.get_height(current.right)
            return 1 + max(height_left, height_right)


T = int(input())
my_tree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = my_tree.insert(root, data)
height = my_tree.get_height(root)
print(height)
