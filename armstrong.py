# armstrong.py
sum=0
user=num
num=int(input("enter the number"))
while num>0:
  rem=num%10
  sum=sum+rem**3
  num=num//10
if(sum==user):
  print("armstorng")
else:
  print("invalid number")  
  
