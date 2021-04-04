import numpy as np
from random import randint
import math

sample=100000
x_1=x_2=x_3=x_4=x_5=1 #Defining values of radom variables
#list[5]=[x_1,x_2,x_3,x_4,x_5]
count1=count2=count3=count4=count5=0
i=0
while i<sample:
  index_of_list = np.random.randint(5)
  if index_of_list==0:#counting number of x_1
    count1+=1
  if index_of_list==1:#counting numberof x_2
      count2+=1
  if index_of_list==2:#counting numberof x_3
    count3+=1
  if index_of_list==3:#counting numberof x_4
    count4+=1
  if index_of_list==4:#counting numberof x_5
    count5+=1
  
  i+=1

pr1=count1/sample#probability of x_1
pr2=count2/sample#probability of x_2
pr3=count3/sample#probability of x_3
pr4=count4/sample#probability of x_4
pr5=count5/sample#probability of x_5
pr1

import numpy as np
from random import randint
import math

sample=100000 #Here I am assuming that there are only 5 random values of random variable X.
x_1=x_2=x_3=x_4=x_5=1 
#Assume a list;lst[5]=[x_1,x_2,x_3,x_4,x_5]
count1=count2=count3=count4=count5=0
i=0
while i<sample:
  index_of_lst = np.random.randint(5)
  if index_of_lst==0:#counting number of x_1
    count1+=1
  if index_of_lst==1:#counting numberof x_2
      count2+=1
  if index_of_lst==2:#counting numberof x_3
    count3+=1
  if index_of_lst==3:#counting numberof x_4
    count4+=1
  if index_of_lst==4:#counting numberof x_5
    count5+=1
  
  i+=1

pr1=count1/sample#probability of x_1
pr2=count2/sample#probability of x_2
pr3=count3/sample#probability of x_3
pr4=count4/sample#probability of x_4
pr5=count5/sample#probability of x_5
Ex=math.pow(x_1,100)*pr1+math.pow(x_2,100)*pr2+math.pow(x_3,100)*pr3+math.pow(x_4,100)*pr4+math.pow(x_5,100)*pr5
print(f"Expectation value of X^100= {Ex}")

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[14]:


#Here i will be creating a list'num' which consist of 6 element using randint function(which used for obtaining number from
#1 to 6 with equal probability) ,i will be repeating this process for 100000 times and will be counting the lists which statisfy
# 2 condition 1)list last number should be 6 2) count of total 6 in the list should be 3.The list which statisfy the above 
#criteria will be counted and will be divided with 100000
z=0
count=0
num=1
while z<100000:
    num.append(randint(1,5))
    if num==5:
        count=count+1
    z=z+1


# In[17]:


print(f"probability of obtaining third six in the sixth throw of the die,{count/100000}")


# In[ ]: