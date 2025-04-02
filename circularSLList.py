class Node:
     def __init__(self,value):
          self.value=value
          self.next=None
class CSinglyLinkedList:
     # def __init__(self,value):
     #      new_node=Node(value)
     #      new_node.next=new_node
     #      self.head=new_node
     #      self.tail=new_node
     #      self.length=1
     def __init__(self):
          self.head=None
          self.tail=None
          self.length=0


     def __str__(self):
          result="v-"
          temp=self.head
          while temp is not self.tail:
               result+=f"{temp.value}->"
               temp=temp.next
          result+=f"{self.tail.value}-^"
          for _ in range(self.length+2):
               print('<-' ,end=" ")
          print()
          return result

          

     def append(self,value):
          new_node=Node(value)
          if self.length==0:
               self.head=new_node
               self.tail=new_node
               new_node.next=new_node
          else:
               self.tail.next=new_node
               new_node.next=self.head
               self.tail=new_node
          self.length+=1

     def prepand(self,value):
          new_node=Node(value)
          if self.length==0:
               self.head=new_node
               self.tail=new_node
               new_node.next=new_node
          else:
               new_node.next=self.head
               self.head=new_node
               self.tail.next=new_node
          self.length+=1

     def insert(self,idx,value):
          if idx==0:
               self.prepand(value)
          else:
               temp=self.head
               new_node=Node(value)
               for _ in range(idx-1):
                    temp=temp.next
               new_node.next=temp.next
               temp.next=new_node
          self.length+=1
     
     def traverse(self):
          temp=self.head
          for _ in range(self.length):
               print(temp.value)     
               temp=temp.next


     def search(self,val):
          temp=self.head
          for i in range(self.length):
               if temp.value==val:
                    return i
               temp=temp.next

     def get(self,idx):
          if idx < 0 or idx>=self.length:
               return None
          temp=self.head
          for _ in range(idx):
               temp=temp.next
          return temp

     def set(self,idx,val):
          node=self.get(idx)
          if node is None:
               return False
          node.value=val
          return True

     def popfirst(self):
          if self.length==0:
               return 
          poped=self.head
          if self.length==1:
               self.head=None
               self.tail=None
          else:
               self.head=self.head.next
               self.tail.next=self.head
          poped.next=None
          self.length-=1
          return poped
     
     def pop(self):
          if self.length==0:
               return
          if self.length==1:
               poped=self.head
               self.head=None
               self.tail=None
               poped.next=None
               return poped   
          temp=self.head
          while temp.next is not self .tail:
               temp=temp.next
          temp.next=temp
          poped=self.tail
          self.tail=temp
          poped.next=None
          self.length-=1
          return poped
     


     def remove(self,idx):
          if idx<0 or idx>=self.length:
               return None
          elif idx==0:
               return self.popfirst()
          elif idx==self.length-1:
               return self.pop()
          prevnode=self.get(idx-1)
          popednode=prevnode.next
          prevnode.next=popednode.next
          popednode.next=None
          self.length-=1
          return popednode
     
     def delete(self):
          if self.length==0:
               return
          self.tail.next=None
          self.head=None
          self.tail=None
          self.length=0





csll=CSinglyLinkedList()
csll.append(10)
# csll.append(20)
# csll.append(30)
# csll.prepand(0)
# csll.prepand(1)
# csll.prepand(2)
# csll.insert(3,42)
# print(csll)
csll.traverse()
# print(csll.search(10))
# csll.set(6,50)
# print(csll.popfirst().value)
print(csll.remove(10))
# print(csll.head.value)
# print(csll.tail.value)
# print(csll.head.next.next.next.next.value)
# print(csll)


          