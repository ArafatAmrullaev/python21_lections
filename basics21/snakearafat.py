import pygame
import sys
import random
pygame.init()

def game():
    size_block = 20
    colors = (147, 112, 219)
    color_rect = (230, 230, 250)
    color_rect2 = (216, 191, 216)
    size = [460, 510]
    count_blocks = 20
    color_snake = (218, 165, 32)
    margin = 1
    header_margin = 50
    color_food = (128, 0, 0)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Arafat_Snakeeeeee')
    timer = pygame.time.Clock()
    size = [size_block * count_blocks + 2 * size_block + margin * count_blocks, size_block * count_blocks + 2 * size_block + margin * count_blocks + header_margin]

    courier = pygame.font.SysFont('courier', 36)

    class SnakeBlock:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def is_inside(self):
            return 0<=self.x<size_block and 0<=self.y<size_block

        def __eq__(self, other):
            return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


    def random_block():
        x = random.randint(0, count_blocks-1)
        y = random.randint(0, count_blocks-1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, count_blocks-1)
            empty_block.y = random.randint(0, count_blocks-1)
        return empty_block

    def draw_block(color, row, column):
        pygame.draw.rect(screen, color, [size_block + column * size_block + margin * (column+1), header_margin + size_block + row * size_block + margin * (row +1), size_block, size_block])

    snake_blocks = [SnakeBlock(10, 9), SnakeBlock(10, 10), SnakeBlock(10, 11)]
    food = random_block()
    d_row = 0
    d_col = 1
    total = 0
    speed = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1


        screen.fill(colors)
        pygame.draw.rect(screen, header_margin, [0, 0, size[0], header_margin])
        text_total = courier.render(f'Total: {total}', 0, color_rect)
        text_speed = courier.render(f'Speed: {speed}', 0, color_rect)
        text_lost = courier.render('You Lose!(C or Q)', 0, color_rect)
        screen.blit(text_total, (size_block, size_block))
        screen.blit(text_speed, (size_block+230, size_block))


        for row in range(count_blocks):
            for column in range(count_blocks):
                if (row+column)%2 == 0:
                    color = color_rect2
                else:
                    color = color_rect
                
                draw_block(color, row, column)
        

        head = snake_blocks[-1]
        def losing():
            screen.fill(colors)
            screen.blit(text_lost, (size_block, size_block))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_c:
                        game()

        for x in snake_blocks[0:-1]:
            while x == head:
                losing()

        while not head.is_inside():
            losing()


        draw_block(color_food, food.x, food.y)

        for block in snake_blocks:
            draw_block(color_snake, block.x, block.y)

        if food == head:
            total += 1
            speed = total//5 + 1
            snake_blocks.append(food)
            food = random_block()
        
        
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)
        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        
    

        pygame.display.flip()
        timer.tick(6+speed)

game()