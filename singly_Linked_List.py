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

     def traverse(self):
          current=self.Head
          while current is not None:
               print(current.value,end="->")
               current=current.next


     def search(self,target):
          current=self.Head
          idx=-1
          while current is not None:
               idx+=1
               if target==current.value:
                    return idx
               current=current.next
          return -1
          
     def get(self,idx):
          current=self.Head
          for _ in range(idx):
               if current.next is not None:
                    current=current.next
               else:
                    return None
          return current
     
     def set(self,idx,value):
          node=self.get(idx)
          if node:
               node.value=value
               return True
          else:
               return False
          
     def pop_first(self):
          if self.length==0:
               return None
          if self.length==1:
               self.Tail=None
          temp=self.Head
          self.Head=self.Head.next
          temp.next=None
          self.length-=1
          return temp
     
     def pop(self):
          if self.length==0:
               return None
          if self.length==1:
               pop=self.Head
               self.Head=None
               self.Tail=None
               self.length-=1
               return pop
          else:
               pop_node=self.Tail
               temp=self.Head
               while temp.next is not self.Tail:
                    temp=temp.next
               self.Tail=temp
               temp.next=None
               self.length-=1
               return pop_node


     def remove(self,index):
          if index>=self.length or index<0:
               return None
          if index==0:
               temp=self.pop_first()
               return temp
          else:
               prev=self.get(index-1)
               rem=prev.next
               prev.next=prev.next.next
               rem.next=None
               self.length-=1
               return rem
     def delete_all(self):
          self.Head=None
          self.Tail=None
          self.length=0
     
     def reverse(self):
        temp=self.head
        last=self.tail
        for i in range(self.length-1,0,-1):
            for j in range(i-1):
                temp=temp.next
            self.append(temp.value)
            temp=self.head
        self.head=last

               



new_linked_list=LinkedList()
new_linked_list.prepend(0)
new_linked_list.append(10)
new_linked_list.prepend(2)
new_linked_list.append(23)
new_linked_list.insert(4,5)

new_linked_list.traverse()
print()
print(new_linked_list.remove(6))
# print(new_linked_list.remove(0))
# print(new_linked_list.remove(0))
new_linked_list.delete_all()
new_linked_list.traverse()




