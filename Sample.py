from pico2d import *
import time

open_canvas(800, 600)
bird = load_image('bird.png')
grass = load_image('grass.png')
x = 400
y = 600
g = 9.8
vel = 5
start = time.time()
delay(1)
end = time.time()
etime = end - start

def imagePoint(w,h):
    global x, y
    newW = w/2
    newH = h/2

    x1 = x-newW
    x2 = x+newW
    y1 = y-newH
    y2 = y+newH

    return x1,x2,y1,y2

print(type(load_image('bird.png')))

def isCrash(image1 = tuple, image2 = tuple):
    image1[0]


    return
def free():
    global x, y
    global end, start, etime

    y -= (vel*etime + 1/2*g*etime**2)

    end = time.time()

    etime = end - start
    if y < 100:
        start = end
while True:
    clear_canvas()
    grass.draw(400, 30)
    
    bird.draw(x, y, 100, 100)

    update_canvas()
    delay(0.01)
    if y < 100:
        y = 600
    free()

close_canvas()