import pygame
import json

pygame.init()

SIZE = (600,400)
FPS = 60
COLOR = (200,200,200)

difficulty = ['легкий','середній','важкий']
filename = 'settings.json'
current_index = 0
main_font = pygame.font.SysFont('Times New Roman', 36)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

class Button:
    def __init__(self, x,y, w,h,color, text, color_text=(0,0,0)):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
        self.text = text
        self.text_color = color_text
        self.font = pygame.font.SysFont('Times New Roman', 28)
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.text_surf = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        screen.blit(self.text_surf, self.text_rect)

play = Button(200, 80, 200, 50,COLOR, 'ГРАТИ')
settings = Button(200, 160, 200, 50,COLOR, 'СКЛАДНІСТЬ')
exit = Button(200, 240, 200, 50,COLOR, 'ВИЙТИ')

running = True

while running:
    diff_text = main_font.render('Складність: ' + difficulty[current_index], True, (200,200,200))
    screen.blit(diff_text, (SIZE[0] // 2 - diff_text.get_width()//2 , 20))
    
    play.draw()
    settings.draw()
    exit.draw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
quit()
