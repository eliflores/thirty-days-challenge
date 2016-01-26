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

    def level_order(self, root):
        tree_height = self.get_height(root)
        for level in range(1, tree_height + 1):
            self.print_nodes_in_level(root, level)

    def print_nodes_in_level(self, root, level):
        if root is not None:
            if level == 1:
                print(root.data, end=' ')
            elif level > 1:
                self.print_nodes_in_level(root.left, level - 1)
                self.print_nodes_in_level(root.right, level - 1)

    def get_height(self, root):
        if root is None:
            return 0
        else:
            current = root
            height_left = self.get_height(current.left)
            height_right = self.get_height(current.right)
            return 1 + max(height_left, height_right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.level_order(root)
