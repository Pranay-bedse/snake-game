#importing modules
import random
import time
import turtle

# snake window
wn = turtle.Screen()
wn.title("Pranay Made Snake Game")
wn.setup(width=600, height=600)
wn.bgcolor("green")
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.penup()
head.goto(0, 0)
head.shape("square")
head.color("white")
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.penup()
food.goto(0, 0)
food.shape("circle")
food.color("red")

#new segment
segment = []

#score
Score = 0
High_score = 0

pen = turtle.Turtle()
pen.penup()
pen.goto(0,260)
pen.shape("square")
pen.color("black")
pen.speed(0)
pen.hideturtle()
pen.write("Score: 0   High_score: 0", align="center",font=("courier",24,"normal"))

# Snake movement
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    elif head.direction == "down":
        head.sety(head.ycor() - 20)

    elif head.direction == "right":
        head.setx(head.xcor() + 20)

    elif head.direction == "left":
        head.setx(head.xcor() - 20)


wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

delay = 0.1

while True:
    wn.update()

    if head.xcor() >  290 or head.xcor() < -290 or head.ycor() >  290 or head.ycor() < -290:
        time.sleep(delay)
        head.goto(0,0)
        head.direction = "Stop"


        for segments in segment:
            segments.goto(1000,1000)

        segment.clear()

        Score = 0

        pen.clear()
        pen.write("Score: {}  High_score: {}".format(Score, High_score), align="center", font=("courier", 24, "normal"))

    for segments in segment:
        if segments.distance(head) < 20:

            time.sleep(delay)
            head.goto(0, 0)
            head.direction = "Stop"

            for segments in segment:
                segments.goto(1000, 1000)

            segment.clear()

            Score = 0

            pen.clear()
            pen.write("Score: {}  High_score: {}".format(Score, High_score), align="center",font=("courier", 24, "normal"))


    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("red")
        segment.append(new_segment)

        Score += 10


        if Score > High_score:
            High_score = Score

        pen.clear()
        pen.write("Score: {}  High_score: {}".format(Score,High_score),align = "center",font= ("courier",24,"normal"))

    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)

    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)

    move()
    time.sleep(delay)

wn.mainloop()
