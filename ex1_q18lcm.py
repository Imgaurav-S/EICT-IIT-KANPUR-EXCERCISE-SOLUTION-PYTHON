num_1 =int(input("enter first number"))
num_2 =int(input("enter second number"))
if (num_1<num_2):
    a =num_1
else:
    a = (num_2)

print(a)

i=2
k=1
lcm =0
for i in range(2,a+1):
    if((num_1%i or num_2%i) ==0):
       k= (num_1*num_2)/i

    i=i+1

print(k)
if(k==1):
    lcm=num_1*num_2
    print(lcm)
