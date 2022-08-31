# for loop  , 2) while loop

"""


number = "9,233,456;768.890;324;567;543;945;"

sep = number[1::4]
print(sep)

number = "3,567,56,6578;5467890:76890.3,678:678,3.45;4;5;3546789;4.5.6."
sep = " "

for char in number:
    if not char.isnumeric():
        sep = sep + char
print(sep) 

 
quote = "Alright wine is Good for HEALth Drink one Ounce Everyday"

for char in quote:
    if not char.islower():
        print(char)

for char in quote:
    if char.isupper():
        print(char)        

for char in quote:
    if char in "QWERTYUIOPASDFGHJKLZXCVBNM":
        print(char)


        
for i in range (10):
    print(i)
    
for i in range (1,10):
    print(i)   
for i in range (5,10):
    print(i)


for i in range(1,11):
    print(i,"*","2","=",i*2)
    
for i in range (1,11):
    for k in range (1,11):
        print(" {0} * {1} = {2}".format(i,k,i*k))
    print("----------------------------------------")


for i in range(5):
    print( "this is to print the same line")
    
for i in range(5):
    print(i)   
    

f = ["apple","banana","cherry","mango"] 

for y in f:
    print(y)
    
print("--------------------------------------")    


for y in f:
    print(y)
    if y == "banana":
        break
print("---------------------------------")   
for y in f:
    
    if y == "banana":
        
        break
    print(y)    
    
stu = "i promise i will finish the assignments to today"

for k in stu:
    print(k)
    if k == "w":
        break

for i in range (0,10): 
    print (i)
print ("------------------------------------")
for i in range (0,10,2): 
    print (i)   
    """



name =" "
while name!= "sateesh":
    name =input("enter NAme")
print( " thanks for confiramtion")    
    
    
    

