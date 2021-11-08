# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import turtle
import time
import random
delay = 0.1
score=0
high_score=0
#set up screen
wn=turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the screen updates

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.penup()
head.color("white")
head.goto(0,0)
head.direction = 'stop'

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.penup()
food.color("red")
food.goto(0,100)


segments=[]
#pen for score
pen=turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score:0 High Score:0", align='center', font=("Courier", 24, 'normal'))

#functions
def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'

def go_left():
    head.direction = 'left'

def go_right():
    head.direction = 'right'

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
#keyboard bindings
    wn.listen()
    wn.onkeypress(go_up,"w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
#main game loop
while True:
    wn.update()
    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.1)
        head.goto(0,0)
        head.direction="stop"

        #hide segments
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
         #reset score
        score = 0
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score, high_score), align="center", font=("Courier", 24, 'normal'))

    #check for collision with food
    if head.distance(food)<20:
        #move food to random spot on screen
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)
        #increse the score
        score+=10

        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score, high_score), align="center", font=("Courier", 24, 'normal'))

    #move the end segments first in revese order
    for index in range(len(segments)-1,0,-1):
        x = segments[index -1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to the head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    #check fo body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score:{} High Score:{}".format(score, high_score), align="center",
                      font=("Courier", 24, 'normal'))
    time.sleep(delay)

wn.mainloop()