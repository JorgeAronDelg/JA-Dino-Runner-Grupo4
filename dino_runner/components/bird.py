from pygame.sprite import Sprite
from utils.constants import BIRD

class Bird(Sprite):
    X_POS = 1100
    Y_POS = 280
    

    def __init__(self):
        self.image = BIRD[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_step = 0
        self.dino_run = True

    def update(self):
        #Pajaro correr
        self.run()

        if self.dino_step >= 10:
            self.dino_step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        self.X_POS-=10
        return self.X_POS
        

    def run(self):
        self.image = BIRD[0] if self.dino_step < 5 else BIRD[1] 
        print(self.dino_step)
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_step += 1