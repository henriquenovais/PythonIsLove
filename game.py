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
pygame.display.set_caption("Professor Craven's Cool Game")
