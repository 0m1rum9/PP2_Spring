import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ballin'")

ball_color = (255, 0, 0)  
ball_x = screen_width // 2  
ball_y = screen_height // 2 
ball_radius = 25
move_distance = 5
FPS = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_radius, ball_x - move_distance)
    elif keys[pygame.K_RIGHT]:
        ball_x = min(screen_width - ball_radius, ball_x + move_distance)
    elif keys[pygame.K_UP]:
        ball_y = max(ball_radius, ball_y - move_distance)  
    elif keys[pygame.K_DOWN]:
        ball_y = min(screen_height - ball_radius, ball_y + move_distance) 

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    FPS.tick(60)
    pygame.display.flip()

pygame.quit()
