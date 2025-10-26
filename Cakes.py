A=0
max_cake=0
cake = int(input("Enter Number of Cakes:"))

for a in range(1,cake+1):
    left_cake = cake%a   
    used_cake = cake-left_cake
    print("Used cake :",used_cake ," Left Cake:",left_cake,"When A :",a)
    
    if(max_cake<left_cake):
        max_cake=left_cake
        A=a
print(f"\n\n\nMaximum Cake that can be Eaten is {max_cake} When Intger A is {A} is ")    
