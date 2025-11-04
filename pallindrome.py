# def ispallindrom(num):
#     org = num
#     reverse=0
#     while(num>0):
#         temp=num%10
#         reverse*=10
#         reverse=reverse+temp
#         num=num//10


#     return reverse==org   


# print(ispallindrom(132031))


digitSum = lambda x,t:x+t #here digit sum act as function which take two variable

def checkFromLamda(num):
    org=num
    rev=0
    while(num>0):
        temp=num%10
        rev*=10;
        rev = digitSum(rev,temp) # as x and t
        num//=10
    return org==rev    

# print(checkFromLamda(126021))


#check digit sum
def sumOfdigit(digit):
    sum=0
    while(digit>0):
        temp=digit%10
        sum=digitSum(sum,temp)
        digit=digit//10
    return sum

print(sumOfdigit(123)==sumOfdigit(3210))
