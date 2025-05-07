class Circular_queue():
     def __init__ (self,maxSize):
          self.items=maxSize * [None]
          self.maxSize=maxSize
          self.start=-1
          self.top=-1

     def __str__(self):
          values=[str(x) for x in self.items]
          return " ".join(values)
     
     def isfull(self):
          if self.top+1==self.start:
               return True
          elif self.start==0 and self.top+1==self.maxSize:
               return True
          else:
               return False
     def isEmpty(self):
          if self.top==-1:
               return True
          else:
               return False
     def enqueue(self,value):
          if not self.isfull():
               if self.isEmpty():
                    self.start=0
                    self.top=0
                    self.items[0]=value
               else:
                    if self.top+1==self.maxSize:
                         self.top=0
                    else:
                         self.top+=1
                    self.items[self.top]=value
               return "value added"
          else:
               return "the circular queue is full"
          
     def dequeue(self):
          if not self.isEmpty():
               self.items[self.start]=None
               ele=self.items[self.start]
               if self.start==self.top:
                    self.start=-1
                    self.top=-1
               elif self.start+1==self.maxSize:
                    self.start=0
               else:
                    self.start+=1
               return ele
          
     def peek(self):
          if not self.isEmpty():
               return self.items[self.start]
     
     def delete(self):
          self.items=self.maxSize*[None]
          self.top=-1
          self.start=-1
          

     
test=Circular_queue(3)
# print(test.isEmpty())
print(test.enqueue(12))
print(test.enqueue(12))
print(test.enqueue(15))
print(test.enqueue(100))
print(test.isfull())
print(test.dequeue())
print(test.enqueue(25))
print(test.enqueue(5))
# print(test.dequeue())
# print(test.dequeue())
print(test.isfull())
print(test.isEmpty())
print(test.peek())
test.delete()


# print(test.isEmpty())
print(test)



          

     