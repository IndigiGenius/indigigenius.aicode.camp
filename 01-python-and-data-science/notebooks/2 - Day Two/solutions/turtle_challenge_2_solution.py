import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()

# Challenge 2: Circles in a Grid with One Missing

# YOUR CODE HERE
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

def draw_circle(center_x, center_y, radius):
    t.penup()
    
    # set the position to the center of the circle I want to draw
    # t.circle draws from the bottom of the circle, so you will want to move down by the amount of the radius before you draw the circle
    # so find the new y coordinate
    bottom_y = center_y - radius # subract the radius amount from the center_y value, you're moving down, so use subtraction
    t.setposition(center_x, bottom_y)
    t.pendown() # set the pen down
    t.circle(radius) #draw a circle with the provided radius
    t.penup()


draw_circle(-75, 0, 25) # center left circle
draw_circle(-75, 75, 25) # center top circle
# draw_circle(-75, -75, 25)

draw_circle(0, 0, 25)
draw_circle(0, 75, 25)
draw_circle(0, -75, 25)

draw_circle(75, 0, 25)
draw_circle(75, 75, 25)
draw_circle(75, -75, 25)

draw_square(0, 0, 250)



# YOUR CODE HERE


# DON'T TOUCH THIS
turtle.mainloop()

# DON'T TOUCH THIS
turtle.mainloop()