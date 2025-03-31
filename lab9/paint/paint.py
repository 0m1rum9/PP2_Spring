import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 5
    mode = 'blue'
    points = []
    shape = ''
    start_pos = None
    end_pos = None
    rectangles = []  
    circles = []  
    rhombuses = [] 
    triangles = []  
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #just a quit
                return
            if event.type == pygame.KEYDOWN: #if any key is pressed
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                #if statements for getting the colors and the shapes
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_1:
                    shape = 'rectangle'
                elif event.key == pygame.K_2:
                    shape = 'circle'
                elif event.key == pygame.K_3: 
                    shape = 'rhombus'
                elif event.key == pygame.K_4:
                    shape = 'triangle'
                elif event.key == pygame.K_0:
                    shape = ''

            if event.type == pygame.MOUSEBUTTONDOWN: #if mousebutton is pushed
                if shape in ['rectangle', 'circle', 'rhombus', 'triangle'] and event.button == 1:
                    start_pos = event.pos
                    end_pos = event.pos

            if event.type == pygame.MOUSEMOTION: #if mouse drags
                if shape == '' and pygame.mouse.get_pressed()[0]:
                    points.append(event.pos)
                    points = points[-256:]  
                elif shape in ['rectangle', 'circle', 'rhombus', 'triangle'] and start_pos:
                    end_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP: #if the mousebutton releases
                if shape == 'rectangle' and start_pos and event.button == 1:
                    rectangles.append((start_pos, end_pos, mode))  
                elif shape == 'circle' and start_pos and event.button == 1:
                    circles.append((start_pos, end_pos, mode))  
                elif shape == 'rhombus' and start_pos and event.button == 1:
                    rhombuses.append((start_pos, end_pos, mode))
                elif shape == 'triangle' and start_pos and event.button == 1:
                    triangles.append((start_pos, end_pos, mode))
                start_pos = None
                end_pos = None
        
        screen.fill((0, 0, 0))
        
        for i in range(len(points) - 1): #for drawing points
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode) 
        
        for rect in rectangles: #for drawing rect's
            drawRectangle(screen, rect[0], rect[1], rect[2], temp=False)
        
        for circle in circles: # for drawing circles
            drawCircle(screen, circle[0], circle[1], circle[2])
            
        for rhombus in rhombuses: # for drawing rhombuses
            drawRhombus(screen, rhombus[0], rhombus[1], rhombus[2])
            
        for triangle in triangles: # for drawing triangles
            drawTriangle(screen, triangle[0], triangle[1], triangle[2])
        
        if shape == 'rectangle' and start_pos and end_pos: #for pre-draw the rectangle
            drawRectangle(screen, start_pos, end_pos, mode, temp=True)
        
        if shape == 'circle' and start_pos and end_pos: #for pre-draw the circle
            drawCircle(screen, start_pos, end_pos, mode, temp=True)
            
        if shape == 'rhombus' and start_pos and end_pos: #for pre-draw the rhombus
            drawRhombus(screen, start_pos, end_pos, mode, temp=True)
            
        if shape == 'triangle' and start_pos and end_pos: #for pre-draw the triangle
            drawTriangle(screen, start_pos, end_pos, mode, temp=True)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    color = {'blue': (c1, c1, c2), 'red': (c2, c1, c1), 'green': (c1, c2, c1)}.get(color_mode, (255, 255, 255))
    
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start, end, color_mode, temp=False):
    color = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}.get(color_mode, (255, 255, 255))
    
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), #getting min if the start pos is higher than end
                       abs(end[0] - start[0]    ), abs(end[1] - start[1])) #the same logic as above
    
    pygame.draw.rect(screen, (255, 255, 255) if temp else color, rect, 2) #drawing the rectangle

def drawCircle(screen, start, end, color_mode, temp=False):
    color = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}.get(color_mode, (255, 255, 255))
    
    radius = int(math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2))   #formula for radius in xy-plane
    pygame.draw.circle(screen, (255, 255, 255) if temp else color, start, radius, 2) #drawing the circle

def drawRhombus(screen, start, end, color_mode, temp=False):
    color = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}.get(color_mode, (255, 255, 255))
    
    # the center point
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    
    half_width = abs(end[0] - start[0]) // 2
    half_height = abs(end[1] - start[1]) // 2
    
    #the four points of the rhombus
    points = [
        (center_x, center_y - half_height),  # top
        (center_x + half_width, center_y),   # right
        (center_x, center_y + half_height),  # bottom
        (center_x - half_width, center_y)    # left
    ]
    
    # draw the rhombus
    pygame.draw.polygon(screen, (255, 255, 255) if temp else color, points, 2)

def drawTriangle(screen, start, end, color_mode, temp=False):
    color = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}.get(color_mode, (255, 255, 255))
    
    #width and height
    width = end[0] - start[0]
    height = end[1] - start[1]
    
    #three points of the triangle
    points = [
        (start[0], end[1]),                # bottom-left
        (start[0] + width // 2, start[1]), # top-middle
        (end[0], end[1])                   # bottom-right
    ]
    
    # draw the triangle
    pygame.draw.polygon(screen, (255, 255, 255) if temp else color, points, 2)

main()