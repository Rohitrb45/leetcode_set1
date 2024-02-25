class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       def find_height(node):
           if not node:
               return 0
           l_height=find_height(node.left)
           r_height=find_height(node.right)
           return max(l_height,r_height)+1

       def check_balance(node):
            if not node:
                return True
            lh=find_height(node.left)
            rh=find_height(node.right)
            if(abs(lh-rh)>1):
                return False
            return check_balance(node.left) and check_balance(node.right)

       return check_balance(root)