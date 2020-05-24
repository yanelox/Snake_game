import pygame
import snake
import random
import prize_object
import Game_Parameters


class Environment:
    def __init__(self):
        # Creating snake
        self.snakes = [snake.SnakeElement(Game_Parameters.white), snake.SnakeElement(Game_Parameters.white)]
        self.snakes[1].set_snake_element_x(self.snakes[1].get_snake_element_x() + 20)

        # Creating prize
        self.prize = prize_object.Prize()

        # Score field
        self.score = 0

        # Last coordinates
        self.last_x = self.snakes[1].get_snake_element_x()
        self.last_y = self.snakes[1].get_snake_element_y()

        # Game init
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((Game_Parameters.width, Game_Parameters.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.game_running = True

        # Create sprite group and adding prize and snake to this group
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(i for i in self.snakes)
        self.all_sprites.add(self.prize)

    def crash(self):
        k = 0

        for i in range(1, len(self.snakes)):
            if self.snakes[i].get_snake_element_x() == self.snakes[0].get_snake_element_x() \
                    and \
                    self.snakes[i].get_snake_element_y() == self.snakes[0].get_snake_element_y():
                k += 1
                break

        if self.snakes[0].get_snake_element_x() < 0\
                or self.snakes[0].get_snake_element_x() > Game_Parameters.width\
                or self.snakes[0].get_snake_element_y() < 0\
                or self.snakes[0].get_snake_element_y() > Game_Parameters.height:
            k += 1

        if k > 0:
            return True
        else:
            return False

    def eat_prize(self):

        if self.snakes[0].get_snake_element_x() == self.prize.get_prize_x() and \
                self.snakes[0].get_snake_element_y() == self.prize.get_prize_y():

            cord_equality = True

            while cord_equality:
                k = 0
                for i in self.snakes:
                    if i.get_snake_element_x() == self.prize.get_prize_x()\
                            and\
                            i.get_snake_element_y() == self.prize.get_prize_y():
                        k += 1

                if k > 0:
                    self.prize.set_prize_x(random.randint(10, Game_Parameters.width - 10) // 2 // 10 * 2 * 10 + 10)
                    self.prize.set_prize_y(random.randint(10, Game_Parameters.height - 10) // 2 // 10 * 2 * 10 + 10)
                else:
                    cord_equality = False

            self.score += 1

            return True
        else:
            return False

    def upgrade(self):

        self.snakes.append(snake.SnakeElement(Game_Parameters.white))
        self.snakes[len(self.snakes) - 1].set_snake_element_x(self.last_x)
        self.snakes[len(self.snakes) - 1].set_snake_element_y(self.last_y)
        self.all_sprites.add(self.snakes[len(self.snakes) - 1])

    def start_game(self):
        # Game cycle
        while self.game_running:

            # Time control
            self.clock.tick(Game_Parameters.fps)

            # Checking for events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.game_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake.orientation != 'right':
                        snake.orientation = 'left'
                        break
                    elif event.key == pygame.K_UP and snake.orientation != 'down':
                        snake.orientation = 'up'
                        break
                    elif event.key == pygame.K_DOWN and snake.orientation != 'up':
                        snake.orientation = 'down'
                        break
                    elif event.key == pygame.K_RIGHT and snake.orientation != 'left':
                        snake.orientation = 'right'
                        break

            snake.move(self.snakes)

            if self.crash():
                self.game_running = False

            self.last_x = self.snakes[len(self.snakes)-1].get_snake_element_x()
            self.last_y = self.snakes[len(self.snakes)-1].get_snake_element_y()

            if self.eat_prize():
                self.upgrade()

            # Update
            self.all_sprites.update()

            # Render
            self.screen.fill(Game_Parameters.black)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
        print(self.score)
    pygame.quit()
