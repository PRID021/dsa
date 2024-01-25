# Definition for a binary tree node.
null  = None
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Tree:
    def __init__(self, arr: list) -> None:
        def getNode(x: int):
            if x is None:
                return None
            return TreeNode(val=x)
        arr_node = [getNode(x) for x in arr ]
        n = len(arr_node)
        for i in range(0,n):
            if 2*i +1 < n:
                arr_node[i].left = arr_node[2*i +1]
            if 2*i + 2 < n:
                arr_node[i].right = arr_node[2*i + 2]
        self.root = arr_node[0]
        self.travel(node=self.root)

    def travel(self,node: TreeNode):
        print(node.val,end=" ")
        if node.left is not None:
            self.travel(node=node.left)
        if node.right is not None:
            self.travel(node=node.right)
