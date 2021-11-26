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
#5
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
	lst.reversed()
	print(lst)
except:
	print("There is an error")
#4
sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
set_0 = set(sequence_0)
if len(set_0)==len(sequence_0):
	print("Последовательность уникальна.")
else:
	print("Последовательность не уникальна.")
