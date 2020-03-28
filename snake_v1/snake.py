import turtle
import time
import random

speedtime = 0.125

#SCOREBOARD
score = 0
high_score = 0

# Configurar ventana

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeza serpiente

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('#00FF11')  # Hex Colors
head.penup()
head.goto(0, 0)  # x(right - left), y(up - down)
head.direction = "stop"

"""
------- Functions -------
"""

# Movement
def mov():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)  # pixels

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)  # pixels

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)  # pixels

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)  # pixels

#Direction keys

def up_key():
    head.direction = 'up'

def down_key():
    head.direction = 'down'

def right_key():
    head.direction = 'right'

def left_key():
    head.direction = 'left'

def stop_mov():
    head.direction = 'stop'

# Keyboard

wn.listen()
wn.onkeypress(up_key, "Up")
wn.onkeypress(down_key, "Down")
wn.onkeypress(right_key, "Right")
wn.onkeypress(left_key, "Left")

#Random Food

apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color('red')  # html natural names
apple.penup()
apple.goto(0,100)  # x(right - left), y(up - down)
apple.direction = "stop"

#Snake Body

segments = []

#SCOREBOARD

text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write('Score: {}      High Score: 0'.format(score), align= 'center', font=(22))


while True:
    wn.update()

    #Border Collisions
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        stop_mov()

        #Hide segments
        for sg in segments:
           sg.goto(2000,2000)

        segments.clear()
        apple.goto(0, 100)
        score = 0
        text.write('Score: {}      High Score: {}'.format(score, high_score), align= 'center', font=(22))

    #Body Collisions

    for sg in segments:
        if sg.distance(head) < 20:
            time.sleep(1)
            score = 0
            head.goto(0,0)
            stop_mov()
            apple.goto(0,100)
            text.write('Score: {}      High Score: {}'.format(score, high_score), align='center', font=(22))

            # Hide segments
            for nested_sg in segments:
                nested_sg.goto(1000,1000)
            segments.clear()

    if head.distance(apple) < 30: #each item measures 20 pixels, if they have collided
        x = random.randint(-280, 280) #-20 px from the border
        y = random.randint(-280, 280)
        apple.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color('#C1FFC1')
        new_segment.penup()
        new_segment.goto(0, 0)  # x(right - left), y(up - down)
        new_segment.direction = "stop"
        segments.append(new_segment)

        #icrease scoreboard
        score = score + 1
        text.clear()
        if score > high_score:
            high_score = score
        text.write('Score: {}      High Score: {}'.format(score, high_score), align= 'center', font=(22))

    #Body movement
    total = len(segments)

    for sg in range(total - 1, 0, -1):
        x = segments[sg - 1].xcor()
        y = segments[sg - 1].ycor()
        segments[sg].goto(x,y)
    if total > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    mov()
    time.sleep(speedtime)
