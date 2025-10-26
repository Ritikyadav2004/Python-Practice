
#Input:
# The first line will be given by N number of works
# Next, N line will be given SH, SM, EH and EM each separated by space(SH=starting hr, SM=starting min, EH=ending hr, EM=ending min
def tracker(numberOfWork):
    #first we will convert houre in minute
    for i in range(0,numberOfWork):
        sh=int(input("Enter Strarting Hour:"))
        sm=int(input("Enter Strarting Minute:"))
        eh=int(input("Enter Ending Hour:"))
        em=int(input("Enter Ending Minute:"))
        totalStaringMinute= sm+sh*60
        totalEndingMinute = em+eh*60
        StudyMinute=totalEndingMinute-totalStaringMinute
        if(StudyMinute>=60):
            print(StudyMinute//60,"Hour")
            print(StudyMinute-(StudyMinute//60)*60,"Minite")
        else:
            print(StudyMinute,"Minutes") 
tracker(1)