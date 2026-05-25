# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class double_linked_list:
#     def __init__(self):
#         self.head=None
# class traverse:
#     def display(head):
#         curr=head
#         while curr is not None:
#             print(curr.data,end=">")
#             curr=curr.next
#     print()

# obj=node(10)
# Python Program for Forward Traversal (Iterative) of
# Doubly Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

# Function to traverse the doubly linked list
# in forward direction        
def forward_traversal(head):
    curr = head
    while curr is not None:
        
        # Output data of the current node
        print(curr.data, end=" ")
        
        # Move to the next node
        curr = curr.next
    
    print()

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal: ", end="")
    forward_traversal(head)
