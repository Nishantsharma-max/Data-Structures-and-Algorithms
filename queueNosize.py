class Queue:
     def __init__(self):
        self.items = []
     
     def __str__(self):
          values = [str(x) for x in self.items]
          return ' '.join(values)

     def isEmpty(self):
          if self.items == []:
               return True
          else:
               return False

     def enqueue(self,value):
          self.items.append(value)

     def dequeue(self):
          if not self.isEmpty():
               removed=self.items.pop(0)
               return removed
     
     def peek(self):
          if not self.isEmpty():
               return self.items[0]

     def delete(self):
          self.items=None



myqueue=Queue()
print(myqueue.isEmpty())
myqueue.enqueue(10)
myqueue.enqueue(20)
myqueue.enqueue(30)
print(myqueue)
print(myqueue.dequeue())
print(myqueue)
print(myqueue.peek())
myqueue.delete()
print(myqueue.items)


          