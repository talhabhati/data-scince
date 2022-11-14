#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('talha')


# In[2]:


'''thi 
is 
a bok
'''


# In[3]:


print('ksdds\n')      #next line ma lana k liye \n ha
print('utd\n')


# In[5]:


'''sdfjf\n 
akljdjad\n
sdfsdf'''


# In[6]:


print(3%3)


# In[13]:


name='mustansar'
name.count('m')


# In[16]:


name.find('s')


# In[21]:


name[1:8:2]    #list ka programe


# In[24]:


len(name)


# In[25]:


name.replace('s','g')


# In[30]:


dummy=['apple','orange',4,True]
dummy[1:4]


# In[29]:


dummy[2:]   #


# In[64]:


l1=[1,3,5,2,4,6]    #irregular array 
l1.sort()        #sort usko arrange karega
l1


# In[65]:


l1.insert(4,9)     #4 index pe 9 layega
l1


# In[66]:


l1.pop()     #last element nikalaga list ka
l1


# In[67]:


l1.remove(5)     # 5 agar hoa tu remove karega na hoa tu error dega
l1


# In[69]:


l1.index(9)     #index 4 pe konsa elemnt ha btaiga


# In[53]:


#tuple ka programme
#tuple immutable ha edit nhi hoga
#baqi is per .count   aur .inex  k programe laga kar bus dekh sate ha
t1=(1,2,3)
t1.count(3)


# In[57]:


#kisi bhi element ki location maloom karna k liya
t1.index(3)  # index 1 se shoro hoga is ma 


# In[82]:


#dictioinary and object
# yha key ko '' k ander hi likhna ha
dict={'key' :'value',
      'gender' : 'male',
      'mark' : 32,
     'list' : [1,2,3]}

dict['mark']    #jo bhi key likho ga uski value ayegi


# In[86]:


dict.items()    #sari items means key with values dega


# In[85]:


dict.keys()     #sirf keys dega dictionary ki


# In[88]:


dict.values()    #dictionary ki sari values dega


# In[94]:


dict.update({'name':'ali'})  #new item add karega dictionary ma
dict


# In[95]:


dict.get('name')     # key dekar uski value lega


# In[98]:


#sets programme
s={1,2,3,4}
s.pop()       #reove 1st element of set


# In[99]:


s.remove(4)   # remove 4 from set
s


# In[100]:


s.union({78,34})   # s set ki new set se union karega


# In[103]:


set1={2,3,4,5,6}
s.intersection(set1)    # set1 ki s se intersection kaerwayega common element dega


# In[10]:


#conditional statement
a=21
if a<20:
    print('talha')
elif a>22:
    print('its ok')
else:
        print('value is not true')


# In[17]:


#while loop
i=0
while i<5:
    print('husnain')
    i=i+1


# In[20]:


#for loop is used for iteration in list ,tuples and dictionary
l2=[2,4,6,8,10,3]
for i in l2:
    print(i%2)


# In[26]:


for i in range(2,10):    #odd even alag kiye 2 se 17 tak
    if i%2==0:
        print(i)
    else:
        print('odd number')


# In[27]:


for i in range (1,8):
    if i%2==0:
        print('you too')
    elif i%2!=0:
        print('tooyou')
    else:
        break


# In[36]:


for i in range(1,5):
    
    if i==3:
        break   #jha 3 hoa i waha yeh loop beak hoga  print('i') if se pehla ha tu 3 bhi show hoga
    print(i)    #agar bad likha tu nhi hoga
       


# In[40]:


for i in range(1,7):
    if i==5:
        continue    #jha 5 ayega wah output nhi ayegi baqi sara loop chala ga
    else:
        print(i)


# In[43]:


#function
def mul(a,b):
    return a*b
mul(2,4)


# In[ ]:


# input and output
data=open(this.txt,'r')

