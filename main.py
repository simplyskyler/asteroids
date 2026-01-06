import pygame, sys
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from player import Player
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, drawable, updatable)
	AsteroidField.containers = (updatable)
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	game = "on"
	while game == "on":
		log_state()
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill("black")
		for obj in updatable:
			if obj is player:
				player.reload -= dt
			obj.update(dt)
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					asteroid.split()
					shot.kill()
		for drw in drawable:
			drw.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	

if __name__ == "__main__":
    main()
