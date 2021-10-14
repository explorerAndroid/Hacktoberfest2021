# //your code here
# Program to check if a number is prime or not

num = int(input("Enter  a Number "))
flag = False


if num > 1:
   
    for i in range(2, num):
        if (num % i) == 0:

            flag = True
       
      break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

      # Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))


if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")
