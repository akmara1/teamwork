#1
sum = 0
for i in range(1, 1000):
	if i%3==0 or i%5==0:
		sum += i
print(sum)

#2
a = 333
b = 555
buf = a
a = b
b = buf
print(a, b)

#3
a = "4729461084"
sum = 0
for i in a:
    sum+=int(i)
print(sum)

#4
a = str(input())
lst = list(a.split("-"))
date = {}
date["year"] = lst[0]
date["month"] = lst[1]
date["day"] = lst[2]
date["
