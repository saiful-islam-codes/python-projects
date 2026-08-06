import pygame
import sys
import random
pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("SNAKE Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 35)


def spawn_food(snake):
    while True:
        food_x = random.randint(0, 34) * 20
        food_y = random.randint(0, 34) * 20
        if [food_x, food_y] not in snake:   
            return [food_x, food_y]


snake_color = (0, 255, 0)
food_color = (255, 0, 0)
score = 0


def reset_game():
    global snake, x_change, y_change, game_over, food, score
    snake = [[300, 300], [280, 300], [260, 300]]
    x_change = 20
    y_change = 0
    game_over = False
    food = spawn_food(snake)
    score = 0


reset_game()

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    reset_game()
            else:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -20
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = 20
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -20
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = 20

    if not game_over:
        new_head = [snake[0][0] + x_change, snake[0][1] + y_change]
        snake.insert(0, new_head)

        if snake[0][0] == food[0] and snake[0][1] == food[1]:
            score += 10
            food = spawn_food(snake)
        else:
            snake.pop()

        head_x = snake[0][0]
        head_y = snake[0][1]

        if head_x < 0 or head_x >= 700 or head_y < 0 or head_y >= 700:
            game_over = True

        if snake[0] in snake[1:]:
            game_over = True

    screen.fill((0, 0, 0))
    for block in snake:
        pygame.draw.rect(screen, snake_color, (block[0], block[1], 20, 20))

    pygame.draw.rect(screen, food_color, (food[0], food[1], 20, 20))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    if game_over:
        text_surface = font.render("GAME OVER! PRESS 'R' to Retry", True, (255, 50, 50))
        screen.blit(text_surface, (150, 320))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()












# import pygame
# import sys
# import random
# pygame.init()

# screen = pygame.display.set_mode((700 ,700))
# pygame.display.set_caption("SNAKE Game")

# clock = pygame.time.Clock()

# font = pygame.font.SysFont("Arial", 35)
# def spawn_food():
#     food_x = random.randint(0, 34) * 20
#     food_y = random.randint(0, 34) * 20
#     return [food_x, food_y]

# snake = [[300 , 300] , [280 , 300] , [260 , 300]]
# snake_color = (0 , 255 , 0)
# x_change = 20 
# y_change = 0
# game_over = False
# food = spawn_food() 
# food_color = (255, 0, 0)
# score = 0
# def reset_game():
#     global snake, x_change, y_change, game_over
#     snake = [[300, 300], [280, 300], [260, 300]] 
#     x_change = 20  
#     y_change = 0   
#     game_over = False

# reset_game()
# snake_color = (0, 255, 0)

# Running = True
# while Running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: 
#            Running = False
#         if event.type == pygame.KEYDOWN:
#             if game_over:
#                 if event.key == pygame.K_r:
#                     reset_game()
#             else:        
#                 if event.key == pygame.K_LEFT and x_change == 0: 
#                     x_change = -20
#                     y_change = 0
#                 elif event.key == pygame.K_RIGHT and x_change == 0:
#                     x_change = 20
#                     y_change = 0
#                 elif event.key == pygame.K_UP and y_change == 0:
#                     x_change = 0
#                     y_change = -20 
#                 elif event.key == pygame.K_DOWN and y_change == 0:
#                     x_change = 0
#                     y_change = 20           
#     if not game_over:
#         new_head = [snake[0][0] + x_change, snake[0][1] + y_change]
#         snake.insert(0, new_head)  
#         snake.pop() 
#         new_head = [snake[0][0] + x_change, snake[0][1] + y_change]
#         snake.insert(0, new_head)
#         snake.pop()
        
#         if snake[0][0] == food[0] and snake[0][1] == food[1]:
#             score += 10        
#             food = spawn_food() 
#         else:
#             snake.pop()
#         head_x = snake[0][0]
#         head_y = snake[0][1]    
        
#         if head_x < 0 or head_x >= 700 or head_y < 0 or head_y >= 700:
#             game_over = True
#     screen.fill((0 , 0 , 0))
#     for block in snake:
#         pygame.draw.rect(screen , snake_color , (block[0] , block[1] , 20 , 20))
    
#     pygame.draw.rect(screen, food_color, (food[0], food[1], 20, 20))
    
#     score_text = font.render(f"Score: {score}", True, (255, 255, 255))
#     screen.blit(score_text, (20, 20))
#     if game_over:
#         text_surface = font.render("GAME OVER! PRESS'R' to Retry", True, (255, 50,50))
#         screen.blit(text_surface, (150, 320))
        
#     pygame.display.flip()
#     clock.tick(10)

# pygame.quit()
# sys.exit()
           