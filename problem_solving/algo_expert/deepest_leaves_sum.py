class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        level_sum = 0
        while queue:
            level_sum = 0
            q_size = len(queue)
            for _ in range(q_size):
                current = queue.pop(0)
                level_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return level_sum
