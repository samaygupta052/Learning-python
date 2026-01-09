# in linkedlist node we can also store object of any data type.
# there are two parts in a node
# 1. data part  
# 2. next part (address of next node)
# last node next part will have null value
# head is the starting point of linkedlist 
# to access data and address use --- head.data and head.next 
# in sigle linkedlist we can traverse in only one direction i.e from head to last node
# to access next block data and address -- head.next.data head.next.next
# we use temp variable to traverse the linkedlist without losing the head pointer

class node: # why to create a class for node ? because each node has its own data and next part
    def __init__(self,data,next=None):  # why to amake constructor ? to initialize the data members of class 
       #why to use self as parameter ? to refer to the current object of the class
        self.data = data
        self.next = next
#what is self.data = data  ?  here left data is the data member of class and right data is the parameter of constructor. what do u mean by member of class ?  member of class means the variables and methods defined inside the class
# why to create linkedlist class ? to manage the linkedlist operations
# we can also create it in node class but it is better to create a separate class for linkedlist operations. but why ? because it will make the code more organized and easier to understand

class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head  # head is the starting point of linkedlist
    
    def insertAtEnd(self,value):
        temp = node(value)  # create a new node with given value
        if(self.head !=None):  
            t1 = self.head # temporary variable to traverse the linkedlist
            while(t1.next != None):
                t1 = t1.next 
            t1.next = temp
        else:
            self.head = temp
    
    def insertAtBeginning(self,value): # insert new node at the beginning of linkedlist
        temp = node(value)
        if(self.head != None):
            temp.next = self.head
            self.head = temp
        else:
            self.head = temp
    
    def insertAtPosition(self,value,x): # insert new node after the node with value x
        temp = node(value)
        if(self.head != None):
            t1 = self.head
            while(t1 != None):
                if(t1.data == x):
                    temp.next = t1.next
                    t1.next = temp
                    break
                t1 = t1.next

    def deleteNode(self,x): # delete the node with value x
        t1 = self.head
        prev = t1
        if(t1.data == x):
            self.head = t1.next
        while(t1.next != None):
            if(t1.data == x):
                prev.next = t1.next
                break
            prev = t1
            t1 = t1.next
        if(t1.data == x): # to delete the last node
            prev.next = None # why prev.next = None ? because we have to make the next part of previous node as null
        
            
    def Display(self):
        t1 = self.head
        while(t1 != None):
            print(t1.data, end=" -> ")
            t1 = t1.next
        print("None")

obj = SingleLinkedList() # create an object of SingleLinkedList class
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeginning(5)
obj.insertAtPosition(15,10)
obj.deleteNode(20)
obj.deleteNode(30)
obj.deleteNode(5)
obj.Display()