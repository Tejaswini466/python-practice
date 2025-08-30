# Armstrong Number: It is a number that is equal to the sum of its own digits, 
# each raised to a power equal to the number of digits in the number.
# 1^3+5^3+3^3= 1+125+27=153

num=int(input("Enter the number: "))
temp=num
num_digit=len(str(num))
sum=0
while(temp>0):
  digit=temp%10
  sum+=digit**num_digit
  temp//=10

if (sum==num):
  print(f"{num} is an Armstrong number")
else:
  print(f"{num} is not an Armstrong number")