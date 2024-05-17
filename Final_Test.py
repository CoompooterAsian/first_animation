import pygame
import math
import random
import time

pygame.init()

# screen settings
WIDTH = 800
HEIGHT = 800
TITLE = "Transcendent Awakening!"
FPS = 60

# Make the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#Colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
BLUE = (103,199,240)

#Fonts
FONT = pygame.font.Font("fonts/smallest_pixel-7.ttf", 35)

pygame.mixer.music.load('music/GohanMusic.ogg')
pygame.mixer.music.play()
pygame.mixer.music.play(-1)

scream = pygame.mixer.Sound("music/scream.ogg")
now = pygame.mixer.Sound("music/Now!.ogg")

# Images

gohan = pygame.image.load('pictures/gohan.png').convert_alpha()

sky = pygame.image.load('pictures/sky.png').convert_alpha()
cloud = pygame.image.load('pictures/cloud.png').convert_alpha()
bg1 = pygame.image.load('pictures/bg1.png').convert_alpha()
bg2 = pygame.image.load('pictures/bg2.png').convert_alpha()
bg3 = pygame.image.load('pictures/bg3.png').convert_alpha()
ground = pygame.image.load('pictures/ground.png').convert_alpha()

aura1 = pygame.image.load('pictures/1.png').convert_alpha()
aura2 = pygame.image.load('pictures/2.png').convert_alpha()
aura3 = pygame.image.load('pictures/3.png').convert_alpha()

impact1 = pygame.image.load('pictures/impact1.png').convert_alpha()
impact2 = pygame.image.load('pictures/impact2.png').convert_alpha()
impact3 = pygame.image.load('pictures/impact3.png').convert_alpha()
impact4 = pygame.image.load('pictures/impact4.png').convert_alpha()

rockup = pygame.image.load("pictures/rock1.png").convert_alpha()

walk1 = pygame.image.load("pictures/walk1.png").convert_alpha()
walk2 = pygame.image.load("pictures/walk2.png").convert_alpha()
walk3 = pygame.image.load("pictures/walk3.png").convert_alpha()
walk4 = pygame.image.load("pictures/walk4.png").convert_alpha()
walk5 = pygame.image.load("pictures/walk5.png").convert_alpha()
walk6 = pygame.image.load("pictures/walk6.png").convert_alpha()
walk7 = pygame.image.load("pictures/walk7.png").convert_alpha()
walk8 = pygame.image.load("pictures/walk8.png").convert_alpha()

beam1 = pygame.image.load("pictures/beam1.png").convert_alpha()
beam2 = pygame.image.load("pictures/beam2.png").convert_alpha()
beam3 = pygame.image.load("pictures/beam3.png").convert_alpha()
beam4 = pygame.image.load("pictures/beam4.png").convert_alpha()
beam5 = pygame.image.load("pictures/beam5.png").convert_alpha()
beam6 = pygame.image.load("pictures/beam6.png").convert_alpha()

rock1 = pygame.image.load("pictures/rock1.png").convert_alpha()

beambg1 = pygame.image.load("pictures/beambg1.png").convert_alpha()
beambg2 = pygame.image.load("pictures/beambg2.png").convert_alpha()
beambg3 = pygame.image.load("pictures/beambg3.png").convert_alpha()
beambg4 = pygame.image.load("pictures/beambg4.png").convert_alpha()
beambg5 = pygame.image.load("pictures/beambg5.png").convert_alpha()
beambg6 = pygame.image.load("pictures/beambg6.png").convert_alpha()

impactbeam1 = pygame.image.load("pictures/impactbeam1.png").convert_alpha()
impactbeam2 = pygame.image.load("pictures/impactbeam2.png").convert_alpha()
impactbeam3 = pygame.image.load("pictures/impactbeam3.png").convert_alpha()
impactbeam4 = pygame.image.load("pictures/impactbeam4.png").convert_alpha()

transition1 = pygame.image.load("pictures/transition1.png").convert_alpha()
transition2 = pygame.image.load("pictures/transition2.png").convert_alpha()
transition3 = pygame.image.load("pictures/transition3.png").convert_alpha()
transition4 = pygame.image.load("pictures/transition4.png").convert_alpha()
transition5 = pygame.image.load("pictures/transition5.png").convert_alpha()
transition6 = pygame.image.load("pictures/transition6.png").convert_alpha()
transition7 = pygame.image.load("pictures/transition7.png").convert_alpha()
transition8 = pygame.image.load("pictures/transition8.png").convert_alpha()
transition9 = pygame.image.load("pictures/transition9.png").convert_alpha()
transition10 = pygame.image.load("pictures/transition10.png").convert_alpha()
transition11 = pygame.image.load("pictures/transition11.png").convert_alpha()

text = pygame.image.load("pictures/text.png").convert_alpha()
hold = pygame.image.load("pictures/hold.png").convert_alpha()

aura_images = [impact1,impact2,impact3,impact4,aura1,aura2,aura3]
walk_images = [walk1,walk2,walk3,walk4,walk5,walk6,walk7,walk8]
beam_images = [beam1,beam2,beam3,beam4,beam5,beam6]
beambg_images = [beambg1,beambg2,beambg3,beambg4,beambg5,beambg6]
impactbeam_images = [impactbeam1,impactbeam2,impactbeam3,impactbeam4,impactbeam4]
transition_images = [transition1,transition2,transition3,transition4,transition5,transition6,transition7,transition8,transition9,transition10,transition11]



x = 0
y = 0

walk_x = 270
walk_y = 0


aura_index = 0
ticks = 0
aura_speed = 3
aura_timer = 0
aura_fade = 0
text_timer = 0
aura_on = False

white_timer = 0
fade_white = 0

walk_index = 0
beam_index = 0
beambg_index = 0
impactbeam_index = 0
transition_index = 0

beam_ticks = 0
walk_ticks = 0
beambg_ticks = 0
impactbeam_ticks = 0
text_ticks = 0
transition_ticks = 0

white_timer = 0
fade_white = 0

beamimpact = 0

beam_speed = 1000
rock1_speed = 6

transition_slide = False
animation = True
running2 = False


num_rockup = 10
rockup_locs = []
for i in range(num_rockup):
    rockup_x = random.randrange(-200, 1000)
    rockup_y = random.randrange(800, 1600)
    rockup_locs.append([rockup_x, rockup_y])
print(rockup_locs)

num_rock1 = 20
rock1_locs = []
for i in range(num_rock1):
    rock1_x = random.randrange(800, 1600)
    rock1_y = random.randrange(0, 800)
    rock1_locs.append([rock1_x, rock1_y])
print(rock1_locs)


def draw_whitesky():
    pygame.draw.rect(screen, WHITE, [0, 0, 800, 800])


def draw_aura(aura_index):
    aura = aura_images[aura_index]
    screen.blit(aura,[x,y])

def draw_gohan():
    screen.blit(gohan, [x, y])

def draw_setting():
    screen.blit(sky, [x, y])
    screen.blit(cloud, [x, y])
    screen.blit(bg1, [x, y])
    screen.blit(bg2, [x, y])

def draw_ground():
    screen.blit(bg3, [x, y])
    screen.blit(ground, [x, y])

def draw_textbox():
    pygame.draw.rect(screen, BLACK, [186, 197, 440, 70])

def draw_rockup(rockup_locs):
    for loc in rockup_locs:
        x, y = loc
        screen.blit(rockup,[x,y])

def draw_blacksky():
        screen.fill(BLACK)

def draw_whiteflash():
    screen.fill(WHITE)

def draw_beam(beam_index):
    beam = beam_images[beam_index]
    screen.blit(beam,[x,y])
    
def draw_walk(walk_index):
    walk = walk_images[walk_index]
    screen.blit(walk,[walk_x,walk_y])

def draw_rock1(rock1_locs):
    for loc in rock1_locs:
        x, y = loc
        screen.blit(rock1,[x,y])

def draw_beambg(beambg_index):
    beambg = beambg_images[beambg_index]
    screen.blit(beambg,[x,y])

def draw_impactbeam(impactbeam_index):
    impactbeam = impactbeam_images[impactbeam_index]
    screen.blit(impactbeam,[x,y])

def draw_transition(transition_index):
    transition = transition_images[transition_index]
    screen.blit(transition,[x,y])

def draw_text():
    screen.blit(text,[x,y])

def draw_hold():
    screen.blit(hold,[x,y+35])


    # Game loop
running = True

while running:


    if animation == True:


        draw_setting()
        draw_ground()
        draw_gohan()

        text_ticks += 1
        if text_ticks > 35:
            draw_text()
            if text_ticks > 70:
                text_ticks = 0



        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        for loc in rockup_locs:
                            loc[0] = random.randrange(-200,1000)
                            loc[1] = random.randrange(800,1600)
                        if aura_on == True:      
                            aura_on = False
                        else:
                            aura_index = 0
                            aura_on = True
                            scream.play()

                        if aura_fade == 0:      
                            aura_fade = 1
                            aura_timer = 0
                            aura_speed = 3
                        else:
                            aura_fade = 0
                    if event.key == pygame.K_a:
                        transition_slide = True
                            
                        
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        fade_white = 1      

        if aura_on == True:
            draw_aura(aura_index)
            if ticks > 12:
                draw_rockup(rockup_locs)


        if aura_fade == 0:
            aura_timer += 1

        if 150 > aura_timer > 80:
            aura_speed = 4

        if aura_timer > 150:
            aura_speed = 6

        pressed = pygame.key.get_pressed()

        ticks += 1

        if ticks % aura_speed == 0:
            aura_index += 1
            
            if aura_index == 7:
                aura_index = 4

        if transition_slide == True:
            draw_transition(transition_index)
            transition_ticks += 1
                        
            if transition_ticks % 4 == 0:
                transition_index += 1
            
        if transition_index == 11:
            transition_index = 0 
            animation = False
            transition_slide = False

        text_timer += 1

        if 50 < text_timer < 250:
            draw_textbox()
            text1 = FONT.render("I can never forgive you", True, WHITE)
            text2 = FONT.render("for what you've done!", True, WHITE)
            screen.blit(text1, [210, 200])
            screen.blit(text2, [230, 230])

        for loc in rockup_locs:
            loc[1] -= 3

            if loc[1] < -300:
               loc[0] = random.randrange(-200,1000)
               loc[1] = random.randrange(800,1600)

        if fade_white == 1 and aura_on == False:
            white_timer += 1
            if white_timer > 2:
                draw_whitesky()
        if white_timer > 10:
            white_timer = 0
            fade_white = 0

        pygame.display.update()

        clock.tick(FPS)


        # Close window and quit

    else:
        running2 = True
        fade_white = 1
        
        
        # Game loop
        while running2:
            # Input handling
            '''
            This is where we React to key presses, mouse clicks, etc. For now,
            we'll just check to see if the X is clicked.
            '''
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running2 = False
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            running2 = False
                            animation = True
                        if event.key == pygame.K_LEFT:
                            now.play()
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            impactbeam_index = 0
                            fade_white = 1

                            
                            

            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_LEFT]:
                if walk_ticks % 10 == 0:
                    beam_speed -= 1
                if walk_ticks % 30 == 0:
                    walk_index += 1
                if beam_speed < 4:
                    if walk_index == 8:
                        walk_index = 4
                if beam_speed == 2:
                    beam_speed = 3
            else:
                beam_speed = 10
                if walk_ticks % 30 == 0:
                    walk_index += 1
                
                if walk_index > 3:
                    walk_index = 0




            # Logic

            beam_ticks += 1
            walk_ticks += 1
            beambg_ticks += 1
            if 5 >= beam_speed >= 4:
                impactbeam_ticks += 1


            if beambg_ticks % 5 == 0:
                beambg_index += 1
            
                if beambg_index == 6:
                    beambg_index = 0

            if impactbeam_ticks % 5 == 0:
                impactbeam_index += 1
                    
                if impactbeam_index > 4:
                    impactbeam_index = 0
                    

            if beam_ticks % beam_speed == 0:
                beam_index += 1
                
                if beam_index == 6:
                    beam_index = 0


            for loc in rock1_locs:
                loc[0] -= rock1_speed

                if loc[0] < -300:
                   loc[0] = 800
                   loc[0] = random.randrange(800,1600)
                   loc[1] = random.randrange(-200,800)

            if beam_speed < 4:
                rock1_speed = 20
            else:
                rock1_speed = 5
                

            
            # Drawing code
            '''
            Understand that nothing is actully drawn on the screen here. Instead,
            the picture is assembled in the computers memory.
            '''
            draw_blacksky()
            if beam_speed < 4:
                draw_beambg(beambg_index)
                draw_rock1(rock1_locs)
                
            draw_beam(beam_index)
            draw_walk(walk_index)
            if 5 >= beam_speed >= 4:
                walk_index = 4
                draw_impactbeam(impactbeam_index)

            text_ticks += 1
            if text_ticks > 20:
                draw_hold()
            if text_ticks > 40:
                text_ticks = 0
                
            if fade_white == 1:
                white_timer += 1
                draw_whiteflash()
                walk_index = 4
                draw_impactbeam(impactbeam_index)
                if white_timer == 15:
                    white_timer = 0
                    fade_white = 0
                

            # Update screen (Actually draw the picture in the screen.)
            '''
            The update() function takes the picture from the computer's memory buffer
            and actually puts it on the screen.
            '''
            pygame.display.update()


            # Limit refresh rate of game loop
            '''
            The game loop will pause for a bit here so that the screen refreshes at
            the desired rate.
            '''
            clock.tick(FPS)


        # Close window and quit
pygame.quit()

