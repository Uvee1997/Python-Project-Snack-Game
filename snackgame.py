# import packages
import turtle
import random
import time


# creating screen
screen = turtle.Screen()
screen.title("SNACK GAME")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# score
score = 0;
delay = 0.1

# snack
snack = turtle.Turtle()
snack.speed()
snack.shape("square")
snack.color("blue")
snack.penup()
snack.goto(0, 0)
snack.direction = 'stop'

# food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# Creating a bag for the fruits which are eat by snack
old_fruit=[]

# scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("score: ", align="center", font=("courier",24,"bold"))

# define how to move
def snack_go_up():
    if snack.direction != "down":
        snack.direction = "up"

def snack_go_down():
    if snack.direction != "up":
        snack.direction = "down"

def snack_go_left():
    if snack.direction != "right":
        snack.direction = "left"

def snack_go_right():
    if snack.direction != "left":
        snack.direction = "right"

def snack_move():
    if snack.direction == "up":
        y = snack.ycor()
        snack.sety(y + 20)

    if snack.direction == "down":
        y = snack.ycor()
        snack.sety(y - 20)

    if snack.direction == "left":
        x = snack.xcor()
        snack.setx(x - 20)

    if snack.direction == "right":
        x = snack.xcor()
        snack.setx(x + 20)


# keybord binding
screen.listen()
screen.onkeypress(snack_go_up, "Up")
screen.onkeypress(snack_go_down, "Down")
screen.onkeypress(snack_go_left, "Left")
screen.onkeypress(snack_go_right, "Right")

# main loop
while True:
    screen.update()

    # snack & fruit colision
    if snack.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("score: {}".format(score), align="center", font=("courier", 24, "bold"))
        delay -= 0.001

        # creating new fruits
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # adding ball snack

    for index in range(len(old_fruit) -1, 0, -1):
        a = old_fruit[index -1].xcor()
        b = old_fruit[index -1].ycor()

        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snack.xcor()
        b = snack.ycor()
        old_fruit[0].goto(a, b)

    snack_move()

    # snack & border colision
    if snack.xcor() > 280 or snack.xcor() < -300 or snack.ycor() > 240 or snack.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0,0)
        scoring.write(" Game over \n Your score is {}".format(score), align="center", font=("courier", 30, "bold"))

    # snack colision
    for food in old_fruit:
        if food.distance(snack) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(" Game over \n Your score is {}".format(score), align="center", font=("courier", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()





