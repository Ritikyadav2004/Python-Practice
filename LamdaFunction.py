# lambda function in Python is:
# ➡️ A small anonymous function (no name)(also know as ).
# ➡️ Can take any number of arguments but has only one expression.
# ➡️ The expression is automatically returned (no need for return).
#lambda arguments: expression
# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8


# multiply =lambda x,y :x*y
# print(multiply(5,3))

# add = lambda a,b,c: (a+b)*c
# print(add(2,4,2))



#sum 1 to n
#using the formula
#sum = n*(n+1)/2

# sumOfDigit = lambda n:(n*(n+1))//2
# print(sumOfDigit(10))
# sum of digit 


# digit = 91
# sum=0

# digitSum = lambda x,t:x+t

# while(digit>0):
#     temp=digit%10
#     sum = digitSum(sum,temp)
#     digit//=10

# print(sum)




#sum of digit using ruduce function and lamda function 
from functools import reduce
num=1234

digits = list(map(int,str(num)))  #['1','2','3','4']-->num then int convert into --> [1,2,3,4]
#x->1,y->2, then x me 3 and y me 3 then  x me 6 then y me 4 then x me 10 and return
sumOfDigit=reduce(lambda x,y:x+y,digits) # x and y starting value 

print(sumOfDigit)