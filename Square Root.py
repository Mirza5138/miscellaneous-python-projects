# This algorithm initially uses Heron's method of calculating square roots. 

initial = int(input())

goal = initial**.5
counter = 0
x1 = 10
x2 = initial/x1

while x1 != goal: #This condition can return True due to hardware limitations when in reality, it can only approximate the square root.
    print(x1, goal)
    x1 = .5*(x1+x2)
    x2 = initial/x1
    counter += 1

print(counter, x1)
