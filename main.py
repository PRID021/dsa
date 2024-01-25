
from typing import Optional

from binary_tree import Tree, TreeNode


global max_length
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        global max_length
        max_length = 0
        if root is None:
            return max_length
        self.backTrack(node=root,target =root.val,current=[])
        return max_length

    
    def backTrack(self,node: TreeNode,target:int, current: list):
        global max_length
        if node.val == target:
            current.append(node.val)
            max_length = max(max_length, len(current) -1)

            if node.left is not None:
                self.backTrack(node= node.left,target= target ,current=current.copy())
            if node.right is not None:
                self.backTrack(node= node.right,target = target ,current=current.copy())
        else:
            self.backTrack(node=node,target=node.val,current=[])



tree  = Tree(arr=[1,4,5,4,4,None,5])
solution = Solution()
print(solution.longestUnivaluePath(root=tree.root))