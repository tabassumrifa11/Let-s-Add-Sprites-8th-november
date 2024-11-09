import pygame

import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2



PURPLE = pygame.Color('purple')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')



YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, color, height, width ):
        
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()
        
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]
        
        
    def update(self):
        
        self.rect.move_ip(self.velocity)
        
        boundary_hit = False
        
        if self.rect.left <= 0 or self.rect.right >= 500:
            
            self.velocity[0]= -self.velocity[0]
            boundary_hit = True
            
        
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            
            self.velocity[1]= -self.velocity[1]
            boundary_hit = True
            
            
            
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))

            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
            
            
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
        
        
def change_background_color():
    global bg_color
    bg_color = random.choice([PURPLE, LIGHTBLUE, DARKBLUE])
    
    
all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

sp2 = Sprite(WHITE, 20, 30)
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 370)
all_sprites_list.add(sp2)

sp3 = Sprite(WHITE, 20, 30)
sp3.rect.x = random.randint(0, 480)
sp3.rect.y = random.randint(0, 370)
all_sprites_list.add(sp3)

sp4 = Sprite(WHITE, 20, 30)
sp4.rect.x = random.randint(0, 480)
sp4.rect.y = random.randint(0, 370)
all_sprites_list.add(sp4)

sp5 = Sprite(WHITE, 20, 30)
sp5.rect.x = random.randint(0, 480)
sp5.rect.y = random.randint(0, 370)
all_sprites_list.add(sp5)

sp6 = Sprite(WHITE, 20, 30)
sp6.rect.x = random.randint(0, 480)
sp6.rect.y = random.randint(0, 370)
all_sprites_list.add(sp6)

sp7 = Sprite(WHITE, 20, 30)
sp7.rect.x = random.randint(0, 480)
sp7.rect.y = random.randint(0, 370)
all_sprites_list.add(sp7)

sp8 = Sprite(WHITE, 20, 30)
sp8.rect.x = random.randint(0, 480)
sp8.rect.y = random.randint(0, 370)
all_sprites_list.add(sp8)

sp9 = Sprite(WHITE, 20, 30)
sp9.rect.x = random.randint(0, 480)
sp9.rect.y = random.randint(0, 370)
all_sprites_list.add(sp9)

sp10 = Sprite(WHITE, 20, 30)
sp10.rect.x = random.randint(0, 480)
sp10.rect.y = random.randint(0, 370)
all_sprites_list.add(sp10)

sp11 = Sprite(WHITE, 20, 30)
sp11.rect.x = random.randint(0, 480)
sp11.rect.y = random.randint(0, 370)
all_sprites_list.add(sp11)

sp12 = Sprite(WHITE, 20, 30)
sp12.rect.x = random.randint(0, 480)
sp12.rect.y = random.randint(0, 370)
all_sprites_list.add(sp12)

sp13 = Sprite(WHITE, 20, 30)
sp13.rect.x = random.randint(0, 480)
sp13.rect.y = random.randint(0, 370)
all_sprites_list.add(sp13)

sp14 = Sprite(WHITE, 20, 30)
sp14.rect.x = random.randint(0, 480)
sp14.rect.y = random.randint(0, 370)
all_sprites_list.add(sp14)

sp15 = Sprite(WHITE, 20, 30)
sp15.rect.x = random.randint(0, 480)
sp15.rect.y = random.randint(0, 370)
all_sprites_list.add(sp15)


screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")
bg_color = PURPLE
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()


while not exit:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit = True
            
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
            sp2.change_color()
            sp3.change_color()
            sp4.change_color()
            sp5.change_color()
            sp6.change_color()
            sp7.change_color()
            sp8.change_color()
            sp9.change_color()
            sp10.change_color()
            sp11.change_color()
            sp12.change_color()
            sp13.change_color()
            sp14.change_color()
            sp15.change_color()
            
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()
        
        
    all_sprites_list.update()
    screen.fill(bg_color)
    
    all_sprites_list.draw(screen)
    
    
    pygame.display.flip()
    clock.tick(240)
    
pygame.quit()