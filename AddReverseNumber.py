#logic
#everse ,  add  reverse again , emove leading zeros
def reverse(num):
    if num<9:
        return num
    sum=0;
    while(num>0):
        temp=num%10
        sum*=10
        sum+=temp
        num//=10
    return sum    
print(reverse(21100) )

# def removeZero(num):

def addNumber(a,b):
    A=reverse(a)
    B=reverse(b)
    C=reverse(A+B)
    return C


print(addNumber(4358 ,754))
print(addNumber(24, 1))
print(addNumber(305 ,794))
print(addNumber(1200,30))
print(addNumber(100,200))


