# string is a collecgtion of charcters whoch are specified in quotations
"""
a =  "welcome to LeveluP"
      0  1  2  3  4  5  6     +ve Indexing
#     L  e  v  e  l  U  P
      -7 -6 -5 -4 -3 -2 -1    -Ve Indexing                   
"""

a = "LevelUP"
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[-7])
print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])
print(a[-4])

print(len(a))

b = " Happy  Birthday "
print(b)
c=(b.strip()) # it removes spaces in the start or at the end

print(c.lower())

print(c.upper())

d = " new, day"
print(d)
print(d.replace("new","old"))

print(d.split(","))

f= "new" in d
print(f)

f= "new1" in d
print(f)

# Concatenate ( combine to strings " +")

a = "welcome"
b = "to"
c = "LevelUP"

print(a+' '+b+' '+c)

#age = 24
#com = " my name is raju, i am " + age
#print (com)

age = 24
com = " my name is raju, i am {}"
print (com.format(age))

# 1) Capitalize() First letter in the string will become uppercase

a = "today is good day"
print(a.capitalize())
print(a)

# 2) Casefold()
a = "HAPPY  BIRTHDAY"
print(a.casefold())

# 3) center

a = "levelup"
print(a.center(20))
print(a.center(40))
print(a.center(60))
print(a.center(80))

# 4) count this is used to count howmany times a value is repeated in a string

a = " welcome to levelup i am learing python in levelup i go to levelup everyday"

print(a.count("a"))

# 5) endswith()

print(a.endswith("."))

# 6) expandtabs

a = "HAPPY/tBIRTHDAY"
print(a.expandtabs(10))
print(a.expandtabs(3))
print(a.expandtabs(4))
print(a.expandtabs(5))
print(a.expandtabs(6))

# 7) find()

a = "welcome to levelup i am learing python in levelup i go to levelup everyday"

print(a.find("welcome"))
print(a.find("levelup"))

#8 format()

v = "for onlr {price:2f} dollers"
print(v.format(price= 87))


#9 Index()
a = "welco12me t12o levelu12p 12i am12 leari12ng python12 in12 levelup12 i12 go12 to12 levelup12 everyday12"
#print(a.index("welcome"))

#10 isalnum()
a = "12"   
print(a.isalnum())

# 11 isdigit()

print(a.isdigit())

# 12 islower

a = "Welcome to levelup i am learing python in levelup i go to levelup everyday"

print(a.islower())

# 13) isnumeric

a = "12345678"
b = "1234567a"

print(a.isnumeric())
print(b.isnumeric())

# 14) istitle

a = 'I Am New To Python'
b = 'I Am new To Python'

print(a.istitle())
print(b.istitle())

# 15) isupper

a = "I AM NEW TO PYTHON"
b = 'I Am new To Python'

print(a.isupper())
print(b.isupper())












    

    












