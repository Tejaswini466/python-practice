import math
print("Enter co-efficients of a,b and c: ")
a=(float(input()))
b=(float(input()))
c=(float(input()))
d=b**2-4*a*c  #discriminant

if d>0:
  root1=(-b+math.sqrt(d))/2*a
  root2=(-b-math.sqrt(d))/2*a
  print(f"Root 1: {root1}")
  print(f"Root 2: {root2}")
elif d==0:
  root=-b/(2*a)
  print(f"Root : {root}")
else:
  real=-b/(2*a)
  imag=math.sqrt(abs(d))/(12*a)
  print(f"Root 1: {real}+{imag}i")
  print(f"Root 2: {real}-1{imag}i")