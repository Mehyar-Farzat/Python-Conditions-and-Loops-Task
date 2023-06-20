# 1- print numbers from 0 to 10 using while

i = 0
while i <= 10:
    print(i)
    i += 1
-------------------------------

# 2- print numbers from 0 to 10 using for

for i in range(11):
    print(i)
-------------------------------
# 3- stop the loop if the number = 5

for i in range(11):
    if i == 5:
        break
    print(i)
-------------------------------
# 4- Skip the 5 iteration from print

for i in range(11):
    if i == 5:
        continue
    print(i)

-----------------------------------
# 5- Print multiplication table from 1 to 5

for n in range (1,6):
    for b in range (1,11):
        print(f'{n} * {b} =',n*b)
-----------------------------------
# 6- How to get numbers from 10 to 20 using range ?

for x in range(10,21):
    print(x)
-----------------------------------
# 7- How to get numbers from 10 to 100 with 3 at each step using range ?

for i in range(10, 100, 3):
    print(i)
-----------------------------------
# 8- Get a list of even numbers from 1 to 100 using for

for i in range(2, 101, 2):
    print(i)
-----------------------------------
# 9- et a list of even numbers from 1 to 100 using while

x = 2
while x <= 101:
    print(x)
    x +=2
----------------------------------
# 10- Get a list of even numbers from 1 to 100 using range

for x in range(1,101):
    if x%2==0:
        print(x)
----------------------------------

