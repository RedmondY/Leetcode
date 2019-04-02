class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 如果不是none的话返回true
        if root is None:
            return True
        else:
            # 左右节点存在返回true
            if self.symmetric(root.right, root.left):
                return True
        return False
    
    def symmetric(self, a, b):
        if a is None and b is None:
            return True
        elif a is not None and b is None:
            return False
        elif a is None and b is not None:
            return False
        elif a.val != b.val:
            return False
        else:
            return self.symmetric(a.right, b.left) and self.symmetric(a.left, b.right)