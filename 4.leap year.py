year=int(input("Enter the year: "))

if(year%400==0) and (year%100==0): #to check for centuries
  print(f"{year} is a leap year")
elif (year%4==0) and (year%100!=0): #to check for leap years
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")