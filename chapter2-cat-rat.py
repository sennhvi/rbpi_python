import turtle
import time

box_size = 200
caught = False
score = 0


# functions that are called on key presses
def up():
    mouse.forward(10)
    check_bound()


def left():
    mouse.left(45)


def right():
    mouse.right(45)


def back():
    mouse.backward(10)
    check_bound()


def quit_turtles():
    window.bye()


# stop the mouse from leaving the square set by box size
def check_bound():
    global box_size
    if mouse.xcor() > box_size:
        mouse.goto(box_size, mouse.ycor())
    if mouse.xcor() < -box_size:
        mouse.goto(-box_size, mouse.ycor())
    if mouse.ycor() > box_size:
        mouse.goto(mouse.xcor(), box_size)
    if mouse.ycor() < -box_size:
        mouse.goto(mouse.xcor(), -box_size)


# setup screen
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
cat.color("red")
mouse.penup()
mouse.goto(100, 100)

# add key listeners
window.onkeypress(up, "Up")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.onkeypress(back, "Down")
window.onkeypress(quit_turtles, "Escape")

difficulty = window.numinput("Difficulty", "Enter a difficulty from easy (1), for hard (5) ", minval=1, maxval=5)

window.listen()

# main loop
# note how it changes with difficulty
while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8 + difficulty)
    score = score + 1
    if cat.distance(mouse) < 5:
        caught = True
    time.sleep(0.2 - (0.01 * difficulty))

window.textinput("GAME OVER", "Well done. You scored: " + str(score * difficulty))
window.bye()
