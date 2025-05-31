class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)



tree5 = BinaryTree(1)
tree5.left = BinaryTree(2)
tree5.right = BinaryTree(3)
tree5.left.left = BinaryTree(4)
tree5.left.right = BinaryTree(5)
tree5.right.left = BinaryTree(6)
tree5.right.right = BinaryTree(7)
ele=branchSums(tree5)
print(ele)