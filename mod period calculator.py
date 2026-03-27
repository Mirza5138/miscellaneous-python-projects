m = 999973
a = 76922
c = 618017

x = (a+c)%m
print(1)
while x != 1:
    print(x)
    x = (a*x+c)%m