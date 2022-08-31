"""
# Day4 :-

#Agenda :- condational Statements
# what IF

name = input("Please enter your name:")
age = int(input("how old are you,{0}?".format(name)))

if age >= 21:
    print(" 1.{0}you are old enough to apply for visa".format(name))
    print(" 2.PLease visit our website to check the polices" )
    print(" 3. application charges are  $300 ")
    print(" 4.applicaiton deadline is 30 the aug")
else:
    print("please come back in {0} years".format(21-age))
    print( "{0}, We will send the guidelines for your ref".format(name) )    



#print( "my name is", name, "and my age is", age  )

Pan_card = 'abc123','adfgadg','879ui','jskdg7'

user=input("PLease enter your pancard number")

if user in Pan_card:
    print(" You are safe")
else:
    print("PLease apply for one")    
    
people =20
cats = 40
dogs = 50

if people < cats:
    print(" Too Many Cats !")

if people > cats:
    print("not many cats !")
else:
    print( " people less than cats")    
 

if people < dogs:
    print( " dogs are pets")
    
if people  < dogs:
    print( " this is okay!")
 
dogs +=5

if people >= dogs:
    print( " i know this")
 
if people <= dogs:
    print ( " this is expected")
    
if people == dogs:
    print ( " this  is a good sigh") 
else:
    print( "this is for demo")    




people = int(input("please enter a number:"))
cars = int(input("please enter a number:"))
buses =  int(input("please enter a number:"))
        
if cars > people:
    print("cars are more than people")
elif cars < people:
    print( "cars are less than people")
elif buses > cars:
    print( " there are too many buses")
elif buses < cars:
    print(" there are too many cars" ) 
elif people > buses:
    print( " too many people")
else:
    print( " this is just  demo")                   
    
print (" you have two doors to enter the house , do you want to enter through door #1 or door #2 ? ")   

door = input( ">") 

if door == "1":
    print("There is gaint dog eating the cheese cake, what will you do")
    print( "1. take the cake from the dog ")
    print( "2. just run as fast as poosible")
    
    dog = input( ">") 
    if dog == "1":
        print( " dog will eat your face off")
    elif dog =="2":
        print(" this is good option")
    else:
        print( "you are a samrt fellow") 

elif door == '2':
    print(" there are beautiful butter files and greenry and blue berries")
    print("1. catch the butter files")
    print( "2. eat blue berries")
    print( " 3. shut the door and enjoy greenry")
    
    greenry = input(">")
    
    if greenry == '1' or '2':
        print( " this is for demo")
    else:
        print( " this demo for else statement")
else:
    print(" this is how you wite python if else condations")            
    
              
    
    
        
        
if < expression>:
    <statement>
    <statement>
else:
    <statement>
    <statement>
         
    


        
if < expression>:
    <statement>
    <statement>
elif:
    <statement>
    <statement>
elif:
    <statement>
    <statement> 
elif:
    <statement>
    <statement> 
else:
    <statment>                
"""


take_a_number= int(input( " please give a number as a input:"))

if take_a_number == 0:
    print( take_a_number, " this is 4 even number")
elif take_a_number%2==0:
    print( take_a_number, " this is even number")
else:
    print( take_a_number, " this is odd number")    
        
