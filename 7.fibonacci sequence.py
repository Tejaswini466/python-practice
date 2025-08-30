# Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, 
# typically starting with 0
n=int(input("How many terms? "))
n1,n2=0,1
count=0
if n<=0:
  print("Please enter a positive number.")
elif n==1:
  print(f"Fibonacci sequence is: {n1}")
else:
  print("Fibonacci sequence is: ")
  while count<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1

    