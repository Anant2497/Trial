#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip


# In[2]:


pip install mysql.connector


# In[10]:


import mysql.connector


# In[22]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# In[25]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="practise"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[33]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="practise"
)

mycursor = mydb.cursor()
sql = "INSERT INTO department (Customer_name, Customer_id, Open_date, Last_Consulted_Date, Vacination _TYPE, Dr_name, State, Country, DOB, Customer_active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
val = [
    ("Alex","123457","20101012","20121013","MVD","Paul","SA","USA","6031987","A"),
    ("John","123458","20101012","20121013","MVD","Paul","TN","IND","06031987","A")
]

mycursor.executemany(sql, val)

mydb.commit()


print(mycursor.rowcount,"Records Inserted")


# In[ ]:





# In[ ]:




