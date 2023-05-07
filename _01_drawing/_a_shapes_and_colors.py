import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Jason = turtle.Turtle( )

    # Make your turtle's shape 'turtle', .shape('turtle')
    Jason.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Jason.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Jason.color('green')
    Jason.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range(4):
        Jason.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        Jason.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    Jason.goto(4, 4)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Jason.begin_fill()
    Jason.circle(10, steps=30)
    Jason.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    Jason.penup()
    Jason.goto(200,150)
    Jason.pendown()
    Jason.color('#25bbbe')
    Jason.begin_fill()
    for i in range(8):
        Jason.forward(100)
        Jason.left(45)
    Jason.end_fill()
    Jason.penup()
    Jason.goto(200,-50)
    Jason.pendown()
    Jason.color('#Fdc79e')
    Jason.begin_fill()
    Jason.circle(50,steps=50)
    for i in range(2):
        Jason.left(90)
        Jason.forward(50)
    Jason.left(100)
    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
