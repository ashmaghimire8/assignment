num = input("Enter a number: ")
num = int(num)
if num == 1 or num == 0:
    print("The number is neither prime nor composite")
elif num < 0:
    print("Enter positive number!")
else:
    for i in range(2,num):
        if(num % i ==0):
         print("The number is composite")
         break
    else:
        print("The number is prime")