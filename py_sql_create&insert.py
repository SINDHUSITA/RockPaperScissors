#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyodbc')


# In[148]:


import pandas as pd
import pyodbc


# In[149]:


server = 'SINUGANTI-LT' # your local server name 
database = 'EYBadgeMetrics'  # database name that is stored in server


# In[150]:


connection = pyodbc.connect('driver={SQL Server};server=SINUGANTI-LT;database=testDb')
cursor = connection.cursor()
cursor


# In[8]:


cursor.execute('''CREATE DATABASE mydatabase''')


# In[53]:


cursor.execute('''

               CREATE TABLE People
               (
               Name nvarchar(50),
               Age int,
               City nvarchar(50)
               )

               ''')


# In[64]:


connection.commit()


# In[ ]:


query='select * from ;'
pd.read_sql(query,connection)


# In[47]:





# In[139]:


data = pd.read_excel('sampleData.xlsx')


# In[19]:


for i in data.dtypes:
    print(match_types[str(i)])


# In[12]:


match_types = {'int64':'int', 'float64':'FLOAT','object':'varchar(100)'}


# In[13]:


match_types['int64']


# In[51]:


create_query += ')'


# In[62]:


create_query = 'create table sampleTable ('
for i in range(len(names)):
    create_query += names[i] + ' ' + match_types[types[i]] + ','
create_query = create_query[:-1]
create_query += ');'
create_query


# In[34]:


types = [str(i) for i in data.dtypes]


# In[60]:


types = [str(i) for i in data.dtypes]
names = [str(i) for i in data.columns]


# In[105]:


from tqdm import tqdm
for i in tqdm(range(data.shape[0])):
    pass
# for i in range(len(names)):
#     print(names[i])


# In[80]:


data.stringBig.apply(lambda x: "'"+x+"'")


# In[129]:


data.stringBig = data.stringBig.str.replace("'"," ")
data.stringBig = data.stringBig.apply(lambda x: "'"+x+"'")
data.name = data.name.apply(lambda x: "'"+x+"'")
data.idk = data.idk.apply(lambda x: "'"+x+"'")
data.department = data.department.apply(lambda x: "'"+x+"'")
data.fillna('NULL', inplace=True)


# In[50]:


create_query = create_query[:-1]


# In[144]:


data = pd.read_excel('sampleData.xlsx')
data.fillna('NULL', inplace=True)
for i in range(len(names)):
    if(types[i]=='object'):
        data[names[i]] = data[names[i]].str.replace("'"," ")
        data[names[i]] = data[names[i]].apply(lambda x: "'"+x+"'")


# In[63]:


cursor.execute(create_query)


# In[65]:


data.stringBig.str.replace(',','')


# In[84]:


data.head(2)


# In[159]:


insert_query = '''insert into sampleTable values(NULL,'1.7 Foot Com---@88%%pact & "Cube", Office Refrigera','Muhammed MacIntyre',3,-213.25,38.94,35,'Nunavut','Storage & Organization',0.8)'''
cursor.execute(insert_query)
connection.commit()


# In[145]:


print('total rows: ', data.shape[0])
fc = []
for i in range(data.shape[0]):
    insert_query = 'insert into sampleTable values('
    for j in data.values[i]:
        insert_query += str(j) + ','
    insert_query = insert_query[:-1]
    insert_query += ');'
    try:
        cursor.execute(insert_query)
        connection.commit()
    except:
        fc.append(insert_query)
# print('failed\n',fc)


# In[167]:


s = 'sinduh hkl'
s.replace(' ', '_')


# In[100]:


get_ipython().run_cell_magic('capture', '', 'from tqdm import tqdm_notebook as tqdm\ntqdm().pandas()')


# In[162]:


data = pd.read_excel('sample2.xls')
data.dtypes


# In[177]:


match_types = {'int64':'int', 'float64':'FLOAT','object':'varchar(100)','datetime64[ns]':'varchar(20)'}
data = pd.read_excel('sample2.xls')
types = [str(i) for i in data.dtypes]
names_c = [str(i).replace(' ', '_') for i in data.columns]
names = [str(i) for i in data.columns]

create_query = 'create table sampleTable2 ('
for i in range(len(names)):
    create_query += names_c[i] + ' ' + match_types[types[i]] + ','
create_query = create_query[:-1]
create_query += ');'
print(create_query)
cursor.execute(create_query)
connection.commit()

data.fillna('NULL', inplace=True)
for i in range(len(names)):
    if(types[i]=='object'):
        data[names[i]] = data[names[i]].str.replace("'","''")
        data[names[i]] = data[names[i]].apply(lambda x: "'"+x+"'")
for i in range(len(names)):
    if(types[i] not in ['object','int64','float64']):
        data[names[i]] = data[names[i]].apply(lambda x: "'"+str(x)+"'")
print('total rows: ', data.shape[0])

fc = []
for i in range(data.shape[0]):
    insert_query = 'insert into sampleTable2 values('
    for j in data.values[i]:
        insert_query += str(j) + ','
    insert_query = insert_query[:-1]
    insert_query += ');'
    try:
        cursor.execute(insert_query)
        connection.commit()
    except:
        fc.append(insert_query)
print('number of failed queries  :',len(fc))


# In[171]:


fc[0]


# In[ ]:




