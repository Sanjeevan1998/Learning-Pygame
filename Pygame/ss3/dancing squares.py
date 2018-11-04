import pygame
import time
import random

pygame.init()
clock=pygame.time.Clock()

info = pygame.display.Info()
dispx,dispy = info.current_w,info.current_h
screen=pygame.display.set_mode((dispx,dispy),pygame.FULLSCREEN)

t,r,g,b=0,0,0,0



def color():
    global t,r,g,b
    t=t+1
    if t % 100 == 0:
        r=random.randint(50,255)
        g=random.randint(50,255)
        b=random.randint(50,255)
    return (r,g,b)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)




def draw(x,y,a,b):
    pygame.draw.rect(screen,color(),(x,y,a,b),2)

def move(x,y,a,b,fx,fy):
    draw(x,y,a,b)

    if fx==0:
        x=x+5
    if fy==0:
        y=y+4
    if fx==1:
        x=x-5
    if fy==1:
        y=y-4

    if(x>=dispx-a):
        fx=1
    if(y>=dispy-b):
        fy=1
    if(x<=0):
        fx=0
    if(y<=0):
        fy=0
    print("$$",x,y,a,b,fx,fy,"%%")
    return [x,y,a,b,fx,fy]



def screensaver():

    a1,b1 = 100,100
    x1,y1= random.randint(0,dispx-a1),random.randint(0,dispx-b1)
    fx1,fy1=0,0

    a2,b2 = 100,100
    x2,y2 = random.randint(0,dispx-a2),random.randint(0,dispy-b2)
    fx2,fy2=0,0

    a3,b3 = 100,100
    x3,y3 = random.randint(0,dispx-a3),random.randint(0,dispy-b3)
    fx3,fy3=0,0

    a4,b4 = 100,100
    x4,y4 = random.randint(0,dispx-a3),random.randint(0,dispy-b3)
    fx4,fy4=0,0

    a5,b5 = 100,100
    x5,y5 = random.randint(0,dispx-a3),random.randint(0,dispy-b3)
    fx5,fy5=0,0


    pygame.display.set_caption('Squares')

    running = True
    while (running):
        time.sleep(1/100)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        sq1=move(x1,y1,a1,b1,fx1,fy1)
        x1=sq1[0]
        y1=sq1[1]
        a1=sq1[2]
        b1=sq1[3]
        fx1=sq1[4]
        fy1=sq1[5]


        sq2=move(x2,y2,a2,b2,fx2,fy2)
        x2=sq2[0]
        y2=sq2[1]
        a2=sq2[2]
        b2=sq2[3]
        fx2=sq2[4]
        fy2=sq2[5]


        sq3=move(x3,y3,a3,b3,fx3,fy3)
        x3=sq3[0]
        y3=sq3[1]
        a3=sq3[2]
        b3=sq3[3]
        fx3=sq3[4]
        fy3=sq3[5]

        sq4=move(x4,y4,a4,b4,fx4,fy4)
        x4=sq4[0]
        y4=sq4[1]
        a4=sq4[2]
        b4=sq4[3]
        fx4=sq4[4]
        fy4=sq4[5]


        sq5=move(x5,y5,a5,b5,fx5,fy5)
        x5=sq5[0]
        y5=sq5[1]
        a5=sq5[2]
        b5=sq5[3]
        fx5=sq5[4]
        fy5=sq5[5]






        pygame.display.update()

    clock.tick(60)

screensaver()
pygame.quit()
quit()
