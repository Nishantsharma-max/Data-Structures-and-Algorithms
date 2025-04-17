class Stack:
     def __init__(self):
          self.list=[]
     
     def __str__(self):
          values=[str(x) for x in reversed(self.list)]
          return '\n'.join(values)
     
     def isEmpty(self):
          if self.list==[]:
               return True
          else:
               return False
          
     def push(self,val):
          self.list.append(val)
     
     def pop(self):
          if self.isEmpty():
               print("stack is empty")
          else:
               val=self.list.pop()
               return val
     
     def peek(self):
          if self.isEmpty():
               print("stack is empty")
          else:
               return self.list[-1]
          
     def delete(self):
          self.list=[]
     

customstack=Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)


print(customstack)

