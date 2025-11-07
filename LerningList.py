lst = [[1,2,3,4,5],['Jhon' , 'Sam','Ebram','Samson']]
# print(lst)

# for i in range (0,len(lst)):
#     print(lst[i])


# print(lst[1][3]) #Samson
# print(lst[0][4]) #5


# lst[0].append(6)  list ke ander number gy he 
# lst[1].append('Ritik')

# print(lst)

# lst[0].append(0)




#to insert in specific position

# lst[0].insert(0,0) # assigning 0 to oth index

# print(lst[0])

# lst[0].remove(5)
# print(lst[0])



lst1=[1,2,3,4,5,6]
lst2 =[7,8,9,10]

lst1.append(lst2) #list ke ander list gyi he  
# print(lst1)

lst3 =[11,12,13,14]
lst2.extend(lst3)

# print(lst2)

#DIFFRNEC BETWEEN DELET AND REMOVE IS 
#DEL ME HUM INDEX PROVIDE KR RHE HE 
#REMOVE ME HUM DIRECT VALUE PASS KRTE HE 

#to delet the elemnt from the list
index=3 # pomter lst3[3]
del lst3[index]
# print(lst3)



#print(lst[1].pop()) # pop return a new last value of the list bydefult

#print(lst[1].pop(0)) # can work as to delete the specific number from lt
  

lst4 = ['one','two','three','four','five','six']

# if 'one' in lst4:
#     print("AI")


lst4.reverse()

# print(lst4)



lst5=[5,7,6,3,1,6,8,7,1,5,4,5]

# print(sorted(lst5))

# print(lst5.sort())

# print(sorted(lst5,reverse=True)) # bydefu;t revese=false


lst6=[1,2,3,4,'b','c']   # cannot sort ,  TypeError: '<' not supported between instances of 'str' and 'int'
# print(lst6.sort())


# print(sorted(lst6))


List = [54,45,51,5,1,84,51,4,841,]


SortedList = sorted(List)
print(SortedList) # print in sorted manner 
print(List)  # original list will return 

List.sort() # it modify this original list 
print(List)