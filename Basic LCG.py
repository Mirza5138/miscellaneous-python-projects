#This is a really basic version of a Linear Congruential Generator, one of the simplest forms of a pseudo-random number generator. It can generate numbers from 0 to 999972.
#It starts with one (thing, i don't know why) and then continues the sequence further until it hits 1 again which takes 999973 steps.
#The values (a, m and c) are chosen specifically and likely won't work the same way if you change them.

m = 999973
a = 76922
c = 618017

x = (a+c)%m
print(1)
while x != 1:
    print(x)
    x = (a*x+c)%m
