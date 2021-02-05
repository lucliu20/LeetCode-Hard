# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

"""
Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# [1,2,3,None,None,4,5,None,None,None,None]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# [-1,0,3,-2,4,None,None,8,None,None,None,10,None,None,None]
# root = TreeNode(-1)
# root.left = TreeNode(0)
# root.right = TreeNode(3)
# root.left.left = TreeNode(-2)
# root.left.right = TreeNode(4)
# root.left.left.left = TreeNode(8)
# root.left.left.left.left = TreeNode(10)

# root = None


# Iteratively
# BFS
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        queue = collections.deque([root])
        res = []
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                if curr:
                    res.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    res.append(None)
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data[0])
        queue = collections.deque([root])
        k = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                curr = queue.popleft()
                if curr:
                    if data[k] != None:
                        node = TreeNode(data[k])
                        queue.append(node)
                        curr.left = node
                    
                    if data[k+1] != None:
                        node = TreeNode(data[k+1])
                        queue.append(node)
                        curr.right = node
                k += 2
        return root
                
        
ser = Codec()
stype = ser.serialize(root)
print(stype)

deser = Codec()
ans = deser.deserialize(stype)
print(ans)

# Runtime: 108 ms, faster than 91.66% of Python3 online submissions for Serialize and Deserialize Binary Tree.
# Memory Usage: 18.8 MB, less than 78.18% of Python3 online submissions for Serialize and Deserialize Binary Tree.


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))