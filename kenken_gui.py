
from inspect import trace
from re import S
from cv2 import solve
import pygame, sys

from sqlalchemy import false
import puzzle_generation
from random import randint
import backtracking

        

WIDTH = 1000
original_grid_element_color = (52, 31, 151)
background_color = (255,255,255)

colors= []
for r  in range(20 ,255 , 80):
    for b  in range(0 ,255 , 80):
        for g  in range(10,255 , 80):
          colors.append((r,g,b))  

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def init_win():
    mainClock = pygame.time.Clock()
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("kenken")
    win.fill(background_color)
    image = pygame.image.load(r'download.png')
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    button_font = pygame.font.SysFont('Comic Sans MS', 28)

    win.fill((255,255,255))
    draw_text('Select Puzzle Size', myfont, (0, 0, 0), win, 20, 350)

    button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
    button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
    button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
    button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
    button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
    button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
    button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

    draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
    draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
    draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
    draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
    draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
    draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
    draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)

    button_gen = pygame.draw.rect(win, (75, 173, 73), pygame.Rect(350, 800, 300, 75))
    draw_text('Generate Board', button_font, (255, 255, 255), win, 400, 815)

    while True:
        win.blit(image, (300, 100))
        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        global cliques, size

        if button_1.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                size = 3
                button_1 = pygame.draw.ellipse(win, (0, 0, 0), pygame.Rect(50, 455, 150, 75))
                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
        if button_2.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                size = 4
                button_2 = pygame.draw.ellipse(win, (0, 0, 0), pygame.Rect(300, 455, 150, 75))
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
        if button_3.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                size = 5
                button_3 = pygame.draw.ellipse(win, (0, 0, 0), pygame.Rect(550, 455, 150, 75))
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
        if button_4.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                size = 6
                button_4 = pygame.draw.ellipse(win, (0, 0, 0), pygame.Rect(800, 455, 150, 75))
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
        if button_5.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                size = 7
                button_5 = pygame.draw.ellipse(win, (0, 0, 0), pygame.Rect(175, 555, 150, 75))
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
        if button_6.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                size = 8
                button_6 = pygame.draw.ellipse(win, (0, 0, 0), pygame.Rect(425, 555, 150, 75))
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
        if button_7.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                size = 9
                button_7 = pygame.draw.ellipse(win, (0, 0, 0), pygame.Rect(675, 555, 150, 75))
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)

        if button_gen.collidepoint((mx, my)):
            if click[0]:
                button_1 = pygame.draw.ellipse(win, (189, 15, 111), pygame.Rect(50, 455, 150, 75))
                button_2 = pygame.draw.ellipse(win, (7, 168, 20), pygame.Rect(300, 455, 150, 75))
                button_3 = pygame.draw.ellipse(win, (10, 73, 145), pygame.Rect(550, 455, 150, 75))
                button_4 = pygame.draw.ellipse(win, (45, 130, 227), pygame.Rect(800, 455, 150, 75))
                button_5 = pygame.draw.ellipse(win, (212, 205, 4), pygame.Rect(175, 555, 150, 75))
                button_6 = pygame.draw.ellipse(win, (227, 144, 20), pygame.Rect(425, 555, 150, 75))
                button_7 = pygame.draw.ellipse(win, (181, 30, 16), pygame.Rect(675, 555, 150, 75))

                draw_text('3x3', button_font, (255, 255, 255), win, 100, 470)
                draw_text('4x4', button_font, (255, 255, 255), win, 350, 470)
                draw_text('5x5', button_font, (255, 255, 255), win, 600, 470)
                draw_text('6x6', button_font, (255, 255, 255), win, 850, 470)
                draw_text('7x7', button_font, (255, 255, 255), win, 225, 570)
                draw_text('8x8', button_font, (255, 255, 255), win, 475, 570)
                draw_text('9x9', button_font, (255, 255, 255), win, 725, 570)
                cliques = puzzle_generation.generate(size)
                draw(cliques, size)

        pygame.display.update()
        mainClock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

def draw(cliques, size):   
    mainClock = pygame.time.Clock() 
    pygame.init()
    win_2 = pygame.display.set_mode((1400, WIDTH))
    pygame.display.set_caption("kenken")
    win_2.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 180//size)
    button_font = pygame.font.SysFont('Comic Sans MS', 28)
    myfont2 = pygame.font.SysFont('Comic Sans MS', 42)

    draw_text('Select Solving', myfont2, (0, 0, 0), win_2, 20, 50)
    draw_text('Algorithm:', myfont2, (0, 0, 0), win_2, 20, 110)

    button_algo1 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 225, 350, 115))
    button_algo2 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 375, 350, 115))
    button_algo3 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 525, 350, 115))

    draw_text('Backtracking', button_font, (255, 255, 255), win_2, 140, 260)
    draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 390)
    draw_text('forward checking', button_font, (255, 255, 255), win_2, 110, 425)
    draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 540)
    draw_text('arc consistency', button_font, (255, 255, 255), win_2, 130, 575)

    button_solve = pygame.draw.rect(win_2, (75, 173, 73), pygame.Rect(130, 700, 200, 75))
    draw_text('Solve', button_font, (255, 255, 255), win_2, 195, 715)

    button_font3 = pygame.font.SysFont('Comic Sans MS', 19)
    button_solve8 = pygame.draw.rect(win_2, (75, 173, 73), pygame.Rect(130, 820, 200, 75))
    draw_text('Generate New Board', button_font3, (255, 255, 255), win_2, 140, 835)

    x =0 
    w=((WIDTH-100)//size)
    for clique in cliques:
        index ,op, target = clique
        color = colors[randint(0, len(colors)-1)]
        colors.remove(color) 
        for i in index:
            shape_surf = pygame.Surface(pygame.Rect(((450+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w )).size,pygame.SRCALPHA )
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            shape_surf.set_alpha(100)
            win_2.blit(shape_surf,((450+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w) )
        value = myfont.render(str(target), True, (0,0,0))
        win_2.blit(value, (( (index[0][0]-1) *w )+455 ,((index[0][1]-1)*w )+55 ))
        if op != '.':
            value = myfont.render(op, True, (0,0,0))
            win_2.blit(value, ( ( (index[0][0]-1) *w )+475+ ((6*9)//size)*len(str(target) ) , ((index[0][1]-1)*w )+50 ))
        
    for i in range(size+1):
        pygame.draw.line(win_2, (0,0,0), (450 +w*i, 50), (450 + w*i ,950 ), 2 )
        pygame.draw.line(win_2, (0,0,0), (450, 50 + w*i), (1350, 50 + w*i), 2 )
    pygame.display.update()
    ken = puzzle_generation.Kenken(size, cliques)
    but_pressed =0 
    solved=0
    while True : 
        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if button_algo1.collidepoint((mx, my)):
            if click[0] and solved==0:
                button_algo1 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 225, 350, 115))
                button_algo2 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 375, 350, 115))
                button_algo3 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 525, 350, 115))

                draw_text('Backtracking', button_font, (255, 255, 255), win_2, 140, 260)
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 390)
                draw_text('forward checking', button_font, (255, 255, 255), win_2, 110, 425)
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 540)
                draw_text('arc consistency', button_font, (255, 255, 255), win_2, 130, 575)
                button_algo1 = pygame.draw.rect(win_2, (0, 0, 0), pygame.Rect(50, 225, 350, 115))
                draw_text('Backtracking', button_font, (255, 255, 255), win_2, 140, 260)
                but_pressed =1
            
        if button_algo2.collidepoint((mx, my)):
            if click[0] and solved==0:
                button_algo1 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 225, 350, 115))
                button_algo2 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 375, 350, 115))
                button_algo3 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 525, 350, 115))

                draw_text('Backtracking', button_font, (255, 255, 255), win_2, 140, 260)
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 390)
                draw_text('forward checking', button_font, (255, 255, 255), win_2, 110, 425)
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 540)
                draw_text('arc consistency', button_font, (255, 255, 255), win_2, 130, 575)
                button_algo2 = pygame.draw.rect(win_2, (0, 0, 0), pygame.Rect(50, 375, 350, 115))
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 390)
                draw_text('forward checking', button_font, (255, 255, 255), win_2, 110, 425)
                but_pressed =2
        if button_algo3.collidepoint((mx, my)):
            if click[0] and solved==0:
                button_algo1 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 225, 350, 115))
                button_algo2 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 375, 350, 115))
                button_algo3 = pygame.draw.rect(win_2, (95, 116, 161), pygame.Rect(50, 525, 350, 115))

                draw_text('Backtracking', button_font, (255, 255, 255), win_2, 140, 260)
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 390)
                draw_text('forward checking', button_font, (255, 255, 255), win_2, 110, 425)
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 540)
                draw_text('arc consistency', button_font, (255, 255, 255), win_2, 130, 575)
                button_algo3 = pygame.draw.rect(win_2, (0, 0, 0), pygame.Rect(50, 525, 350, 115))
                draw_text('Backtracking with', button_font, (255, 255, 255), win_2, 110, 540)
                draw_text('arc consistency', button_font, (255, 255, 255), win_2, 130, 575)
                but_pressed =3

        assignments={}
        if button_solve.collidepoint((mx, my)):
            if click[0] and solved==0:
                if but_pressed ==1:
                    assignments = backtracking.backtracking_search(ken)
                elif but_pressed==2:
                    assignments = backtracking.backtracking_search(ken, inference=backtracking.forward_checking)
                elif but_pressed==3:
                    assignments = backtracking.backtracking_search(ken, inference=backtracking.AC3)
                for assignment in assignments.keys():
                    i =0 
                    solved=1
                    for index in assignment:
                        myfont = pygame.font.SysFont('Comic Sans MS', 500//size)
                        value = myfont.render(str(assignments[assignment][i]), True, (0,0,0))
                        win_2.blit(value, ( ( (index[0]-1) *w )+470 +90//size , (((index[1]-1)*w )+(w//2) +size)) )
                        i+=1
                but_pressed=0
                
        if button_solve8.collidepoint((mx, my)):
            if click[0] :
                init_win()


        pygame.display.update()
        mainClock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    size =3
    cliques = puzzle_generation.generate(size) 
    init_win()

