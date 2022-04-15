#calculate lcm
num1 = 3
num2 = 4

def calculate_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

print("The L.C.M. is", calculate_lcm(num1, num2))