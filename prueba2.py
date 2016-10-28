import pygame
import sys


WIDTH = 864#940
HEIGHT = 540

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('images/pika1.png'))
        self.images.append(load_image('images/pika2.png'))
        self.images.append(load_image('images/pika3.png'))
        self.images.append(load_image('images/pika4.png'))

        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)
        self.speed = [0.5, -0.5]

    def update(self, time):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
   
    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

def load_image(name):
    image = pygame.image.load(name)
    return image


def main():
    pygame.init()
    screen = pygame.display.set_mode((250, 250))
    clock = pygame.time.Clock()
    time = clock.tick(10)

    my_sprite = TestSprite()
    my_sprite.actualizar(time)
    my_group = pygame.sprite.Group(my_sprite)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all 
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        #my_group.update(time)
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
