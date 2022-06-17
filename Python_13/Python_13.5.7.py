import random

x = int(random.random()*100)
print(x)
x = int(input())


#print(22 == 5 or 44)
#print((x % 10) or (x // 10) == 5)

#print(((x % 10) or (x // 10)) == 5)

#print(type((((x // 10) or (x % 10)) == 5)))
#print(type(((x // 10) or (x % 10)) == 5))
print(type(((x // 10) or (x % 10)) == 5))


if (x // 10) == 5 or (x % 10) == 5:
    print("yes")
else:
    print("No")

