#Equipo 7
# Abiel Moisés Borja García     A01654937
# Alejandro Mariacca Santin     A01654102

from turtle import *
from random import randint, randrange
import random
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['blue', 'yellow', 'magenta', 'orange', 'dark green']

snakeColor = random.choice([i for i in colors])
foodColor = random.choice([j for j in colors if j != snakeColor])

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

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food or (head+10) == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    elif head != food:
        foodMove = randint(1,2)
        if foodMove == 1:
            food.y += 10
        else:
            food.x += 10
        
        if not inside(food):
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10

        snake.pop(0)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, food)
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