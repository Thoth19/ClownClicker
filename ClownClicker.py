import pygame,random
from classes import *
pygame.init()
screen = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()

score = 0
space_presses = 1
hits = 1
pygame.display.set_caption('Clown Clicker: A Game of Fun ... unles you have a red nose Score: %d' %(score))

all_group = pygame.sprite.Group()
for i in range(5):
    position = (random.randint(1,800),random.randint(1,600))
    color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    speed = (1,1)
    direction = [random.randrange(-1,2,2),random.randrange(-1,2,2)]
    clown = Clown(position,color,speed,direction)
    all_group.add(clown)

all_group.draw(screen)
pygame.display.flip()
done = False
while(not(done) and pygame.time.get_ticks() < 1000*60): #60 seconds
    pygame.display.update()
    screen.fill((0,0,0))
    clock.tick(30)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]: 
        pygame.display.quit()
        done = True
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                mouse_pos = pygame.mouse.get_pos()
                space_presses += 1
                for clown in all_group:
                    if clown.rect.collidepoint(mouse_pos):
                        score += clown.speed[0]
                        clown.speed = clown.speed[0] + 1, clown.speed[1] + 1
                        clown.direct = [random.randrange(-1,2,2),random.randrange(-1,2,2)]
                        hits += 1
                        clown2 = Clown((clown.rect.x,clown.rect.y), clown.color, clown.speed, [random.randrange(-1,2,2),random.randrange(-1,2,2)])
                        all_group.add(clown2)
    all_group.update()
    pygame.display.set_caption('Clown Clicker: Score: %d, Time Remaining: %d, Accuracy: %f' %(score,60- pygame.time.get_ticks()/1000, (hits/(float(space_presses)))))
    all_group.draw(screen)
    pygame.display.flip()
pygame.display.quit()
print("Score: %d, Accuracy: %f" %(score, (hits/(float(space_presses)))))
exit()