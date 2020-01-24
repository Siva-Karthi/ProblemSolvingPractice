# This is the class of the input root. Do not edit it.
def branchSums(root):
    res = []

    def branch_sum_helper(root, curr_sum=0):
        if root:
            curr_sum += root.value
            if not root.left and not root.right:
                res.append(curr_sum)
                return
            branch_sum_helper(root.left, curr_sum)
            branch_sum_helper(root.right, curr_sum)
        else:
            return

    branch_sum_helper(root)
    return res
