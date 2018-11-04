import pygame
pygame.init()
clock = pygame.time.Clock()

r,g,c=0,0,0
color=(r,g,c)
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

def screensaver():
    infostuffs = pygame.display.Info()
    dispx, dispy = infostuffs.current_w, infostuffs.current_h

    x,y=0,0
    a,b=100,100
    fx,fy=0,0
    jump=0
    temp=2
    screen=pygame.display.set_mode((dispx,dispy ),pygame.FULLSCREEN )
    running = True
    while (running):
        if fx==0:
            x=x+5
        if fy==0:
            y=y+4
        if fx==1:
            x=x-5
        if fy==1:
            y=y-4
        if temp==1:
             screen.fill(white)
             pygame.display.set_caption('Square')
             pygame.draw.rect(screen, color, (x,y,a*800/dispx,b*400/dispy), 2)
             pygame.display.update()
        elif temp==2:
            pygame.display.set_caption('Square')
            screen.fill(white)
            pygame.draw.rect(screen, color, (x,y,a,b), 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   running = False
                elif event.key == pygame.K_F2:
                   temp=1
                   screen=pygame.display.set_mode((800,400) )
                   screen.fill(white)
                   pygame.display.set_caption('Square')
                   pygame.draw.rect(screen, color, (x,y,a*800/dispx,b*400/dispy), 2)
                elif event.key == pygame.K_F1:
                   temp=2
                   screen=pygame.display.set_mode((dispx,dispy ),pygame.FULLSCREEN )
                   pygame.display.set_caption('Square')
                   screen.fill(white)
                   pygame.draw.rect(screen, color, (x,y,a,b), 2)
        w, h = pygame.display.get_surface().get_size()
        fxt=fx
        fyt=fy
        if(x>=w-a):
            fx=1
        if(y>=h-b):
            fy=1
        if(x<=0):
            fx=0
        if(y<=0):
            fy=0
        if(fxt!=fx or fyt!=fy):
            jump=1 if jump==0 else 0
        if(jump==0):
            a=a+1
            b=b+1
        else:
            if a==1:
                jump=0
            else:
                a=a-1
                b=b-1
        pygame.display.update()
        clock.tick(60)

screensaver()

pygame.quit()
quit()
