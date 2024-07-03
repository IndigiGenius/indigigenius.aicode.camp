import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()

# Challenge 4: Draw the outline of a Starquilt!

size = 120
little_size = size/6
t.speed(3.5)
colors = ["red", "black"]

def draw_leaf(t):
    t.forward(size)
    t.left(45)
    t.forward(size)
    t.left(90+45)
    t.forward(size)
    t.left(45)
    t.forward(size)
    t.left(90+45)

def draw_verticals(t):
    t.forward(little_size)
    t.left(45)
    t.forward(size)
    t.right(45)
    t.forward(little_size)
    t.right(135)
    t.forward(size)
    t.left(135)

def draw_horizontals(t):
    t.left(45)
    t.forward(little_size)
    t.right(45)
    t.forward(size)
    t.left(45)
    t.forward(little_size)
    t.left(135)
    t.forward(size)
    t.right(180)

def go_back(t):
    t.left(180)
    t.forward(size)
    t.left(180)

def go_back_h(t):
    t.right(135)
    t.forward(size)
    t.right(180)

cnt = 0
while True:
    t.color(colors[cnt % 2])
    cnt += 1
    for i in range(8):
        draw_leaf(t)

        for i in range(3):
            draw_verticals(t)

        go_back(t)

        for i in range(3):
            draw_horizontals(t)

        go_back_h(t)

    t.clear()

# DON'T TOUCH THIS
turtle.mainloop()