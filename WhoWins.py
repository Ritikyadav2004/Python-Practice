def whoWins(num):
    flip=True;
    while(num>0):
      if(flip):
        num=num-1;
        flip=False;
      else:
        num-=2;
        flip=True;
    # mean defintley left one stone but if turn rmesh ki hui to vo do stone consume nhi kr sakta num become -1
    if(num!=0):
      num-=1
      flip=True

    if(not flip):
      return "Suresh"
    else:
      return "Ramesh"



print(whoWins(13))
print(whoWins(10))
print(whoWins(1))
print(whoWins(2))

