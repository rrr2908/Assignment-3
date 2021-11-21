#!/usr/bin/env python
# coding: utf-8

# In[4]:


#  Write a Python function to sum all the numbers in a list.
def sum(num):
    res = 0
    for i in num:
        res = res + i
    return res
n = int(input("Enter the number of elements in array: "))
arr = []
for i in range(0, n):
    ele=int(input())
    arr.append(ele)
print(arr)
print(sum(arr))


# 

# In[3]:


# Write a Python program to reverse a string.
def my_function(x):
    return x[::-1]

mytxt = my_function(str(input()))

print(mytxt)


# In[8]:


def number(s):
    d = {"Upper_Case": 0, "Lower_Case": 0}
    for i in s:
        if i.isupper():
            d["Upper_Case"]= d["Upper_Case"] + 1
        elif i.islower():
            d["Lower_Case"] = d["Lower_Case"] + 1
    print("Upper Characters: ", d["Upper_Case"])
    print("Lower Characters: ", d["Lower_Case"])
    
s = str(input())
print(number(s))


# In[ ]:




