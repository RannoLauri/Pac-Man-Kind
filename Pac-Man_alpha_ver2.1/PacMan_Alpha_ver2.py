import pygame
import time
import random

pygame.init()
screen_width = 560
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))
x = 25
y = 285
width = 10
height = 10
vel = 20 #speed
right = False
left = False
up = False
down = False
pygame.display.set_caption("Pac - Man")
score = 0
green = (113, 255, 48) #Sõnumi jaoks
white = (255,255,255)
img1 = pygame.image.load('R1.png')
img1 = pygame.transform.scale(img1, (15, 15))
img2 = pygame.image.load('R2.png')
img2 = pygame.transform.scale(img2, (15, 15))
ghost1 = pygame.image.load("ghost1.png")
ghost1 = pygame.transform.scale(ghost1, (15, 15))
direction = "right"
clock = pygame.time.Clock()
i = 0 #For animation, see sprite()
fps = 5


mapTest = [
['############################'],
['#************##************#'],
['#*####*#####*##*#####*####*#'],
['#*####*#####*##*#####*####*#'],
['#*####*#####*##*#####*####*#'],
['#**************************#'],
['#*####*##*########*##*####*#'],
['#*####*##*########*##*####*#'],
['#******##****##****##******#'],
['######*#####*##*#####*######'],
['######*#####*##*#####*######'],
['######*##**********##*######'],
['######*##*###  ###*##*######'],
['######*##*#      #*##*######'],
['      ****#      #****      '],
['######*##*#      #*##*######'],
['######*##*########*##*######'],
['######*##**********##*######'],
['######*##*########*##*######'],
['######*##*########*##*######'],
['#************##************#'],
['#*####*#####*##*#####*####*#'],
['#*####*#####*##*#####*####*#'],
['#***##****************##***#'],
['###*##*##*########*##*##*###'],
['###*##*##*########*##*##*###'],
['#******##****##****##******#'],
['#*##########*##*##########*#'],
['#*##########*##*##########*#'],
['#**************************#'],
['############################']]

newMap = ''
seinad = []
coins = []

def text_on_screen(text, colour, size, x, y):
    font = pygame.font.SysFont(None, int(size)) #(None, font size)
    tekst_ekraanil = font.render(text, True, colour) #True - anti analysing
    # (text, location)
    screen.blit(tekst_ekraanil, [x, y] )

def sprite(img1, img2, x, y, direction):
    global i
    if direction == "right":
        screen.blit(img1, (x,y))
        pygame.display.update()
        screen.blit(img2, (x,y))
        pygame.display.update()
    if direction == "left":
        img1 = pygame.transform.rotate(img1, 180)
        img2 = pygame.transform.rotate(img2, 180)
        screen.blit(img1, (x, y))
        pygame.display.update()
        screen.blit(img2, (x, y))
    if direction == "up":
        img1 = pygame.transform.rotate(img1, 90)
        img2 = pygame.transform.rotate(img2, 90)
        screen.blit(img1, (x, y))
        pygame.display.update()
    if direction == "down":
        img1 = pygame.transform.rotate(img1, 270)
        img2 = pygame.transform.rotate(img2, 270)
        screen.blit(img1, (x, y))
        pygame.display.update()
        screen.blit(img2, (x, y))
        
def ghosts_move(x, y):
    directions =  ["right", "left", "up", "down"]
    direction = directions[random.randint(0, 3)]
    if str(x - 5 - vel) + ':' + str(y - 5) in seinad: #Kas on sein
            x = x
    else:
        x -= vel
        direction = "left"
    if keys[pygame.K_RIGHT] and x < (screen_width - width - vel):
        if str(x - 5 + vel) + ':' + str(y - 5) in seinad: #Kas on sein
            x = x
        else:
            x += vel
            direction = "right"
    if keys[pygame.K_UP] and y > vel:
        if str(x - 5) + ':' + str(y - 5 - vel) in seinad: #Kas on sein
            y = y
        else:
            y -= vel
            direction = "up"
    if keys[pygame.K_DOWN] and y < (screen_height - height - vel):
        if str(x - 5) + ':' + str(y - 5 + vel) in seinad: #Kas on sein
            y = y
        else:
            y += vel
            direction = "down"

def ghost_image(ghost1, ghost2): #
    pass
    

    
   

for i in range(len(mapTest)):
        for j in range(len(mapTest[i])):
            for k in range(len(mapTest[i][j])):
                if mapTest[i][j][k] == '#': #Wall lists
                    seinad.append(str(k*20) + ':' + str(i*20))
                elif mapTest[i][j][k] == '*': #Score list
                    coins.append(str(k*20) + ':' + str(i*20))
                    
run = True
while run:
    start = time.time()
    clock.tick(fps) #fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        if str(x - 5 - vel) + ':' + str(y - 5) in seinad: #Kas on sein
            x = x
        else:
            x -= vel
            direction = "left"
    if keys[pygame.K_RIGHT] and x < (screen_width - width - vel):
        if str(x - 5 + vel) + ':' + str(y - 5) in seinad: #Kas on sein
            x = x
        else:
            x += vel
            direction = "right"
    if keys[pygame.K_UP] and y > vel:
        if str(x - 5) + ':' + str(y - 5 - vel) in seinad: #Kas on sein
            y = y
        else:
            y -= vel
            direction = "up"
    if keys[pygame.K_DOWN] and y < (screen_height - height - vel):
        if str(x - 5) + ':' + str(y - 5 + vel) in seinad: #Kas on sein
            y = y
        else:
            y += vel
            direction = "down"
 
        
    #Score
    if (str(x - 5) + ':' + str(y - 5)) in coins:
        
        newMap = ''
        score += 1
        #Game gets faster with every collected coin
        fps += 0.1
        coins.remove(str(x - 5) + ':' + str(y - 5))
        
        for i in range(len(mapTest[int(y/20)][0])):
            if i == int(x/20):
                newMap += ' '
            else:
                newMap += mapTest[int(y/20)][0][i]
                
        mapTest[[int(y/20)][0]] = [newMap]
        if score == 288:
            #green on pre-defined muutuja
            finish = time.time()
            time_elapsed = round((finish - start), 2)
            text_on_screen("You win", green, 50, 215, 260) # You win tekst kui score on maksimaalne
            text_on_screen(("Time: " + str(time_elapsed) + " seconds"), green, 50, 215, 300)
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            quit()
    
    screen.fill((0,0,0))
    for i in range(len(mapTest)):
        for j in range(len(mapTest[i])):
            for k in range(len(mapTest[i][j])):
                if mapTest[i][j][k] == '#':
                    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(k*20, i*20, 20, 20))
                elif mapTest[i][j][k] == '*':
                    pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(k*20+7.5, i*20+7.5, 5, 5))
    sprite(img1, img2, x, y, direction)
#    ghosts_move()
    text_on_screen( ("Score: " + str(score)), white, 25, 10, 630)
    pygame.display.update()

pygame.quit()