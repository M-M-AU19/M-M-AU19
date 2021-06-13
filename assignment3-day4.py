factorial = 1
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("Even")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(factorial)
