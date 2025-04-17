class Node:
     def __init__(self,value):
          self.value=value
          self.next=None

class Linkedlist:
     def __init__(self):
          self.head=None

class Stack:
     def __init__(self):
          self.stacklinkedlist=Linkedlist()
     
     def isEmpty(self):
          if self.stacklinkedlist.head is None:
               return True
          else:
               return False
          
     def push(self,value):
          node=Node(value)
          if self.stacklinkedlist.head==None:
               self.stacklinkedlist.head=node
          else:
               node.next=self.stacklinkedlist.head
               self.stacklinkedlist.head=node

     def pop(self):
          if self.isEmpty():
               print('stack is empty')
          else:
               remove=self.stacklinkedlist.head
               self.stacklinkedlist.head=self.stacklinkedlist.head.next
               remove.next=None
               return remove.value
          
     def peek(self):
          if self.isEmpty():
               print('stack is empty')
          else:
               top=self.stacklinkedlist.head
               return top.value
          
     def delete(self):
          self.stacklinkedlist.head=None

          
customstack=Stack()
print(customstack.isEmpty())
          