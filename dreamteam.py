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
a = int(input())
b = int(input())
c = int(input())
a += b
b += c-a
c += a
	print(a, b, c)
