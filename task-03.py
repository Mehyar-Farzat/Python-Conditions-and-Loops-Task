# Python Conditions
------------------
x = 10
y = 15
if x > 15:
    print('x bigger than y')
else:
    print('x smaller than y')
x smaller than y
-----------------------------
x = 2
y = 3
z = 4
if all(x==2 , y==3 , z===4):
    print('true')
true
----------------------------
x = 2
y = 3
z = 4
if (x==2 and y==3 and z==4) :
    print('true)
true
---------------------------
x = 2
y = 3
z = 4
if (x==1 or y==3 or z==5) :
    print('true)
true
---------------------------
x = 2
y = 3
z = 4
if any(x==1 , y==3 , z==5) :
    print('true)
true
--------------------------
          
If we need all the conditions to be true we will use all
----------------------------
          
What is the differences between if , elif ?

The main difference between them is that if statements are
independent of each other while elif statements are
dependent on the previous if statement.

x = 5

if x > 10:
    print("x is greater than 10")
    
elif x > 7:
    print("x is greater than 7")
    
elif x > 3:
    print("x is greater than 3")
x is greater than 3
----------------------------------------

What is the differences between elif else ?

The main difference between elif and else is that elif statements
are used to execute multiple conditional statements while else statements
are used to execute a single conditional statement when none of the previous
conditions are true.

x = 5

if x > 10:
    print("x is greater than 10")
    
elif x > 7:
    print("x is greater than 7")
    
else:
    print("x is less than or equal to 7")
-----------------------------------------------

Can we use more than one elif ?

Yes, we can use multiple elif statements in Python.

x = 5

if x > 10:
    print("x is greater than 10")
    
elif x > 7:
    print("x is greater than 7")
    
elif x > 5:
    print("x is greater than 5")
    
else:
    print("x is less than or equal to 5")
-----------------------------------------------

Can we use more than one else in python ?

No, we can’t use more than one else statement in Python.

x = 5

if x > 10:
    print("x is greater than 10")
    
elif x > 7:
    print("x is greater than 7")
    
else:
    print("x is less than or equal to 7")
------------------------------------------------
write s simple ternary operator

x = 5

print("x is greater than 10") if x > 10 else "x is less than or equal to 10"
-------------------------------------------------

In elif , python will check all the conditions no matter what ?

No, Python will only check the conditions in the elif statements
if the previous conditions are false.
-------------------------------------------------

in elif we use else for ... ?

we use an else statement after an if or elif statement
to execute a block of code if none of the conditions are true.
-------------------------------------------------

 if we have this list [2,4,6,8,10] :

# 1- check to see if 4 in this list or not ?

a = [2, 4, 6, 8, 10]

if 4 in a:
    print("4 is in the list")
    
else:
    print("4 is not in the list")

# 2- check to see if 4 and 6 in this list on not ?

Yes, we can check if multiple elements are in a list in Python

my_list = [2, 4, 6, 8, 10]

if 4 in my_list and 6 in my_list:
    print('4 and 6 are both in the list')
    
else:
    print('Either 4 and 6 is not in the list')

# 3- check to see if 3 or 6 in this list ?

s = [2, 4, 6, 8, 10]

if 3 in s or 6 in s:
    print("Either 3 or 6 is in the list")
    
else:
    print("Either 3 or 6 is in the list")

# 4- check to see if 2 , 4 and 5 in this list ?

z = [2, 4, 6, 8, 10]

if all([2, 4, 5]) in z :
    print("All of the elements are in the list")
    
else:
    print("At least one of the elements is not in the list")
--------------------------------------------------------------------









