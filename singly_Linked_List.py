class Node:
     def __init__(self,value):
          self.value=value
          self.next=None


class LinkedList:
     def __init__(self):
          self.Head=None
          self.Tail=None
          self.length=0

     def __str__(self):
          result=""
          while self.Head is not None:
               result+=f"{self.Head.value}->"
               self.Head=self.Head.next
          return result

     
     def append(self,value):
          newNode=Node(value)
          if self.Head is not None:
               self.Tail.next=newNode
               self.Tail=newNode
          else:
               self.Head=newNode
               self.Tail=newNode
          self.length+=1

     def prepend(self,value):
          newNode=Node(value)
          if self.Head is not None:
               newNode.next=self.Head
               self.Head=newNode
          else:
               self.Head=newNode
               self.Tail=newNode
          self.length+=1

     def insert(self,index,value):
          if index==0:
               self.prepend(value)
          elif index==self.length:
               self.append(value)
          else:
               newNode=Node(value)
               tempnode=self.Head
               for _ in range(index-1):
                    tempnode=tempnode.next
               newNode.next=tempnode.next
               tempnode.next=newNode
               self.length+=1





new_linked_list=LinkedList()
new_linked_list.prepend(0)
# new_linked_list.append(10)
# new_linked_list.prepend(2)
# new_linked_list.append(23)
# new_linked_list.insert(4,5)


print(new_linked_list)
print(new_linked_list.length)

print(new_linked_list.Tail)
print(new_linked_list.Head)
