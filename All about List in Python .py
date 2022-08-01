#!/usr/bin/env python
# coding: utf-8

# # # LIST METHOD 1
# 

# In[ ]:


#ADDING USING APPEND 
basket = [1,3,4,5,6]
basket.append(100) ## Using the appending method
new_list = basket  
print(new_list)


# In[ ]:





# In[9]:


#ADDING USING INSERT
basket = [1,3,4,5,6]
basket.insert(4,100) ## Using the inserting method
new_list = basket  
print(new_list)


# In[11]:


#ADDING EXTEND
basket = [1,3,4,5,6]
basket.extend([100,101]) ## Using the extend method. basically for looping over. 
new_list = basket  
print(new_list)


# In[12]:


# REMOVING USING POP
basket = [1,3,4,5,6]
basket.pop() ## which removes the last interger value of the variable basket
print(basket)


# In[13]:


# REMOVING USING POP
basket = [1,3,4,5,6]
basket.pop(0) ## we can use remove to delete based on the index from the list
print(basket)


# In[15]:


# REMOVING USING REMOVE
basket = [1,3,4,5,6]
basket.remove(3) ## which is used to remove based on the value we want to delete. 
print(basket)


# In[17]:


# REMOVING USING CLEAR
basket = [1,3,4,5,6]
basket.clear() ## Completely delete everything. 
print(basket)


# In[28]:


# INDEXING 
basket = ["a","b","c","d","e"]
print(basket.index("c"))

## Finding for keywords 
print("d" in basket) # it keeps you to search for items you are not sure if is part of the list

## COUNTING
print(basket.count ("d")) # it counts the number of times a value have occurred. 


# In[34]:


## SORT  
basket = ["a","x","c","d","e","b","m"]
basket.sort() ## sort Modifies the list as seen below
print(basket)


# In[35]:


## SORTED
basket = ["a","x","c","d","e","b","m"]
print(sorted(basket)) ## Sorted create a new different list as compared to sort
print(basket)


# In[36]:


## SORT AND REVERSE 
basket = ["a","x","c","d","e","b","m"]
basket.sort()
basket.reverse()
print(basket)


# In[39]:


## Range in list 
print(list(range(1,100)))


# In[41]:


## JOIN IN LIST 
sentence = "  "
new_sentence = sentence.join(["hi", "my name", "is", "Yaw"])
print(new_sentence)


# In[42]:


## Upacking in list 
a,b,c, *other, d = [1,2,4,5,6,7,8,9]
print (a)
print (b)
print (c)
print (other)
print (d)


# In[ ]:




