from typing import List
class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

def addNode(node: TreeNode, place: int) -> None:
    if node:
        if place > node.val:
            if node.right == None:
                node.right = TreeNode(place)
            else:
                addNode(node.right, place)
        if place < node.val:
            if node.left == None:
                node.left = TreeNode(place)
            else:
                addNode(node.left, place)

def createTree(nums: List[int]) -> TreeNode:
    if not nums:
        return None
    root = TreeNode(nums[0])
    for i in range(1,len(nums)):
        addNode(root, nums[i])
    return root 

def inorderT(root: TreeNode) -> List[int]:
    nums = []
    def helper(root: TreeNode, nums: List[int]) -> None:
        # inorder traversal
        if root != None:
            helper(root.left, nums)
            nums.append(root.val)
            helper(root.right, nums)
    helper(root, nums)
    return nums

def isValidBST(root: TreeNode) -> bool:
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)

"""
def isInvertedBST(root):

    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        val = node.val
        if val >= lower or val <= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True

    return helper(root)
"""
def breadthT(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    levels = [[root]]
    soln = [[root.val]]
    while levels[-1]:
        add = []
        addSoln = []
        for v in levels[-1]:
            if v.left:
                add.append(v.left)
                addSoln.append(v.left.val)
            if v.right:
                add.append(v.right)
                addSoln.append(v.right.val)
        levels.append(add)
        if addSoln:
            soln.append(addSoln)
    return soln
            