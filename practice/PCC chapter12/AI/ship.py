import pygame

class Ship():
    # initialize the spaceship
    def __init__(self,screen):

        # load the spaceship image
        self.screen = screen


        self.image = pygame.image.load('images/ai.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put new spaceship in the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)
