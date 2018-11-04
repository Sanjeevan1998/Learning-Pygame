import pygame
pygame.init()



infostuffs = pygame.display.Info() # gets monitor info

dispx, dispy = infostuffs.current_w, infostuffs.current_h

dispx = int(dispx) # So your resolution does not contain decimals
dispy = int(dispy)



#make the pygame window
screen=pygame.display.set_mode((dispx,dispy ),pygame.FULLSCREEN )
pygame.display.set_caption('Screen saver')
clock = pygame.time.Clock()

bg=pygame.image.load('C:/Users/SANJEEVAN/Desktop/GIT/Pygame/SS1/bg.png')
bg = pygame.transform.scale(bg, (dispx, dispy))


running = True

black=(0,0,0)
white=(255,255,255)




while (running):
        screen.fill(white)
        screen.blit(bg, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   running = False
                elif event.key == pygame.K_F1:
                   pygame.display.quit()
                   pygame.display.init()
                   bg = pygame.transform.scale(bg, (800,400))
                   screen=pygame.display.set_mode((800, 400),pygame.RESIZABLE)
                   pygame.display.set_caption('Screen saver')
                elif event.key == pygame.K_F2:
                   pygame.display.quit()
                   pygame.display.init()
                   bg = pygame.transform.scale(bg, (dispx, dispy))
                   screen=pygame.display.set_mode((dispx,dispy ),pygame.FULLSCREEN )
                   pygame.display.set_caption('Screen saver')
            elif (event.type==pygame.VIDEORESIZE and event.size!=(dispx, dispy)):
                bg = pygame.transform.scale(bg, (event.size))
                screen=pygame.display.set_mode((event.size),pygame.RESIZABLE)
                pygame.display.set_caption('Screen saver')


        pygame.display.update()
        clock.tick(60)
pygame.quit()
quit()
