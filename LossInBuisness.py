# 5        # N = 5 people
# 100      # X = 100 (minimum skill required)
# 110      # person 1 skill
# 130      # person 2 skill
# 90       # person 3 skill
# 100      # person 4 skill
# 45       # person 5 skill
def myPartners(numberOfEmployee,minimumSkill):
    employee=[]
    for i in range(0,numberOfEmployee):
        skill = int(input("Enter Skill:"))
        employee.append(skill)
    for i in range(0,len(employee)):
        if(employee[i]>=minimumSkill):
            print("Yes")
        else:
            print("NO")
myPartners(5,100)    