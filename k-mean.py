#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import matplotlib.pyplot as plt


# In[93]:


x=np.array([[1,1],[2,2],[2,3],[2,5],[3,4],[3,2],[4,3],[2,1],[6,6],[7,6],[7,5],[6,7],[8,8] ])


# In[94]:


plt.scatter(x[:,0],x[:,1])


# In[96]:


k=2
centroids=[x[0],x[1]]


# In[97]:


epochs=500
for j in range(epochs):
    cluster1=[]
    cluster2=[]
    for i in range(x.shape[0]):
        d1=np.sqrt((x[i][0]-centroids[0][0])**2 + (x[i][1]-centroids[0][1])**2)
        d2=np.sqrt((x[i][0]-centroids[1][0])**2 + (x[i][1]-centroids[1][1])**2)
        if d1<d2:
            cluster1.append([x[i][0],x[i][1]])
        else:
            cluster2.append([x[i][0],x[i][1]])
    c1_x=0
    c1_y=0
    for i in range(np.shape(cluster1)[0]):
        c1_x=c1_x+cluster1[i][0]
        c1_y=c1_y+cluster1[i][1]
    avg_x=c1_x/np.shape(cluster1)[0]
    avg_y=c1_y/np.shape(cluster1)[0]
   
    min_=999
    for i in range(np.shape(cluster1)[0]):
        d=np.sqrt((cluster1[i][0]-avg_x)**2 + (cluster1[i][1]-avg_y)**2)
    
        if d<min_:
            min_=d
            centroids[0]=cluster1[i]
            
            
            
    c2_x=0
    c2_y=0
    for i in range(np.shape(cluster2)[0]):
        c2_x=c2_x+cluster2[i][0]
        c2_y=c2_y+cluster2[i][1]
    avg_x=c2_x/np.shape(cluster2)[0]
    avg_y=c2_y/np.shape(cluster2)[0]
    min_=9999
    for i in range(np.shape(cluster2)[0]):
        d=np.sqrt((cluster2[i][0]-avg_x)**2 + (cluster2[i][1]-avg_y)**2)
        if d<min_:
            min_=d
            centroids[1]=cluster2[i]  
        
    


# In[99]:


plt.scatter([row[0] for row in cluster1],[row[1] for row in cluster1])
plt.scatter([row[0] for row in cluster2],[row[1] for row in cluster2])
plt.scatter(centroids[0][0],centroids[0][1],color='black')
plt.scatter(centroids[1][0],centroids[1][1],color='black')

