import pygame
import json
import time
import os

pygame.init()

SIZE = (600,400)
FPS = 60
COLOR = (200,200,200)

difficulty = ['легкий','середній','важкий']
filename = 'settings.json'
current_index = 0
main_font = pygame.font.SysFont('Times New Roman', 36)
main_font0 = pygame.font.SysFont('Times New Roman', 18)
try:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            if data.get("difficulty") in difficulty:
                current_index = difficulty.index(data["difficulty"])
except (FileNotFoundError, json.JSONDecodeError):
        current_index = 0
        with open(filename, 'w') as f:
            json.dump({"difficulty":difficulty[0]}, f)

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
    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

play = Button(200, 80, 200, 50,COLOR, 'ГРАТИ')
settings = Button(200, 160, 200, 50,COLOR, 'СКЛАДНІСТЬ')
exit = Button(200, 240, 200, 50,COLOR, 'ВИЙТИ')

running = True

while running:
    screen.fill((0,0,0))
    diff_text = main_font.render('Складність: ' + difficulty[current_index], True, (200,200,200))
    screen.blit(diff_text, (SIZE[0] // 2 - diff_text.get_width()//2 , 20))

    play.draw()
    settings.draw()
    exit.draw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if exit.is_clicked(e):
            running = False
        if play.is_clicked(e):
            diff_text = main_font0.render('Гра починається зі складністю: ' + difficulty[current_index], True, (200,200,200))
            screen.blit(diff_text, (SIZE[0] // 2 - diff_text.get_width()//2 , 350))
            pygame.display.update()
            time.sleep(2)
            running = False
        if settings.is_clicked(e):
            current_index = (current_index + 1) % len(difficulty)
            with open(filename, 'w') as f:
                json.dump({"difficulty":difficulty[current_index]}, f)
    pygame.display.update()
    clock.tick(FPS)
quit()
