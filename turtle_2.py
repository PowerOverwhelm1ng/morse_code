import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Five Box Ladder")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

# Function to draw a square
def draw_square():
    for _ in range(4):
        tess.forward(50)
        tess.left(90)

# Loop to draw five boxes
for i in range(5):
    draw_square()
    tess.penup()
    tess.forward(60)  # Move turtle forward for the next box
    tess.pendown()

turtle.done()
