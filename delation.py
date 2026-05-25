class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single_linkedList:
    def __init__(self):
        self.head=None
    def delete_at_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_at_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            prev=prev.next
            temp=temp.next
        prev.next=None
    def delete_at_middle(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            prev=prev.next
            temp=temp.next
        prev.next=temp.next
        temp.next=None
    def search(self,val):
        if self.head is None:
            print("empty")
            return
        flag=pos=0
        temp=self.head
        while temp:
            pos=pos+1
            if (temp.data==val):
                print(val,"vale is present")
                flag=1
            temp=temp.next
            if (flag==0):
                print(val,"not present")

    def tarverse (self):
        if self.head is None:
            print("single linked list is empty")
        temp=self.head
        while temp is not None:
            print(temp.data,"-->",end=" ")
            temp=temp.next #n2
obj=single_linkedList()
n1=node(10)
obj.head=n1
n2=node(20)
n1.next=n2
n3=node(30)
n2.next=n3
n4=node(40)
n3.next=n4

# obj.delete_at_middle()
# obj.delete_at_end()
# obj.delete_at_beg()
obj.search()
obj.tarverse()
