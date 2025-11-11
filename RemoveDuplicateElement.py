a = [1,2,3,4,5,5]

seen=[]
out=[]

for x in a:
    if x not in seen:
        seen.append(x)
        out.append(x)

# b={}
# b=a
# print(b)
# print(out)


target=10



#standard approach
for i in range(len(a)):
    for j in range(i,len(a)):
        if(a[i]+a[j]==target and i!=j):
            print(i,j)
            break

#optimizw approch
left=0
right=len(a)-1
while(left<=right):
    if(a[left]+a[right]==target):
        print(left , right)
        break;
    elif(a[left]+a[right]>target):
        right-=1

    else:
        left+=1       