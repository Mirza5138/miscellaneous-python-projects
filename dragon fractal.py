import turtle

turtle.tracer(False)  # Turn off animation for max speed
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(4)

turns = [0, 1]
depth = 12

def main(lst):
    for i in range(depth):
        turnAppender(lst)
    fractalDraw(lst)
    turtle.update()  # Update once at the end

def turnAppender(lst):
    l = len(lst)
    for i in lst[:-1]:
        lst.insert(l, 1 - i)
    return lst

def fractalDraw(lst):
    for i in lst:
        if i:
            t.right(90)
        else:
            t.left(90)
        t.forward(8)

main(turns)

turtle.exitonclick()