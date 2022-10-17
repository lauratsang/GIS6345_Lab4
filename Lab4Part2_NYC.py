#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[8]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[9]:


map1 = gis.map('New York City, NY')
map1


# In[10]:


# Item Added From Toolbar
# Title: New York City_s Green Spaces and Trees 2015_WFL1 | Type: Feature Service | Owner: jgaffud1
item = gis.content.get("a237b7072ba540b199a2ce2d3117d9ec")
item


# In[12]:


map1.add_layer(item)
map1

