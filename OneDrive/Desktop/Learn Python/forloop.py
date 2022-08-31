"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
promise = "I will finish the python loops module!"

for i in promise:
  print(i)
  if i == "w":
      break
  
  
from turtle import clear


number = "9,233;567;454,664 778;809"
separators = number[1::4]  

print(separators)

number= "8,9786870989;879;7892:79808,879.678879 098,4:44:"
separators=""

for char in number:
    if not char.isnumeric():
        separators =  separators + char
        print(separators)
print(separators)

values ="".join(char if char not in separators else " " for char in number).split()
print ([int(val) for val in values])

#https://docs.python.org/3/library/functions.html    

values ="".join(char if char not in separators else " " for char in number).split()
print (sum([int(val) for val in values]))

quote = " alright WIne Is Good For Health drink EVEreryday"

for char in quote:
    if not char.islower():
        print(char)
for char in quote:
    if char .isupper():
        print(char)
for char in quote:
    if char in "QWERTYUIOPASDFGHJKLZXCVBNM":
        print(char)
for i in range(1,20):
    print(" i is now {}".format(i))

for k in range(1,9):
    print ("k")
    print (k)    
for l in range(10):
    print(l)
for l in range(0,10,2):
    print(l)    
age = int(input(" how old are you ?"))    
if age >= 16 and age <= 65:
    print("have  a good day at work")
else:
    print("enjoy your free time")
    print ("-"* 80)  


if age >= 16 or age <= 65:
    print("have  a good day at work")
else:
    print("enjoy your free time")
    print ("-"* 80)         

for i in range ( 1, 10):
    print (i,"*",i,"=",i*2)

for i in range (1,10):
    for k in range(1,10):
        print("{0} * {1} = {2}".format(i,k,i*k))
    print("----------------------------")
    
list = ["milk", " eggs","orange"]

for item in list:
    print("buy" +item)
    
for item in list:
    if item != " eggs":
        print( "buy" + item)
for item in list:
    if item == " eggs":
        continue
    print ( "Buy"+" " + item)
                             
# Break
# while loops
#for i in range(10):

# while i <10:
#     print(i)"""
       
                              
                              
                              
heights = [161,162,163,144,154,178,179,124]
can_ride=[]


for height in heights:
    if height > 161:
        print(height)
        can_ride.append(height)
print(can_ride)        




k = [1,2,3]

l= sum(k)
print(l)

                                      