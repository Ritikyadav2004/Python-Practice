
# def fact(num):
#     if(num==1):
#         return num
#     return num*fact(num-1)


# print(fact(7))


#fibonacci number
#0,1,1,2,3,5,8,13 , 21 , 34 , 55

# fixed number 0 and 1

# def fibonacci(n):
#    if(n<=1):
#     return n
   
#    return fibonacci(n-1)+fibonacci(n-2)
  

# def printf():
#   n=10
#   for i in range(n):
#     print(fibonacci(i),end=" ",)
# printf()    




# sum of n natural number
# def sum(n):
#     if(n==1):
#        return 1
    
#     return n+sum(n-1)

# print(sum(10))



#print n to n1using recursion

# def printf(n):
#     if(n==1):
#         return 1
#     print(n)
#     return printf(n-1)


# print(printf(5))

# printing 1 to n using recursion



# def oneToN(n,end):

#     if(n==end):
#         return n
#     print(n)
#     return oneToN(n+1,end)

# print(oneToN(1,5))


# another way to print one to n 
# def printf(n):
#     if(n==0):
#         return
#     printf(n-1)
#     print(n)
    


# print(printf(5))



#print 1 to n using recursion
# def even(n):
#     if(n==1):
#         return 
        
#     even(n-1)
#     if n%2==0:
#         print(n)  

# even(6)
        


#sum of digit 1 to m

def sum(n):
    if(n==0):
        return 0
    else:
        return n + sum(n-1)
        
print(sum(10))


