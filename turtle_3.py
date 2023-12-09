import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Vertical Connected Squares")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

# Function to draw a square
def draw_square():
    for _ in range(4):
        tess.forward(50)
        tess.left(90)

# Loop to draw the vertical connected squares
for i in range(5):
    draw_square()
    tess.penup()
    tess.left(90)
    tess.forward(60)
    tess.left(90)
    tess.pendown()

turtle.done()
