z = str(input("выбираете знак: "))
n = int(input("первое число: "))
m = int(input("второе число: "))
if z =="+":
        print(n+m)
elif z=="-":
        print(n-m)
elif z=="*":
        print(n*m)
else:
        if m==0:
                print("error")
        else:
                print(n/m)
q = str(input("хочешь закончить, или нет/ Y or N"))
if q=="Y":






#2
a = int(input("enter number:"))
b = int(input("enter number:"))
c = int(input("enter number:"))
a += b
b += c-a
c += a
        print(a, b, c)
#3
q = int(input())
p = q*4
s = q**2
print(p, s)
#6
number = int(input())
if number//1000>number//100%10 and number//100%10>number%100//10 and number%100//10>number%10:
	print("Да")
else:
	print("нет")
