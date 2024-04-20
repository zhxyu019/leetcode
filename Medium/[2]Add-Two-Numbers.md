Logic

- ListNode are classes representing a linked list node, so you cannot apply list slicing to reverse the indexes. l1 & l2 are objects of type ListNode.
- Approach: we need to transverse the linked lists and extract the values of each node to perform addition.
- We need to create a carry variable to hold the carry-over value during addition.
- We then create a loop that continues looping over each index as long as one of the linked lists is not empty, or if there is a carry-over from the previous addition.
- In the loop, we calculate the sum of digits, along with the carry over value. For sum_val, we can calculate the value to be stored in the current node of the result list. One case we have to account for is if sum_val > 10, so we need to find the remainder if that's the case.
- The dummy node exists so we can return to the head of the resulting linked list after all is looped, so this skips the dummy node and starts from the first actual result node.

Runtime: 30ms (beats 98.74% of users)
