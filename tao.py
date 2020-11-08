import turtle
import random
random.seed(10)
tao = turtle.Turtle()
tao.shape('turtle')
#tao.forward(100)
#tao.left(90)
tao.reset()
'''
for i in [10,50,90]:
	print(i)

for i in range(100) :
    tao.forward(100)
    tao.left(100)
'''
#range(4)
#list(range(4))
'''
for j in range(10) :
    for i in range(8) :
        tao.forward(100)
        tao.left(45)
    tao.left(145)
'''
def regtangle():
    for i in range(4):
        tao.forward(100)
        tao.left(90)
#regtangle()
for i in range(10):
    regtangle()
    tao.left(36)
