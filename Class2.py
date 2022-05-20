#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, element):
        self.items.append(element)
        
    def pop(self):
        return self.items.pop()
    
    def get_size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []


# In[2]:


numbers = [1, 2, 3, 4, 5]

def print_inverted_list(my_collection):
    stack = Stack()
    for number in numbers:
        print("Pushing %s" % number)
        stack.push(number)
    while not stack.is_empty():
        number = stack.pop()
        print ("Got %s from pop result" % number)

print_inverted_list(numbers)


# # Mini Challenge 1
# ### Use a stack to invert a string.
# #### Given "mystring" as a parameter, invert it.
# ```
# Examples:
#     Rafeal -> leafaR
#     Collin -> nilloC
# ```

# In[3]:


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
        
    return rev_str

stack = Stack()
input_str = "!ti gid uoy naC"
print(reverse_string(stack, input_str))


# In[4]:


class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, element):
        self.items.append(element)
        
    def dequeue(self):
        self.items.pop(0)
    
    def get_size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []


# # Mini Challenge 2
# ### Create a queue from 2 stacks.
# #### Create a class named Queue2Stacks that consists of only 2 stacks.
# >The Queue2Stacks class should maintain the ordering principle of a Queue while being made up of two stacks (as its only class attributes)
# 
# ````Example (of ordering principle):
# 
# myqueue = Queue2Stacks()
# myqueue.enqueue("A")
# myqueue.enqueue("B")
# myqueue.enqueue("C")
# 
# assert myqueue.dequeue() == "A"
# assert myqueue.dequeue() == "B"
# assert myqueue.dequeue() == "C"
# 
# ````

# In[18]:


class Queue2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, item):
        self.stack1.append(item)
        
    def dequeue(self):
        if self.stack2 == []:
            item = self.stack1.pop()
            self.stack2.append(item)


# In[12]:


myqueue = Queue2Stacks()
for i in range(5):
    myqueue.enqueue(i)

for _ in range(5):
    item = myqueue.dequeue()
    print(item)


# In[ ]:




