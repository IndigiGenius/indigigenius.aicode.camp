import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()

# Challenge 1: Squares in a Grid
def draw_square(center_x, center_y, side_length=20):
    t.penup()
    # go to the top left corner of the square I want to draw
    top_left_x = center_x - side_length/2 # calculate how far left from the center I need to be (negative x)
    top_left_y = center_y + side_length/2 # calculate how far up from the center I need to be (positive y)
    t.setposition(top_left_x, top_left_y) # go to that top left corner spot
    # go to the top left corner of the square, split the length in half to get there, you're in the center now

    # now, face east (0 = east, 90 = north, 180 = west, 270 = south)
    t.setheading(0)
    # I'm where I want to be in the top left corner of the square I want to draw and facing east
    # put the pen down now and draw my square
    t.pendown()
    for side in range(4):
        t.forward(side_length)
        t.right(90)
    
    # put the pen up
    t.penup()

draw_square(-75, 0, 50)
draw_square(-75, 75, 50)
draw_square(-75, -75, 50)

draw_square(0, 0, 50)
draw_square(0, 75, 50)
draw_square(0, -75, 50)

draw_square(75, 0, 50)
draw_square(75, 75, 50)
draw_square(75, -75, 50)

draw_square(0, 0, 250)



# YOUR CODE HERE


# DON'T TOUCH THIS
turtle.mainloop()