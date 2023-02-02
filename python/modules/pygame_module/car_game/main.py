import time
import pygame
import random
from pygame.locals import *

size = width, height = (800, 800)
road_width = 500

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CAR GAME")
screen.fill((0, 200, 0))
pygame.display.update()

car = pygame.image.load("car.png")
car = pygame.transform.smoothscale(car,(150,300))
car_loc = car.get_rect()
car_x, car_y =(width/2-road_width/4+10, height-150)

car2 = pygame.image.load("car2.png")
car2 = pygame.transform.smoothscale(car2,(130,300))
car2_loc = car2.get_rect()
car2_x,car2_y = (width/2-road_width/4+10, -150)


speed =1
count =0
while running:
    count+=1
    if count == 50:
        speed+=speed*0.02
        count=0
    car2_y+=speed
    if width > car2_y > car_y-300 and car2_x==car_x:
        print("Game Over")
        time.sleep(1)
        running=False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a,K_LEFT]:
                car_x = width/2-road_width/4+10
            if event.key in [K_d,K_RIGHT]:
                car_x = width/2+road_width/4-10
    if car2_y>height+150:
        car2_y=-150
        if random.randint(0,1)==0:
            car2_x = width/2-road_width/4+10
        else:
            car2_x = width/2+road_width/4-10

    pygame.draw.rect(screen,(50,50,50),((width-road_width)/2,0,road_width,height))
    pygame.draw.rect(screen,(200,200,200),((width-road_width)/2+25,0,10,height))
    pygame.draw.rect(screen,(200,200,200),((width+road_width)/2-35,0,10,height))
    pygame.draw.rect(screen,(255,255,100),(width/2-5,0,10,height))
    car_loc.center=(car_x, car_y)
    car2_loc.center=(car2_x,car2_y)
    screen.blit(car2,car2_loc) 
    screen.blit(car,car_loc) 
    pygame.display.update()
pygame.quit()

