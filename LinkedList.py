

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList():
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertAfter(self,prev_node,new_data):
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    
    def append(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node

    def deleteNodeByKey(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return

        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next


        if(temp==None):
            return

        prev.next=temp.next
        temp=None
    
    def deleteNodeByPosition(self,position):
        if self.head==None:
            return

        temp=self.head
        if position==0:
            self.head=temp.next
            temp=None
            return
        
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break

        if (temp is None) or (temp.next is None): 
            return

        next=temp.next.next
        temp.next=None 
        temp.next=next
    def getCount(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
    
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev


if __name__ == "__main__":
    
    llist= LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)

    llist.head.next=second
    second.next=third

    llist.push(9)
    llist.append(8)
    llist.insertAfter(llist.head.next,7)
    llist.deleteNodeByKey(7)
    llist.printList()
    print('------------')
    print(llist.getCount())
    print('------------')
    llist.reverse()
    llist.printList()


    




