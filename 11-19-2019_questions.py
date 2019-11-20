#Add two numbers Linked list

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1, curr2 = l1, l2
        carry = 0
        #dummy head for now to not worry about edge case
        #iterate over both lists, add values and make new node respectively
        head = ListNode(None)
        prev = head
        while curr1 and curr2:
            added = curr1.val + curr2.val + carry
            if added > 9:
                carry = 1
                result = added-10
            else:
                carry = 0
                result = added
            newNode = ListNode(result)
            prev.next = newNode
            prev = prev.next
            curr1=curr1.next
            curr2=curr2.next

        while curr1:
            added = curr1.val + carry
            if added >9:
                carry = 1
                result = added -10
            else:
                carry = 0
                result = added
            prev.next = ListNode(result)
            prev=prev.next
            curr1 = curr1.next

        while curr2:
            added = curr2.val + carry
            if added > 9:
                carry = 1
                result = added -10
            else:
                carry = 0
                result = added
            prev.next = ListNode(result)
            prev = prev.next
            curr2 = curr2.next

        if carry != 0:
            prev.next = ListNode(carry)
        return head.next

#Trapping Rain Water
"""
    Lessons learned:
        Approach from left and right to set up DP tables
        Minimum in the DP tables give you the answer
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [None] * len(height)
        max_right = [None] * len(height)

        curr_max = 0
        for i in range(len(height)):
            curr_max = max(height[i],curr_max)
            max_left[i] = curr_max

        curr_max = 0
        for j in range(len(height)-1,-1,-1):
            curr_max = max(height[j],curr_max)
            max_right[j] = curr_max

        print(max_left)
        print(max_right)

        min_combined = [min(max_left[val],max_right[val])-height[val] for val in range(len(height))]
        result = sum(min_combined)
        return result

# Container With Most Water
"""
    Lessons learned:
        Two pointers - start and end
        Able to shift start and end respectively to try to maximize area
        Start with maximum width: 0 and len(height)
        Move the smaller of the height[start] and height[end]
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_area = 0
        while start < end:
            curr_area = min(height[start],height[end]) * (end-start)
            max_area = max(curr_area, max_area)

            if height[start] < height[end]:
                start+=1
            else:
                end -= 1
        return max_area
