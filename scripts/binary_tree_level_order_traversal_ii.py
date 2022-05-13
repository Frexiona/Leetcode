class Solution:
    def levelOrderBottom(self, root):
        queue, results = list(), list()
        if not root:
            return root
        queue.append(root)
        while queue:
            break_count = len(queue)
            # shallow copy, otherwise queue will grow infinitely
            temp_queue = list(queue)
            for each in temp_queue:
                if each.left:
                    queue.append(each.left)
                if each.right:
                    queue.append(each.right)
            sub_list = list()
            while break_count > 0:
                sub_list.append(queue.pop(0).val)
                break_count -= 1
            results.append(sub_list)
        
        return results[::-1]