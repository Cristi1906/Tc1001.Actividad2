"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

import random
from turtle import *
from random import randrange
from freegames import square, vector
from random import randint

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

color=['orange','green','blue','pink','yellow']
while True:
    col1=random.choice(color)
    col2=random.choice(color)
    if (col1!=col2):
        break
    else:
        continue

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    i=10
    j=10
    bools=(True,False)
    xy=random.choice(bools)
    f=randint(-1,1)
    if xy:
        i=i*f
        j=0
    else:
        i=0
        j=j*f
    if (food.x + i <-200 or food.x + i >190):
        i=i*(-1)
    if (food.y + j <-200 or food.y + j >190):
        j=j*(-1)
    food.x = food.x +i
    food.y = food.y +j
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
