l =["Ritik","Rishabh","Ritesh","Riya"]

l.sort()
print(l)

left = l[0]
right =l[len(l)-1]
minlen = min(len(left), len(right))
arr=[]
for i in range(minlen):
    if(left[i]!=right[i]):
        print(arr)
        break

    arr.append(left[i])    