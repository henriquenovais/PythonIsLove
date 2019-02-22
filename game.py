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
PI = 3.141592653

#Openning window and setting window size:
size = (700, 500)
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

    #DRAWING LINES
    pygame.draw.line(screen, RED, [0, 0], [100, 100], 15) #Drawing red line
    pygame.draw.rect(screen, RED, [500, 50, 170, 170], 0) #Drawing red rectangle
    # Draw on the screen several lines from (0, 10) to (100, 110)
    # 5 pixels wide using a for loop
    y_offset = 0
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)

    #DRAWING A RECTANGLE
    # Draw a rectangle
    pygame.draw.rect(screen,BLACK,[240,100,250,100],2)

    #DRAWING AN ELLIPSE
    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [200,250,250,100], 2)

    #DRAWING AN ARC
    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(screen, GREEN, [450,250,250,200],  PI/2,     PI, 2)
    pygame.draw.arc(screen, BLACK, [450,250,250,200],     0,   PI/2, 2)
    pygame.draw.arc(screen, RED,   [450,250,250,200],3*PI/2,   2*PI, 2)
    pygame.draw.arc(screen, BLUE,  [450,250,250,200],    PI, 3*PI/2, 2)

    # DRAWING POLYGONS
    # The function detects the polygon based on the number of points declared
    #The last attribute controls the thickness of the polygon's lines
    pygame.draw.polygon(screen, BLACK, [[50,200], [50,400], [400,200]], 10)

    #DRAWING TEXT
    #Define a font to be used and store it in a variable:
    #The method requires inputs that define , respectively, font type, size, bolding and italicize.
    font1 = pygame.font.SysFont('Calibri',40,True,False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters, but does not put it on the screen yet.
    string1 = "CASTLEVANIA"
    text1 = font1.render("The name of this game is " + string1,False,BLACK)
    # Put the image of the text on the screen at 250x250
    screen.blit(text1, [70, 450])


 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

