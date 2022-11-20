#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#prime numbers between 100 and 200


# In[11]:


for num in range(100,200):
    if all(num%i!=0 for i in range(2,num)):
        print(num)


# In[ ]:


#sort the elements in a list


# In[17]:


l=[1,2,3,8,9,5,4,7,6]
l.sort(reverse=True)
print(l)


# In[ ]:


#without using list.sort() in descending order


# In[16]:


data_list=[1,9,8,4,3,6,5,7,2]
new_list=[]
while data_list:
    min=data_list[0]
    for x in data_list:
        if x>min:
            min=x
    new_list.append(min)
    data_list.remove(min)
print(new_list)


# In[ ]:


#fibonacci series


# In[23]:


def fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fun(n-1)+fun(n-2)
for i in range(0,5):
    print(fun(i))


# In[ ]:


#reversing list


# In[25]:


list=[1,2,3,6,5]
rev=list[::-1]
print(rev)


# In[26]:


list=[10,34,23,78]
def rev(list):
    return list[::-1]
rev(list)


# In[ ]:


#palindrome or not


# In[28]:


def pal(num):
    x1=num[::-1]
    if x1==num:
        print("palindrome")
    else:
        print("not palindrome")
        
print(pal("madam"))


# In[ ]:


#set of duplicates in a list


# In[36]:


list=[8,9,9,4,5,6,5,2,8,4,6]
print(set([x for x in list if list.count(x)>1]))


# In[ ]:


#countng no of words


# In[34]:


s=" My name is Mitta Sandhya Rani"
print(len(s.split()))


# In[ ]:


#search agiven ele x in arr[]


# In[40]:


def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    print("not present in the list")
l=[1,2,3,4,5,6,7]
search(l,4)


# In[55]:


def binary_search(array,target):
    lower=0
    upper=len(array)
    while lower<upper:
        x=lower+(upper-lower)//2
        val=array[x]
        if target==val:
            return x
        elif target>val:
            if lower==x:
                break
            lower=x
        elif target<val:
            upper=x
            
            
binary_search(1,6)
            


# In[ ]:




