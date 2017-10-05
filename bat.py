#Created by Bradley Arnot
import pygame
from monster import Monster
from position import Position

class Bat(Monster):
	
	def __init__(self, x, y, nodeList=[]):
		#Call to parent class to set up state and nodeList and such
		Monster.__init__(self, x, y, nodeList)
		#Holds, monster image... different for every monster
		self.spriteSheet = pygame.image.load("img/monsters.png")
		#amount of damgae dealt if attack player
		self.damage = 25

	#Draws proper sprite in sprite sheet to screen
	def draw(self, screen, camera):
		screen.blit(self.spriteSheet, (self.position.x - camera.position.x, self.position.y - camera.position.y), (((self.animationStage * 32) + (self.direction * 96), 96), (32, 32)))

	def __str__(self):
		return "Bat: " + str(self.position) + " next node " + str(self.nodeList[self.nextIndex])
