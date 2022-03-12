import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root,k,arr=[]):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        if sum(arr)+root.data==k:
            print(*arr,end=" ")
            print(root.data)
        return
    arr.append(root.data)
    rootToLeafPathsSumToK(root.left,k,arr)
    rootToLeafPathsSumToK(root.right,k,arr)
    arr.pop()


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k = int(input())
rootToLeafPathsSumToK(root, k, arr=[])
