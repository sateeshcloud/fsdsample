# # collection

# # 1) list
# # 2) tuple
# # 3) set
# # 4) dict

# # List = it is a collection of elements [ ]

# list1 = [10,20,30,40,50]
# list2 = ["nikhil","syam","radha","krisha"]
# list3 = [ "ram","kiran","raju","hari"]

# print(list1[0])
# print(list2[1])
# print(list3[2])

# # list are mutable objects : - we can change ,we can do insertions, updations and deletions.
# list2.append('Ravali')
# print(list2)

# list1 =eval(input("enter the elements into list:"))
# print(list1)
# list2.insert(0,'ramana')
# print(list2)

# list4 = list3+ list2
# print(list4)

# list4.pop()
# print(list4)

# list4.pop(1)
# print(list4)

# del list4 [1:3]
# print(list4)



# del list4 [1:]
# del list4 [:3]

# list4.clear()
# print(list4)

# list4.reverse()
# print(list4)

# l = [" li", "ru","ra"]
# k = [ "hi", "rm"]
# print(l)
# print(k)
# l= 4
# l=k.copy()
# l.append("li")
# print(k)
# print(l)

# l = [100,200,300,400]
# l1= [100,200,300,400,400,400,400]
# # print(l==l1)

# print(len(l1))
# print(l1.count(400))
# print(max(l1))
# print(min(l1))

# join

flowers = [
    "lily",
    "rose",
    "Sunflower",
    "Tiger Lily",
    "Lavender",
    "daffodil"
]
# for flower in flowers:
#     print(flower)    

separator = "|"
output =separator.join(flowers)
print(output)

separator = "  "
output =separator.join(flowers)
print(output)   

print(",".join(flowers))  

#split

str1 = " there is a dog by name mickey"
str2 = str1.split()
print(str2)






 
           
           
           
           
           

      

