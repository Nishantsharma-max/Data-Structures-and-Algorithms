class Node:
     def __init__(self,value):
          self.prev=None
          self.value=value
          self.next=None

class DoublyLinkedList:
     def __init__(self):
          self.head=None
          self.tail=None
          self.length=0

     def __str__(self):
          temp=self.head
          res='None<-'
          while temp:
               res+=str(temp.value)+'<->'
               temp=temp.next
          
          return res[:-3]+'->None'


     def append(self,val):
          newnode=Node(val)
          if self.length==0:
               self.head=newnode
               self.tail=newnode
          else:
               self.tail.next=newnode
               newnode.prev=self.tail
               self.tail=self.tail.next
          self.length+=1

     def prepend(self,val):
          newnode=Node(val)
          if self.length==0:
               self.head=newnode
               self.tail=newnode
          else:
               newnode.next=self.head
               self.head.prev=newnode
               self.head=self.head.prev
          self.length+=1

     def traverse(self):
          temp=self.head
          while temp:
               print(temp.value,end=" ")
               temp=temp.next
     def reversetraverse(self):
          temp=self.tail
          while temp:
               print(temp.value,end=" ")
               temp=temp.prev

     def search(self,val):
          temphead=self.head
          while temphead:
               if temphead.value==val:
                    return True
               temphead=temphead.next
          return False
         
          



dll=DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.prepend(40)
dll.prepend(40)
dll.prepend(40)
print(dll)
dll.traverse()
print()
dll.reversetraverse()
print(dll.search(40))