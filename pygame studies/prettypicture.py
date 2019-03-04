# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Define some colors:
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
MUDBROWN = ( 135,  64,   8)
MIDNIGHTBLUE = ( 25, 25, 112)
DIMGREY = ( 105, 105, 105)
PI = 3.141592653

#Openning window and setting window size:
size = (1300, 800)
screen = pygame.display.set_mode(size)
#Set caption to the game screen:
pygame.display.set_caption("Henrique's Cool Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    #DRAWING BACKGROUND
    #Big blue rectangle in order to create the sky
    pygame.draw.rect(screen,MIDNIGHTBLUE,[0,0,1300,1300]) 
    #DRAWING SOIL CLIFFS
    #Drawing brown rectangles alongside triangles in order to create two cliffs
    pygame.draw.rect(screen,MUDBROWN,[0,400,300,400]) #The rectangle is completely filled with color, that's why there's no last argument
    pygame.draw.rect(screen,MUDBROWN,[1000,400,300,400]) 
    pygame.draw.polygon(screen,MUDBROWN,[[300,400],[300,800],[400,400]])
    pygame.draw.polygon(screen,MUDBROWN,[[1000,400],[1000,800],[900,400]])
    #DRAW CASTLE
    #Three triangles and one rectangle to create the castle base
    pygame.draw.polygon(screen,DIMGREY,[[300,300],[450,300],[375,400]]) #Small triangle one
    pygame.draw.polygon(screen,DIMGREY,[[450,300],[750,300],[600,500]]) #Big triangle
    pygame.draw.polygon(screen,DIMGREY,[[750,300],[900,300],[825,400]]) #Small triangle two
    pygame.draw.rect(screen,DIMGREY,[300,280,601,20]) #Rectangle for the castle base
    #Three rectangles for the castle's towers 
    pygame.draw.rect(screen,DIMGREY,[300,140,150,145]) #Small tower 1
    pygame.draw.rect(screen,DIMGREY,[450,80,300,200]) #Big tower 
    pygame.draw.rect(screen,DIMGREY,[750,140,151,145]) #Small tower 2
    #Two triangles for the tip of the two small towers
    pygame.draw.polygon(screen,DIMGREY,[[300,140],[450,140],[375,80]])
    pygame.draw.polygon(screen,DIMGREY,[[750,140],[900,140],[825,80]])
    #Five rectangles for the tip of the big tower
    for x in range(0,10):
        pygame.draw.rect(screen,DIMGREY,[451+(31*x),70,20,10])
    



 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

