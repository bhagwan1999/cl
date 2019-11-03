#!/usr/bin/env python
# coding: utf-8

# In[68]:


import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
from sklearn.metrics import accuracy_score


# In[69]:


X = np.array([[1,2],
             [2,4],
             [1.5,1.8],
             [8,8],
             [10,4.6],
             [9,11],
              [11,13]])

#labels

y = [0,0,0,1,1,1,1]


# In[70]:


plt.scatter(X[:,0],X[:,1])


# In[71]:


clf=svm.SVC(kernel='linear')
clf.fit(X,y)


# In[72]:


print("Prediction of target for 3,3 values:")
t= clf.predict([[3,3]])
print(t)


# In[73]:


x_test = np.array([
    [1,1],
    [11,11],
    [2,1]
])
y_test=[0,1,0]
predicted = clf.predict(x_test)
k=accuracy_score(y_test,predicted)
print(' Test accuracy is :')
print(k)


# In[74]:


w=clf.coef_[0]
print(w)


# In[75]:


a = -w[0] / w[1]

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]
h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.legend()
plt.show()

