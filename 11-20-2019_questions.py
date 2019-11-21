#Merge 2 linked list
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        newList = ListNode(None)
        prev = newList

        #if both lists have items
        while l1 and l2:
            if l1.val < l2.val:
                newNode = ListNode(l1.val)
                prev.next = newNode
                prev = prev.next
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                prev.next = newNode
                prev = prev.next
                l2 = l2.next

        #if list1 has more items
        while l1:
            newNode = ListNode(l1.val)
            prev.next = newNode
            prev = prev.next
            l1 = l1.next

        #if list2 has more items
        while l2:
            newNode = ListNode(l2.val)
            prev.next = newNode
            prev = prev.next
            l2 = l2.next

        return newList.next

#Reverse LinkedList
class Solution:
    """
        iterative using a stack
    """
#     def reverseList(self, head: ListNode) -> ListNode:
#         stack = []
#         while head:
#             stack.append(head)
#             head = head.next

#         if stack:
#             curr = stack.pop()
#             newHead = curr
#             while len(stack) > 0:
#                 nex = stack.pop()
#                 curr.next = nex
#                 curr = nex

#             curr.next = None

#             return newHead

#         return None
    """
        recursive
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            rest = self.reverseList(head.next)
            head.next.next  = head
            head.next = None

            return rest

### Merge k sorted lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        from Queue import PriorityQueue

        #we will use a min-heap to help us
        q = PriorityQueue()

        for header in lists:
            if header:
                #put in head's value to sort by and the node itself
                q.put((header.val,header))

        head = curr = ListNode(None)

        while not q.empty():
            val, node = q.get()
            #print(val,node)
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next

            #if the node has more items, add its follower into the heap.
            if node.next:
                q.put((node.next.val,node.next))

        return head.next

#Validate BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = self.inorder(root)
        for i in range(1,len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False

        return True

    def inorder(self,root):
        if root is None:
            return []
        else:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)


#Symmetric Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.mirror(root,root)

    def mirror(self,A,B):
        if A is None and B is None:
            return True
        if A is None or B is None:
            return False
        return A.val == B.val and self.mirror(A.left,B.right) and self.mirror(A.right, B.left)

#Binary Tree Level order traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        from Queue import Queue
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        count = 1
        q = Queue()
        q.put(root)
        result = []
        temp = []

        while not q.empty():
            item = q.get()
            temp.append(item.val)
            count -= 1
            if item.left:
                q.put(item.left)
            if item.right:
                q.put(item.right)
            if count == 0:
                result.append(temp)
                temp = []
                count = q.qsize()
        return result

#Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.helper(root)[1]

    def helper(self,root):
        #input root
        #returns: tuple of (height,max_path)

        if root is None: #Empty tree
            return (0,0)
        if root.left is None and root.right is None:
            return (1,0)

        left = self.helper(root.left) #get height and max_path of left
        right = self.helper(root.right) #get height and max_path of right
        curr_height = max(left[0],right[0]) + 1
        curr_path = max(left[0] + right[0], left[1], right[1])
        return(curr_height,curr_path)
