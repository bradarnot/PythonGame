#Created by Bradley Arnot

import pygame
from level import Level

def main():
	pygame.init()

	#size of game window
	size=[500,500]
	screen=pygame.display.set_mode(size)

	done = False
	#Level object controls the level you are on and all gameplay including
	#Drawing everything to the screen and updating positions
	level = Level(size)
	#Generate the first level
	level.generateLevel()
	clock = pygame.time.Clock()
	#Allows key input to repeat every 80ms
	pygame.key.set_repeat(1, 200)
	font = pygame.font.Font(None, 20)
	while not done:
		for event in pygame.event.get():
			#If the screen is closed or the user hits the 'q' key
			#The game is stopped
			if event.type == pygame.QUIT: 
				done = True
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
				done = True
			#The event is passed to the level object to update
			#All objects in the game
			level.update(event)
		#Draws all the objects in the game to the screen
		level.draw(screen)
		#Flip the buffer to the actual window
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

main()
