#!/usr/bin/env python
# coding: utf-8

# # PYTHON DICTIONARY 
# 
# ### It is a method in python by also a data structure. 
# #### It's a way for us to organize our data in a form that is has some different pros and cons in how we access it, 
# #### for example, with lists.
# 
# 
# 
# Well, let's see what a dictionary looks like. A dictionary? Well, look, something like this will have a key.And a value.

## And then another comma.And then another key.And another value.Let's decipher this.
## So I'm using curly brackets here, which denotes a dictionary.
## A dictionary is an unordered key value pair. What I mean by that unordered means that they are not right next to each other in memory.
# In[6]:


dictionary = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4   
}

print(dictionary) ## Example of how a dictionary works with the keys and values. 

dictionary = {
    "a" : [1,2,4,5],
    "b" : True,
    "c" : 3,
    "d" : "Hello"   
}
print(dictionary["a"]) ## Dictionary can be a list, strirng or boolean


# In[11]:


## Combining a dictionary and a list 
my_list = [
    {
    "a" : [1,2,4,5],
    "b" : True,
    "c" : 3,
    "d" : "Hello"   
    },
   
    {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4 
    },
    
    {    
    "ba" : [4,5,6,7],
    "bb" : False,
    "cc" : 4,
    "ed" : "Good"
    }
    
]
print (my_list[0]["a"][2])## Using list in dictionary


# In[12]:


## Dictionary keys need to have a special property. A key needs to be immutable.That is a key cannot change.

## And numbers booleans. I mean, this is a value that cannot change. A string, if you remember, is a value that cannot change.

## It's immutable. But a list, if you remember, can be changed, right?

dictionary = {
    123 : 1,
    "b" : 2,
    True : 3,
    "d" : 4   
}

print(dictionary)


# In[17]:


## Using the Get fuction to search for key or value in a dictionary 
user ={
    "name"   : "Nana Kwame",
    "amount" :  300
}
print(user.get("age")) ## The output none means we can access a key called age in the dictionary.
print(user.get("age", 32))


# In[25]:


## Method for searching using keys, values and items in python

user_list = {
    "basket" : 1,
    "b" : 2,
    True : 3,
    "hello" : 4   
}

print("basket" in  user_list.keys())
print("basket" in  user_list.values())
print(user_list.items()) ## items output everything in the dictionary


# In[30]:


## Updating a dictionary 
dictionary = {
    "basket" : 1,
    "b" : 2,
    True : 3,
    "age" : 4   
}
print (dictionary.update({"age" : 55})) ## Age got updated.
print(dictionary)
## But if.This was a key that doesn't exist, like pages and I click run.It will still update with a new key item. 
## So this is another really useful method.
print (dictionary.update({"ages" : 55}))
print(dictionary)


# In[ ]:




