'''
Stack Data Structure:

Consider an example where we have some books lying on the floor:

A  B       C       D

Let's now organize thoose books in a stack:

D
C
B
A


----Any time we put something on the top of the stack we refer to that as " we push something on the top of the stack"

----Any time we take out an item from the top of the stack we refer to that that as "we pop something from the top of the stack"

'''
# IMPLEMNTATION OF THE STACK DATASTRUCTURE IN PYTHON:
# The constructor of this Stack class is going to modify a python list

class Stack():
     def __init__(self):
        self.items = []

     def push(self, item):
         self.items.append(item)     

     def pop(self):
         return self.items.pop()   

     def is_empty(self):
         return self.items == []

     def peek(self):
         if not self.is_empty():
             return self.items[-1]

     
     def get_stack(self):
         return self.items

       

# PUSH AND POP METHODS:

s = Stack()
s.push("A") 
s.push("B")             
print(s.get_stack())
s.push("C")
s.push(s.get_stack())
s.pop()
print(s.get_stack())

s = Stack()
print(s.is_empty())

print(s.peek())