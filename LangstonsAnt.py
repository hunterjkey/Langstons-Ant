import pygame
import time
import random
import os
import sys
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
sizeX = 700
sizeY = 500
size = (sizeX, sizeY)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Langston's Ant")

#----- Setup -------

# Loop until the user clicks the close button.
done = False

#variables
borderwidth = 10
gridWidth = 10
gridX = []
gridY = []
gridcolor = []
Activated = False
firstpress = True
antX = 0
antY = 0
antXvelocity = 0
antYvelocity = gridWidth
Break = False
rest = 12

blackSelect = "left"
whiteSelect = "right"
redSelect = "off"
greenSelect = "off"
purpleSelect = "off"

#create grid
currentgridX = borderwidth
currentgridY = borderwidth
for i in range(int((sizeY-(borderwidth*2))/gridWidth)):
    for i in range(int((sizeX-(borderwidth*2)-80)/gridWidth)):
        gridX.append(currentgridX)
        gridY.append(currentgridY)
        currentgridX+=gridWidth
    currentgridX = borderwidth
    currentgridY += gridWidth
for i in range(len(gridX)):
    gridcolor.append(BLACK)
    
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key
            if event.key == pygame.K_UP:
                rest += 1
            elif event.key == pygame.K_DOWN:
                rest -= 1

            
    # background image and grid.
    screen.fill(BLACK)

    for i in range(len(gridX)):
        pygame.draw.rect(screen,gridcolor[i],[gridX[i],gridY[i],gridWidth,gridWidth])
        pygame.draw.rect(screen,WHITE,[gridX[i],gridY[i],gridWidth,gridWidth], 1)
    pygame.draw.rect(screen,BLUE,[antX,antY,gridWidth,gridWidth])

    Resetfont = pygame.font.SysFont('Calibri', 24, True, False)
    text = Resetfont.render("RESET",True,RED)
    screen.blit(text, [sizeX-75, sizeY-borderwidth-22])
    pygame.draw.rect(screen,RED,[sizeX-85,sizeY-borderwidth-25,80,25], 2)

    #selector boxes
    if blackSelect == "left":
        blackBox = [sizeX-80, borderwidth+20,35,20]
    elif blackSelect == "right":
        blackBox = [sizeX-45, borderwidth+20,35,20]
    elif blackSelect == "straight":
        blackBox = [sizeX-45, borderwidth+40,35,20]

    if whiteSelect == "left":
        whiteBox = [sizeX-80, borderwidth+90,35,20]
    elif whiteSelect == "right":
        whiteBox = [sizeX-45, borderwidth+90,35,20]
    elif whiteSelect == "straight":
        whiteBox = [sizeX-45, borderwidth+110,35,20]

    if redSelect == "left":
        redBox = [sizeX-80, borderwidth+160,35,20]
    elif redSelect == "right":
        redBox = [sizeX-45, borderwidth+160,35,20]
    elif redSelect == "off":
        redBox = [sizeX-80, borderwidth+180,35,20]
    elif redSelect == "straight":
        redBox = [sizeX-45, borderwidth+180,35,20]

    if greenSelect == "left":
        greenBox = [sizeX-80, borderwidth+230,35,20]
    elif greenSelect == "right":
        greenBox = [sizeX-45, borderwidth+230,35,20]
    elif greenSelect == "off":
        greenBox = [sizeX-80, borderwidth+250,35,20]
    elif greenSelect == "straight":
        greenBox = [sizeX-45, borderwidth+250,35,20]

    if purpleSelect == "left":
        purpleBox = [sizeX-80, borderwidth+300,35,20]
    elif purpleSelect == "right":
        purpleBox = [sizeX-45, borderwidth+300,35,20]
    elif purpleSelect == "off":
        purpleBox = [sizeX-80, borderwidth+320,35,20]
    elif purpleSelect == "straight":
        purpleBox = [sizeX-45, borderwidth+320,35,20]

    pygame.draw.rect(screen,GREEN,blackBox)
    pygame.draw.rect(screen,GREEN,whiteBox)
    pygame.draw.rect(screen,GREEN,redBox)
    pygame.draw.rect(screen,GREEN,greenBox)
    pygame.draw.rect(screen,GREEN,purpleBox)
    
    # --- Game logic should go here

    #Mouse detection
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

    #Code for direction selection
    if pressed1:
        #reset button
        if (mouseX >= sizeX-80) and (mouseX < sizeX-5) and (mouseY >= sizeY-30-borderwidth) and (mouseY < sizeY-borderwidth):
            for i in range(len(gridcolor)):
                gridcolor[i] = BLACK
                Activated = False
                antX, antY = 0, 0
                firstpress = True
        #direction buttons
        else:
            for i in range(5):
                if (mouseX >= sizeX-80) and (mouseX < sizeX-45) and (mouseY >= borderwidth+20+(70*i)) and (mouseY < borderwidth+40+(70*i)):
                    if (i==0):
                        blackSelect = "left"
                    elif (i==1):
                        whiteSelect = "left"
                    elif (i==2):
                        redSelect = "left"
                    elif (i==3) and (redSelect != "off"):
                        greenSelect = "left"
                    elif (i==4) and (greenSelect != "off"):
                        purpleSelect = "left"
                elif (mouseX >= sizeX-45) and (mouseX < sizeX-10) and (mouseY >= borderwidth+20+(70*i)) and (mouseY < borderwidth+40+(70*i)):
                    if (i==0):
                        blackSelect = "right"
                    elif (i==1):
                        whiteSelect = "right"
                    elif (i==2):
                        redSelect = "right"
                    elif (i==3) and (redSelect != "off"):
                        greenSelect = "right"
                    elif (i==4) and (greenSelect != "off"):
                        purpleSelect = "right"
                elif (mouseX >= sizeX-80) and (mouseX < sizeX-45) and (mouseY >= borderwidth+40+(70*i)) and (mouseY < borderwidth+60+(70*i)):
                    if (i==2) and (greenSelect == "off"):
                        redSelect = "off"
                    elif (i==3) and (purpleSelect == "off"):
                        greenSelect = "off"
                    elif (i==4):
                        purpleSelect = "off"
                elif (mouseX >= sizeX-45) and (mouseX < sizeX-10) and (mouseY >= borderwidth+40+(70*i)) and (mouseY < borderwidth+60+(70*i)):
                    if (i==0):
                        blackSelect = "straight"
                    elif (i==1):
                        whiteSelect = "straight"
                    elif (i==2):
                        redSelect = "straight"
                    elif (i==3) and (redSelect != "off"):
                        greenSelect = "straight"
                    elif (i==4) and (greenSelect != "off"):
                        purpleSelect = "straight"
        

    #code that follows the mouse for initial ant placement
    if (Activated == False):
        conflict = False
        for i in range(len(gridX)):
            if (mouseX-gridX[i]<gridWidth) and (mouseX-gridX[i]>0) and (mouseY-gridY[i]<gridWidth) and (mouseY-gridY[i]>0):
                pygame.draw.rect(screen, WHITE, [gridX[i],gridY[i],gridWidth,gridWidth])
                placementX = gridX[i]
                placementY = gridY[i]
        if pressed1 and (mouseX < sizeX-85):
            Activated = True
            if (firstpress == True):
                firstpress = False
                if (mouseX >= borderwidth) and (mouseX <= sizeX-borderwidth) and (mouseY >= borderwidth) and (mouseY <= sizeY-borderwidth):
                    antX = placementX
                    antY = placementY
            else:
                firstpress = True
    else:
        for i in range(len(gridX)):
            if (gridX[i]==antX) and (gridY[i]==antY) and (Break == False):
                Break = True
                if (gridcolor[i]==PURPLE):
                    turn = purpleSelect
                elif (gridcolor[i]==GREEN):
                    if (purpleSelect != "off"):
                        gridcolor[i] = PURPLE
                    turn = greenSelect
                elif (gridcolor[i]==RED):
                    if (greenSelect != "off"):
                        gridcolor[i] = GREEN
                    turn = redSelect
                elif (gridcolor[i]==WHITE):
                    if (redSelect != "off"):
                        gridcolor[i] = RED
                    turn = whiteSelect
                elif (gridcolor[i]==BLACK):
                    gridcolor[i] = WHITE
                    turn = blackSelect

                if (turn=="right"):
                    if (antXvelocity==gridWidth) and (antYvelocity==0):
                        antXvelocity = 0
                        antYvelocity = gridWidth
                    elif (antXvelocity==-gridWidth) and (antYvelocity==0):
                        antXvelocity = 0
                        antYvelocity = -gridWidth
                    elif (antXvelocity==0) and (antYvelocity==gridWidth):
                        antXvelocity = -gridWidth
                        antYvelocity = 0
                    elif (antXvelocity==0) and (antYvelocity==-gridWidth):
                        antXvelocity = gridWidth
                        antYvelocity = 0
                elif (turn=="left"):
                    if (antXvelocity==gridWidth) and (antYvelocity==0):
                        antXvelocity = 0
                        antYvelocity = -gridWidth
                    elif (antXvelocity==-gridWidth) and (antYvelocity==0):
                        antXvelocity = 0
                        antYvelocity = gridWidth
                    elif (antXvelocity==0) and (antYvelocity==gridWidth):
                        antXvelocity = gridWidth
                        antYvelocity = 0
                    elif (antXvelocity==0) and (antYvelocity==-gridWidth):
                        antXvelocity = -gridWidth
                        antYvelocity = 0
                
        Break = False
        
        antX += antXvelocity
        antY += antYvelocity
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [sizeX-85, borderwidth, 80, sizeY-(borderwidth*2)-30], 2)

    """The text:"""
    startfont = pygame.font.SysFont('Calibri', 12, True, False)
    smallerfont = pygame.font.SysFont('Calibri', 8, True, False)
    text = startfont.render("Black",True,WHITE)
    screen.blit(text, [sizeX-60, borderwidth+6])
    text = startfont.render("White",True,WHITE)
    screen.blit(text, [sizeX-60, borderwidth+76])
    text = startfont.render("Red",True,RED)
    screen.blit(text, [sizeX-54, borderwidth+146])
    text = startfont.render("Green",True,GREEN)
    screen.blit(text, [sizeX-60, borderwidth+216])
    text = startfont.render("Purple",True,PURPLE)
    screen.blit(text, [sizeX-60, borderwidth+288])

    #speed
    text = startfont.render("Speed:",True,WHITE)
    screen.blit(text, [sizeX-80, sizeY-borderwidth-60])
    if rest>6:
        text = startfont.render("6/"+str(rest)+" seconds",True,WHITE)
        screen.blit(text, [sizeX-80, sizeY-borderwidth-45])
    elif rest == 6:
        text = startfont.render("1 second",True,WHITE)
        screen.blit(text, [sizeX-80, sizeY-borderwidth-45])
    else:
        text = startfont.render("LOTSA seconds",True,WHITE)
        screen.blit(text, [sizeX-80, sizeY-borderwidth-45])
        
    """The Selecter Rectangles"""
    for i in range(5):
        pygame.draw.rect(screen, WHITE, [sizeX-80, borderwidth+20+(70*i), 35, 20], 2)
        pygame.draw.rect(screen, WHITE, [sizeX-45, borderwidth+20+(70*i), 35, 20], 2)
        if (i>1):
            pygame.draw.rect(screen, WHITE, [sizeX-80, borderwidth+40+(70*i), 35, 20], 2)
            text = startfont.render("Off",True,WHITE)
            screen.blit(text, [sizeX-70, borderwidth+46+(70*i)])
        pygame.draw.rect(screen, WHITE, [sizeX-45, borderwidth+40+(70*i), 35, 20], 2)

        text = startfont.render("Left",True,WHITE)
        screen.blit(text, [sizeX-72, borderwidth+26+(70*i)])
        text = startfont.render("Right",True,WHITE)
        screen.blit(text, [sizeX-40, borderwidth+26+(70*i)])
        text = smallerfont.render("Straight",True,WHITE)
        screen.blit(text, [sizeX-40, borderwidth+48+(70*i)])
   
    pygame.display.flip()
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)


    #potential time wait
    if rest>5:
        time.sleep((6/rest))
# Close the window and quit.
pygame.quit()
