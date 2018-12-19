import pygame
import time

#Screen update function
def redrawGameWindow():
    global walkCount, ghost1Y, ghost1Vel, ghost2Y, ghost2Vel, ghost3X, ghost3Vel, ghost4X, ghost4Vel
    
    if walkCount >= 2:
        walkCount = 0
    
    screen.fill((0,0,0))
    for i in range(len(mapTest)):
        for j in range(len(mapTest[i])):
            for k in range(len(mapTest[i][j])):
                if mapTest[i][j][k] == '#':
                    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(k*20, i*20, 20, 20))
                elif mapTest[i][j][k] == '*':
                    pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(k*20+7.5, i*20+7.5, 5, 5))
    
    text_on_screen( ("Score: " + str(score)), white, 25, 10, 630)
    
    if right:
        screen.blit(pacmanRight[walkCount], (x, y))
    if left:
        screen.blit(pacmanLeft[walkCount], (x, y))
    if up:
        screen.blit(pacmanUp[walkCount], (x, y))
    if down:
        screen.blit(pacmanDown[walkCount], (x, y))
        
    
    ###Ghosts movement part###
        
    #Ghost number 1
    screen.blit(ghost1, (ghost1X, ghost1Y))
    
    if ghost1Y == 25:
        ghost1Vel = 20
    if ghost1Y == 525:
        ghost1Vel = ghost1Vel * (-1)
    
    #Checks if there is a collision
    if ghost1X == x and ghost1Y == y-20 or ghost1X == x and ghost1Y == y+20 or ghost1X == x and ghost1Y == y:
        youLostText()
    else:
        ghost1Y += ghost1Vel
    
    #Ghost number 2
    screen.blit(ghost2, (ghost2X, ghost2Y))
    
    if ghost2Y == 525:
        ghost2Vel = 20
    if ghost2Y == 25:
        ghost2Vel = ghost2Vel * (-1)
    
    #Checks if there is a collision
    if ghost2X == x and ghost2Y == y-20 or ghost2X == x and ghost2Y == y+20 or ghost2X == x and ghost2Y == y:
        youLostText()
    else:
        ghost2Y -= ghost2Vel
    
    #Ghost number 3
    screen.blit(ghost3, (ghost3X, ghost3Y))
    
    if ghost3X == 25:
        ghost2Vel = 20
    if ghost3X == 525:
        ghost3Vel = ghost3Vel * (-1)
    
    #Checks if there is a collision
    if ghost3X == x+20 and ghost3Y == y or ghost3X == x-20 and ghost3Y == y or ghost3X == x and ghost3Y == y:
        youLostText()
    else:
        ghost3X += ghost3Vel
        
    #Ghost number 4
    screen.blit(ghost4, (ghost4X, ghost4Y))
    
    if ghost4X == 185:
        ghost4Vel = 20
    if ghost4X == 365:
        ghost4Vel = ghost4Vel * (-1)
    
    #Checks if there is a collision
    if ghost4X == x+20 and ghost4Y == y or ghost4X == x-20 and ghost4Y == y or ghost4X == x and ghost4Y == y:
        youLostText()
    else:
        ghost4X += ghost4Vel
        
    
    pygame.display.update()

def youLostText():
    finishTime = time.time()
    time_elapsed = round((finishTime - startTime), 2)
    text_on_screen("YOU LOST", green, 50, 190, 260)
    text_on_screen(("Time: " + str(time_elapsed) + " seconds"), green, 50, 120, 300)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()
    

#Text drawing function
def text_on_screen(text, colour, size, x, y):
    font = pygame.font.SysFont(None, int(size)) #(None, font size)
    tekst_ekraanil = font.render(text, True, colour) #True - anti analysing
    screen.blit(tekst_ekraanil, [x, y] )

startTime = time.time()

pygame.init()
screen_width = 560
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac - Man")

#Loading sprites
pacmanRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png')]
pacmanLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png')]
pacmanUp = [pygame.image.load('UP1.png'), pygame.image.load('UP2.png')]
pacmanDown = [pygame.image.load('DW1.png'), pygame.image.load('DW2.png')]
ghost1 = pygame.image.load('ghost1.png')
ghost2 = pygame.image.load('ghost2.png')
ghost3 = pygame.image.load('ghost3.png')
ghost4 = pygame.image.load('ghost4.png')


#Changing sprites size
for i in range(len(pacmanRight)):
    pacmanRight[i] = pygame.transform.scale(pacmanRight[i], (10, 10))
    pacmanLeft[i] = pygame.transform.scale(pacmanLeft[i], (10, 10))
    pacmanUp[i] = pygame.transform.scale(pacmanUp[i], (10, 10))
    pacmanDown[i] = pygame.transform.scale(pacmanDown[i], (10, 10))
ghost1 = pygame.transform.scale(ghost1, (10, 10))
ghost2 = pygame.transform.scale(ghost2, (10, 10))
ghost3 = pygame.transform.scale(ghost3, (10, 10))
ghost4 = pygame.transform.scale(ghost4, (10, 10))

#Starting positions
x = 25
y = 285

ghost1X = 125
ghost1Y = 25
ghost2X = 425
ghost2Y = 525
ghost3X = 25
ghost3Y = 585
ghost4X = 365
ghost4Y = 225

#Speed
vel = 20
ghost1Vel = 20
ghost2Vel = -20
ghost3Vel = 20
ghost4Vel = 20


height = 10
width = 10

#Colors
green = (113, 255, 48) #Sõnumi jaoks
white = (255,255,255)

right = True
left = False
up = False
down = False

walkCount = 0

score = 0

clock = pygame.time.Clock()

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
['######*##*###--###*##*######'],
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

for i in range(len(mapTest)):
        for j in range(len(mapTest[i])):
            for k in range(len(mapTest[i][j])):
                if mapTest[i][j][k] == '#' or mapTest[i][j][k] == '-': #Wall lists
                    seinad.append(str(k*20) + ':' + str(i*20))
                elif mapTest[i][j][k] == '*': #Score list
                    coins.append(str(k*20) + ':' + str(i*20))

run = True

while run:
    print(x,y)
    clock.tick(10) #fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        if str(x - 5 - vel) + ':' + str(y - 5) in seinad: #Kas on sein
            x = x
        else:
            x -= vel
            walkCount += 1
            left = True
            right = False
            up = False
            down = False
            
    if keys[pygame.K_RIGHT] and x < (screen_width - width - vel):
        if str(x - 5 + vel) + ':' + str(y - 5) in seinad: #Kas on sein
            x = x
        else:
            x += vel
            walkCount += 1
            right = True
            left = False
            up = False
            down = False
            
    if keys[pygame.K_UP] and y > vel:
        if str(x - 5) + ':' + str(y - 5 - vel) in seinad: #Kas on sein
            y = y
        else:
            y -= vel
            walkCount += 1
            up = True
            down = False
            left = False
            right = False
            
    if keys[pygame.K_DOWN] and y < (screen_height - height - vel):
        if str(x - 5) + ':' + str(y - 5 + vel) in seinad: #Kas on sein
            y = y
        else:
            y += vel
            walkCount += 1
            down = True
            up = False
            left = False
            right = False
    
    
    #Score
    if (str(x - 5) + ':' + str(y - 5)) in coins:
        
        newMap = ''
        score += 1
        coins.remove(str(x - 5) + ':' + str(y - 5))
        
        for i in range(len(mapTest[int(y/20)][0])):
            if i == int(x/20):
                newMap += ' '
            else:
                newMap += mapTest[int(y/20)][0][i]
                
        mapTest[[int(y/20)][0]] = [newMap]
    
    if score == 289:
            #green on pre-defined muutuja
            finishTime = time.time()
            time_elapsed = round((finishTime - startTime), 2)
            text_on_screen("You win", green, 50, 200, 260) # You win tekst kui score on maksimaalne
            text_on_screen(("Time: " + str(time_elapsed) + " seconds"), green, 50, 120, 300)
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            quit()
    
    
    redrawGameWindow()

pygame.quit()
