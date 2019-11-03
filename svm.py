#!/usr/bin/env python
# coding: utf-8

# In[43]:


import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
from sklearn.metrics import accuracy_score
from matplotlib import style
style.use("ggplot")


# In[44]:


X = np.array([[1,2],
             [2,4],
             [1.5,1.8],
             [8,8],
             [10,4.6],
             [9,11],
              [11,13]])

#labels

y = [0,0,0,1,1,1,1]


# In[45]:


plt.scatter(X[:,0],X[:,1])


# In[49]:


clf=svm.SVC(kernel='linear')
clf.fit(X,y)


# In[50]:


print("Prediction of target for 0.58,0.76 values:")
t= clf.predict([[3,3]])
print(t)


# In[51]:


predicted = clf.predict(X)
k=accuracy_score(y,predicted)
print(' Training accuracy is :')
print(k)


# In[52]:


w=clf.coef_[0]
print(w)


# In[53]:


a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]
h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.legend()
plt.show()

