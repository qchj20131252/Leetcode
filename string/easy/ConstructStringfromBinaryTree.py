class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:return ""
        ans = str(t.val)
        if t.left or t.right:
            ans += "("+self.tree2str(t.left)+")"
        if t.right:
            ans += "("+self.tree2str(t.right)+")"
        return ans

class Solution2:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:return ""
        ans = str(t.val)
        if t.left and not t.right:
            ans += "("+self.tree2str(t.left)+")"
        if t.right:
            ans += "("+self.tree2str(t.left)+")"+"("+self.tree2str(t.right)+")"
        return ans
