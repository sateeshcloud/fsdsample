"""# Day 3:-
# Recap:-
# 1) Data types
# 2) operators
# 3) Strings -> methods

# Agenda for today:-
# handling Strings
# Slicing Strings
# Operators

#Method :- Join

from xml.dom import xmlbuilder


new = ['Leareing', 'Python', 'is', 'very','easy']
a = print('2'.join(new))
print(a)

# Method ljust

myfavlang = 'python'

y = myfavlang.ljust(10)

print(y, "is my favourite language")

# lstrip = Removes the spaces to the left for sting

furit = "            watermalon            "
y = furit.lstrip()

print (" among the fruits i like ",y)

#partition()
#replace()
#rjust()
# rsplit()
#rstrip()
#lstrip()
#title()
# upper ()
# join
Capitalize()
casefold()
center()
count()
endswith()
expandtabs()
find()
Format()
Index()
isdigit()
isnull()
islower()
isalpnumer()
isnum()
istitle()
isupper()






new = " i practice python everyday in the morning"
x=new.partition("python")

print(x)

#replace()
#rjust()
# rsplit()
#rstrip()
#title()
# upper ()


new= " i like coding in python"
print(new.replace("python","Sql"))

#rfind() where that valse found last postion

new= " i learned python, i practiced python, i can code in python"
a = new.rfind("python")

print(a)

#rjust()
# rsplit()
#rstrip()
#title()
# upper ()

new = "Python"

x =new.rjust(50)
print(x, "is the easy language to learn")

# rsplit()
#rstrip()
#title()
# upper ()

a = "I, learned, python, today"

b=a.rsplit(",")

print(b)

#rstrip()
#title()
# upper ()
furit = "watermelon        "
y = furit.rstrip()

print (y," among the fruits i like ",)

#title()
# upper ()

w= " i learned python, i practiced python, i can code in python"
x=w.title()
print(x)

# upper ()

w= " i learned python, i practiced python, i can code in python"
x=w.upper()
print(x)

# Slicing in strings

a = "today is good day a head"
    # 12345678 

print(a[0])
print(a[0:5]) #today # not including the last index
print(a[4:8]) # y is 
print(a[:8])
print(a[8:])
print(a[:8] + a[8:])
print(a[:])

print (a[-1])
print(a[:-8])


a = "today is good day a head"
   # 02345 78 10
print(a[-9:-6])

print(a[0:15:5]) #tdy
a = "ghjgfghkjasfgkltftdyrdyfoviujhfgk"
print (len(a))

b= a[33:0:-1]

print(b)

b=a[::-1]"""

# sting Formatting
age = int(input( "please enter your age"))
name= input("pleae enter your name")

print("my age is {0} years".format(age))
print("my age is {0} years and my name is {1}".format(age,name))

print(" there are {0} days in {1} , {7}, {3}, {5}, {4}, {6}, and {2}".format(31,"jan","mar","may","jul","aug","oct","dec"))











































































       
       