import pygame
import time

pygame.init()

x=800
y=800
screen=pygame.display.set_mode((x,y))

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

def rotate(surf, image, pos, originPos, angle):

    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    rotated_image = pygame.transform.rotate(image, angle)

    surf.blit(rotated_image, origin)


background=pygame.image.load("body.png")
background = pygame.transform.scale(background,(x ,y))
minute_hand=pygame.image.load("left.png")
minute_hand = pygame.transform.scale(minute_hand,(x ,y))
second_hand=pygame.image.load("right.png")
second_hand=pygame.transform.scale(second_hand,(x ,y))
seconds=-1
minutes=-1


running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    pygame.time.delay(1000)

    seconds+=1

    if seconds%60==0:

        minutes+=1
    screen.fill(WHITE)

    screen.blit(background,(0,0))

    rotate(screen,second_hand,(560,495),(0,0),157-6*seconds)

    rotate(screen,minute_hand,(560,495),(0,0),133-(6)*(minutes))
    
    pygame.display.flip()