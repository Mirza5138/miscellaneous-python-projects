initial = int(input())
#p = int(input())

goal = initial**.5 #* 10**p // 1 / 10**p
counter = 0
x1 = 10
x2 = initial/x1

while x1 != goal:
    print(x1, goal)
    x1 = .5*(x1+x2) #* 10**p // 1 / 10**p
    x2 = initial/x1
    counter += 1

print(counter, x1)