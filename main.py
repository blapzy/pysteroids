from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH
import pygame
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys

def main():
    #create screen, initalize clock
    print(f'Starting Asteroids with pygame version: {pygame.version.ver}')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #define groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    #instantiate player object
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    
    while True:
        log_state()

        #check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #draw screen
        screen.fill("black")
        updatable.update(dt)
        for ast in asteroids:
            if player.collides_with(ast):
                log_event("player_hit")
                print('Game over!')
                sys.exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        #end loop update clock
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
