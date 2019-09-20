#!/usr/bin/env python
# coding: utf-8

# In[51]:


#this is a comment in python
#we can use python as a calculator

2+3 #prints 5
2.05+3 #converts int to float 5.05
f=100
f+_ # the sign _ stores the value of last printed expression

#operations with complex number
a=100+4J #J represents the complex part
b=200-2J
c=a+b
print(c)

10/2.2  #returns 4.545454545454545
round(10/2.2,2)  #returns 4.5
10//2.2 #returns 4 by omitting the fractional part

x=2**3 #returns 8
c=10%3 #1 modulus


# In[8]:


#PYTHON Strings


# In[21]:


'word' #same as writing "word"
'a sentence' #same as writing "a sentence"

'you shouldn\'t do this' #or write it in " " quote
# returns "you shouldn't do this"
#here \is known as escape character
#for a better result we can use print

print('you shouldn\'t do this') #returns you shouldn't do this without second quote

#sometimes we need the blackslash character itself 
#we can use the raw code then

print(r'C:\sondip\python')

print('my name is sondip\n i\'m a laravel developer') #/n used for new line
print("""for printing a long line
we can use three quotes
""")

print('''or for printing a long line
we can use three single quotes
''')


# In[22]:


#Simple operations on string


# In[69]:


s="Lecturer"
len(s)  #prints the length of a string 
name="sondip poul singh"
len(name) # returns 17 by taking the space in counting also
s[0] #prints L
s[-1] #prints r
s[len(s)-1] #prints r
s[0:3] #prints Lec(0,1,2 position)
s[-8:-1] # returns Lecturer but note that s[-1:-8] returns empty string
s[2:4] #returns ct
s[2:] #returns cturer
s[:4] #returns Lect
s[0:100] #no problem with that
s[100] #error out of range
#string is taken from the beginning position to less than the last position given 
#s[0]='B' returns error cause strings in python are immutable or cant be changed
#if needed we have to take another string to assign the updated value

new='J'+s[1:len(s)-1]  #'J'+s[1:]
new #Jecturer 


# In[44]:


#Concatenating strings


# In[65]:


x='python\n'
y=3*x
print(y) #prints 3 times python with new lines

p='data '
q='analysis'

p+q #data analysis

#two string literals concate automatically when variable is not included
'sus' 'moy'  #prints susmoy
print('susmoy ' 'sondip ' 'are brothers') #susmoy sondip are brothers(spaces added for better result view)

gram='goshai' #a variable
'pur' #a string literal

gram+'pur' #note gram'pur' returns error cause a string and a literal cant be added without + sign


# In[70]:


#several operations can be done on string as finding,manipulating,reversing etc
#those topics will be covered in details in next lessons


# In[ ]:




