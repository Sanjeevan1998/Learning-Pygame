import pygame
import random
import time
pygame.init()

clock=pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
info = pygame.display.Info()
width = info.current_w
height = info.current_h

screen=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
screen.fill(white)

man1=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/man1.jpg')
man2=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/man2.jpg')
man3=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/man3.jpg')
man4=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/man4.jpg')
man5=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/man5.jpg')


manm1=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/manm1.jpg')
manm2=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/manm2.jpg')
manm3=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/manm3.jpg')
manm4=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/manm4.jpg')
manm5=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/ss4/man/manm5.jpg')


imgw=man1.get_width()
imgh=man1.get_height()

imgx=0
count=0

def man(img,x,y):
    screen.blit(img, (x,y))



def rain():
    flag=0
    run=True
    while(run):
        time.sleep(1/15)
        screen.fill(white)


        for i in range (0,300):
            x=random.randint(0,width-1)
            y=random.randint(0,height-1)
            pygame.draw.lines(screen, black, False, [(x,y), (x,y+10)], 2)

        global imgx
        global count

        if flag==0:
            if(count in range(0,3)):
                man(man1,imgx,height-imgh)
            elif(count in range(3,6)):
                man(man2,imgx,height-imgh)
            elif(count in range(6,9)):
                man(man3,imgx,height-imgh)
            elif(count in range(9,12)):
                man(man4,imgx,height-imgh)
            elif(count in range(12,15)):
                man(man5,imgx,height-imgh)
            elif(count in range(15,18)):
                man(man4,imgx,height-imgh)
            elif(count in range(18,21)):
                man(man3,imgx,height-imgh)
            elif(count in range(21,24)):
                man(man2,imgx,height-imgh)
        else:
            if(count in range(0,3)):
                man(manm1,imgx,height-imgh)
            elif(count in range(3,6)):
                man(manm2,imgx,height-imgh)
            elif(count in range(6,9)):
                man(manm3,imgx,height-imgh)
            elif(count in range(9,12)):
                man(manm4,imgx,height-imgh)
            elif(count in range(12,15)):
                man(manm5,imgx,height-imgh)
            elif(count in range(15,18)):
                man(manm4,imgx,height-imgh)
            elif(count in range(18,21)):
                man(manm3,imgx,height-imgh)
            elif(count in range(21,24)):
                man(manm2,imgx,height-imgh)
        if flag==0:
            imgx=imgx+7
        else:
            imgx=imgx-7
        if flag==0 and imgx>=width-imgw:
            flag=1
            count=0
        elif flag==1 and imgx<=0:
            flag=0
            count=0






        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False

        count+=1
        if count==24:
            count=0
        pygame.display.update()

    clock.tick(60)
rain()
pygame.quit()
quit()
