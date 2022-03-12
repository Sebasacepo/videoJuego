import pygame
import os

#Tamaño de juego
WIDTH, HEIGHT = 900, 500   
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("juego de navecistas cool")

WHITE = (255, 255 , 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

border =pygame.Rect(WIDTH/2 - 5,0,10, HEIGHT) 

#Fotogramas por segundo
FPS = 60
VEL = 5 #velocidad con la que se va mover ship
max_bullets = 3
bullet_vel=7

ship_width, ship_height = 55, 48

#naves
yellowship_img = pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))
yellowship = pygame.transform.rotate(pygame.transform.scale(
    yellowship_img,(ship_width,ship_height)),90)

redship_img=pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
redship=pygame.transform.rotate(pygame.transform.scale(
    redship_img,(ship_height,ship_width)),-90)

#Cargar la imagen de fondo 
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets','space.png')),(WIDTH, HEIGHT))

def drawWindow(yellow,red, red_bullets  ):
    WIN.blit(SPACE,(0,0)) #blit es la función con la cula se dibuja
    pygame.draw.rect(WIN,BLACK,border)
    WIN.blit(redship,(red.x,red.y))
    WIN.blit(yellowship,(yellow.x,yellow.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL >0: #LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < border.x: #Right
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y - VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_a] and red.x - VEL >border.x + border.width: #LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_d] and red.x + VEL + red.width < WIDTH: #Right
        red.x += VEL
    if keys_pressed[pygame.K_w] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_s] and red.y - VEL + red.height < HEIGHT - 15:
        red.y += VEL

def handle_bullets(red_bullets,yellow_bullets, red, yellow):
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if yellow.colliderect(bullet):
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
    



 #Función principal
def main():
    #los rectangulos reprensentan las ship
    red = pygame.Rect(700,300,ship_height,ship_width)
    yellow = pygame.Rect(100,300,ship_width,ship_height)

    red_bullets= []
    yellow_bullets= []

    clock = pygame.time.Clock()
    run = True

    while run:
        #se encarga de que el bucle se repita 60 veces por segundo
        clock.tick(FPS)

        #pygame.event.get() es una lista con todos los eventos
        #de pygame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height //  2+5,10,5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2+5,10,5)
                    red_bullets.append(bullet)





        keys_pressed=pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(red, yellow, red_bullets, yellow_bullets)
        drawWindow(yellow,red,red_bullets,yellow_bullets)

    main()

    #este if comprueba si el fichero se llama main
if __name__ =="__main__":
    main()