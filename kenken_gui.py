from inspect import trace
import pygame
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

def draw(cliques, size):    
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("kenken")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 42)
    x =0 
    w=((WIDTH-100)//size)
    for clique in cliques:
        index ,op, target = clique
        color = colors[randint(0, len(colors)-1)]
        colors.remove(color) 
        for i in index:
            shape_surf = pygame.Surface(pygame.Rect(((50+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w )).size,pygame.SRCALPHA )
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
            shape_surf.set_alpha(100)
            win.blit(shape_surf,((50+w*(i[0]-1)) , (50+w*(i[1]-1)) ,w, w) )
        value = myfont.render(str(target), True, (0,0,0))
        win.blit(value, (( (index[0][0]-1) *w )+55 ,((index[0][1]-1)*w )+55 ))
        if op != '.':
            value = myfont.render(op, True, (0,0,0))
            win.blit(value, (( (index[0][0]-1) *w )+ 60+15*len(str(target)) ,((index[0][1]-1)*w )+55 ))
        
    for i in range(size+1):
        pygame.draw.line(win, (0,0,0), (50 +w*i, 50), (50 + w*i ,950 ), 2 )
        pygame.draw.line(win, (0,0,0), (50, 50 + w*i), (950, 50 + w*i), 2 )
    pygame.display.update()
    
    return win

# def draw_solution(window, assignment):



size =3
if __name__ == "__main__":
    cliques = puzzle_generation.generate(size) 

    ken = puzzle_generation.Kenken(size, cliques)

    # print(cliques)

    assignment = backtracking.backtracking_search(ken, inference=backtracking.forward_checking)

    print (assignment)

    ken.display(assignment) 

    window = draw(cliques, size)

