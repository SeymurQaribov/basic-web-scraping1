#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


import bs4


# In[4]:


result = requests.get('http://www.example.com')


# In[5]:


type(result)


# In[7]:


result.text


# In[12]:


soup = bs4.BeautifulSoup(result.text,'lxml')


# In[13]:


soup


# In[14]:


soup.select('title')[0].getText()


# In[16]:


soup.select('p')[0].getText()


# In[4]:


res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')


# In[6]:


soup = bs4.BeautifulSoup(res.text,'lxml')


# In[7]:


soup


# In[8]:


first_item = soup.select('.toctext')[0]


# In[9]:


first_item


# In[15]:


for item in soup.select('.toctext'):
    print (item.text)


# In[19]:


ress = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')


# In[20]:


soup1 = bs4.BeautifulSoup(ress.text,'lxml')


# In[21]:


soup1


# In[23]:


soup.select('img')[0]


# In[26]:


computer = soup.select('.thumbimage')[0]


# In[ ]:





# < img
#     src = "//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Harvard_Mark_I_sign-up.agr.jpg/220px-Harvard_Mark_I_sign-up.agr.jpg">
# 

# In[34]:


computer['src']


# <img
#      src="//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Harvard_Mark_I_sign-up.agr.jpg/220px-Harvard_Mark_I_sign-up.agr.jpg">
#      
#      
#      

# In[36]:


image_ling = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Harvard_Mark_I_sign-up.agr.jpg/220px-Harvard_Mark_I_sign-up.agr.jpg')


# In[38]:


image_ling.content


# In[40]:


f = open('my_coputer.jpg','wb')


# In[41]:


f.write(image_ling.content)


# In[42]:


f.close()


# In[ ]:




