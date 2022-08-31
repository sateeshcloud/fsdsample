name =" "
while name!= "sateesh":
    name =input("enter NAme")
print( " thanks for confiramtion")    


x=1

while x<= 10:
    print(x)
    x=x+1


n =int(input(" Enter number:"))
sum = 0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print( " ths sum of fisrt",n,"number is:",sum)       


#------------------------ Pass-----------

for i in range(100):
    if i %9==0:
        print(i)
    else:pass    


#-------------Contuine--------------------

numbers =[10,10,0,5,0,30]
for n in numbers:
    if n==0:
        print( "hey how can we divide with zero.. just skipping")
        continue
    print("100/{}={}".format(n,100/n))
    