class Stack:
     def __init__(self,maxsize):
          self.list=[]
          self.maxsize=maxsize
     
     def __str__(self):
          values=[str(x) for x in reversed(self.list)]
          return '\n'.join(values)
     
     def isEmpty(self):
          if self.list==[]:
               return True
          else:
               return False
     
     def isFull(self):
          if len(self.list)==self.maxsize:
               return True
          else:
               return False
          
     def push(self,val):
          if not self.isFull:
               self.list.append(val)
          else:
               print("stack is full")
     
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