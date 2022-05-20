#!/usr/bin/env python
# coding: utf-8

# In[1]:


for letter in "Hello World":
    print(letter)


# # PROBLEM 1
# ### Given 2 Strings (string_a and string_b) let's check whether or not they are anagrams of each other given the following criteria:
# 
# > Two strings are only anagrams of each other if all conditions below are met:
# > * They must be exactly the same length.
# > * They must use exactly the same characters (no more, no less).
# 
# ```
# Example(s): cars and scar, heart and earth, etc.
# ```

# In[13]:


def test(st1, st2):
    
    st1 = st1.replace(" ", "").lower()
    st2 = st2.replace(" ", "").lower()
    
    a = {}
    for x in st1:
        if x not in a:
            a[x] = 0
        a[x] += 1
    
    e = {}
    for x in st2:
        if x not in e:
            e[x] = 0
        e[x] += 1
        
    return a == e

print(test('wand', 'dawn'))
print(test('Wand', 'dawn'))
print(test('wan d', 'dawn '))
print(test('wands', 'd awn '))
            


# In[ ]:




