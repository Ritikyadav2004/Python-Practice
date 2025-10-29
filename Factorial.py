
# def fact(num):
#     if(num==1):
#         return num
#     return num*fact(num-1)


# print(fact(7))


#fibonacci number
#0,1,1,2,3,5,8,13 , 21 , 34 , 55

# fixed number 0 and 1

def fibonacci(n):
   if(n<=1):
    return n
   
   return fibonacci(n-1)+fibonacci(n-2)
  

def printf():
  n=10
  for i in range(n):
    print(fibonacci(i),end=" ",)
printf()    