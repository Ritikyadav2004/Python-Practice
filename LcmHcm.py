#lcm
a=10213;
b=312; 
minimum = a if a<b  else b


for i in range(minimum,0,-1):
  if( a%i==0 and b%i ==0):
    print(f"GCD of {a} and {b} is {i}")
    print(f"LCM od {a} and {b} is {a*b//i}")
    break;
