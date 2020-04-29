# Library imports
import pygame

# Local imports
# (None)

# Logger import
from Logger.Logger import logger

# Initialize pygame
pygame.init()
pygame.display.init()
pygame.joystick.init()

# Sprites
moveRight = [pygame.image.load('Sprites/PacMan_Animate1.png')
            ,pygame.image.load('Sprites/PacMan_Animate2.png')
            ,pygame.image.load('Sprites/PacMan_Animate3.png')
            ,pygame.image.load('Sprites/PacMan_Animate4.png')
            ,pygame.image.load('Sprites/PacMan_Animate5.png')
            ,pygame.image.load('Sprites/PacMan_Animate4.png')
            ,pygame.image.load('Sprites/PacMan_Animate3.png')
            ,pygame.image.load('Sprites/PacMan_Animate2.png')
            ,pygame.image.load('Sprites/PacMan_Animate1.png')]

background = pygame.image.load('Images/PacMazeBig1.png')

# Screen size constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 886

# Character Info
character_x = 500
character_y = 500
character_radius = 25
character_width = 40
character_height = 60
movement = "Right"
moveCount = 0

character_vel = 15
character_weight = 5

#Controllers
joyCount = pygame.joystick.get_count()
logger.debug("JoySticks Connected: " + str(joyCount))

#Keyboard
inputs = pygame.key.get_pressed()

#Controller
usedJoy = False
if joyCount > 0:
    usedJoy = True
joystick = pygame.joystick.Joystick(0)
joystick.init()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zen Mode Pac-Man")
clock = pygame.time.Clock()

def updateGameWindow():
    global moveCount

    #Window Image
    window.blit(background, (0, 0))
    #Character Image
    if moveCount + 1 >= 10:
        moveCount = 0

    window.blit(moveRight[moveCount], (character_x, character_y))
    moveCount += 1
    pygame.display.update()

def updateMovement():
    global character_x, character_y


    #Switch Pro Controller
    #JOYSTICKS
    stick1_horiz = joystick.get_axis(0)
    stick1_vert = joystick.get_axis(1)
    stick2_horiz = joystick.get_axis(2)
    stick2_vert = joystick.get_axis(3)

    #A, B, X, Y
    Button_B = joystick.get_button(0)
    Button_A = joystick.get_button(1)
    Button_X = joystick.get_button(2)
    Button_Y = joystick.get_button(3)

    #Shoulders and Triggers
    Shoulder_L = joystick.get_button(4)
    Shoulder_R = joystick.get_button(5)
    Trigger_L = joystick.get_button(6)
    Trigger_R = joystick.get_button(7)

    #Plus, Minus, Home, Capture
    Minus = joystick.get_button(8)
    Plus = joystick.get_button(9)
    Home = joystick.get_button(12)
    Capture = joystick.get_button(13)

    #DPAD
    hats = joystick.get_numhats()
    Dpad = joystick.get_hat(0)

    if not usedJoy:
        if inputs[pygame.K_UP] and character_y > (character_radius+5):
            character_y -= character_vel
        if inputs[pygame.K_DOWN] and character_y < (SCREEN_WIDTH-character_radius-5):
            character_y += character_vel
        if inputs[pygame.K_LEFT] and character_x > (character_radius+5):
            character_x -= character_vel
        if inputs[pygame.K_RIGHT] and character_x < (SCREEN_HEIGHT-character_radius-5):
            character_x += character_vel
    if usedJoy == True:
        #Right Dpad
        if Dpad == (1, 0):
            if (character_x + character_vel) > SCREEN_WIDTH-64:
                character_x = SCREEN_WIDTH-64
            else:
                character_x += character_vel
            movement = "Right"
        #Left Dpad
        if Dpad == (-1, 0):
            if (character_x - character_vel) < 0:
                character_x = 0
            else:
                character_x -= character_vel
            movement = "Left"
        #Up Dpad
        if Dpad == (0, 1):
            if (character_y - character_vel) < 0:
                character_y = 0
            else:
                character_y -= character_vel
            movement = "Up"
        #Down Dpad
        if Dpad == (0, -1):
            if (character_y + character_vel) > SCREEN_HEIGHT-64:
                character_y = SCREEN_HEIGHT-64
            else:
                character_y += character_vel
            movement = "Down"

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

if __name__ == "__main__":
    logger.debug("Start")

    running = True

    # Main Loop
    while running:

        # Loop through the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Flip the display
        pygame.display.flip()

        updateMovement()
        updateGameWindow()
        clock.tick(30)

    pygame.quit()