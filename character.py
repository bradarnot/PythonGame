#Created by Bradley Arnot
import pygame
from position import Position
from door import Door
import math

class Character:
	
	#Initialize state
	def __init__(self, x, y):
		self.animationStage = 0
		self.direction = 0
		self.position = Position(x, y)
		self.speed = 5 
		self.animationSpeed = 1
		self.collider = pygame.Rect(x, y, 32, 32)
		self.spriteSheet = pygame.image.load("img/charactersheet.png")
		self.score = 0
		self.health = 100
		self.font = pygame.font.Font(None, 20)
		self.immobilize = False
		self.timer = 0

	#Iterate to next frame in character animation
	def iterateAnimation(self):
		if self.timer < 1:
			self.timer+=self.animationSpeed
		else:
			self.animationStage = (self.animationStage + 1) % 3
			self.timer = 0

	#Change direction character is facing
	def changeDirection(self, newDirection):
		self.direction = newDirection;
		self.animationStage = 0
	
	#Check for collisions with walls, if not, move at speed specified above
	def move(self, room):
		collision = False
		#If character is going to hit a wall in the direction he is moving, then move character to outerbound of the wall
		#print self
		for wall in room.walls:
			if self.direction == 0 and pygame.Rect(self.position.x, self.position.y + self.speed, 32, 32).colliderect(wall.rect()):
				self.position.y = wall.rect().top - 32
				collision = True
			if self.direction == 3 and pygame.Rect(self.position.x, self.position.y - self.speed, 32, 32).colliderect(wall.rect()):
				self.position.y = wall.rect().bottom
				collision = True
			if self.direction == 2 and pygame.Rect(self.position.x + self.speed, self.position.y, 32, 32).colliderect(wall.rect()):
				self.position.x = wall.rect().left - 32
				collision = True
			if self.direction == 1 and pygame.Rect(self.position.x - self.speed, self.position.y, 32, 32).colliderect(wall.rect()):
				self.position.x = wall.rect().right
				collision = True

		#If no collision, move normally
		if not collision:
			if self.direction == 0:
				self.position.y += self.speed
			elif self.direction == 1:
				self.position.x -= self.speed
			elif self.direction == 2:
				self.position.x += self.speed
			else:
				self.position.y -= self.speed
		self.collider = pygame.Rect(self.position.x, self.position.y, 32, 32)
		#If collision with a collectable item, increase score and remove the collectable from the room
		for collectable in room.collectables:
			if self.collider.colliderect(collectable.rect()):
				room.collectables.remove(collectable)
				self.score += 1

	#check if the character has hit a monster and should take damage
	#If he is damaged keep him immobilized for 100 frames
	def checkDamage(self, room):
		if self.immobilize and not self.isDead():
			self.timer += 1
			if self.timer >= 100:
				self.immobilize = False
		else:
			for monster in room.monsters:
				if monster.rect().colliderect(self.collider):
					self.health -= monster.damage
					self.immobilize = True
					self.timer = 0

	#Character is dead if health is less than or equal to 0
	def isDead(self):
		return self.health <= 0

	#Character is immobilized when dead
	def die(self):
		self.immobilize = True
		
	#check what keys have been pressed and change the direction of the characharacter if needed
	def update(self, event, room):
		if (not self.immobilize) and event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_s:
				if self.direction == 0:
					self.iterateAnimation()
				else:
					self.changeDirection(0)
				self.move(room)
			elif event.key == pygame.K_a:
				if self.direction == 1:
					self.iterateAnimation()
				else:
					self.changeDirection(1)
				self.move(room)
			elif event.key == pygame.K_d:
				if self.direction == 2:
					self.iterateAnimation()
				else:
					self.changeDirection(2)
				self.move(room)
			elif event.key == pygame.K_w:
				if self.direction == 3:
					self.iterateAnimation()
				else:
					self.changeDirection(3)
				self.move(room)
			
	#draw character, helth, and score
	def draw(self, screen, camera):
		screen.blit(self.font.render("Score: " + str(self.score), False, (0, 0, 0)), (50, camera.height - self.font.get_height()))
		if not self.immobilize:
			screen.blit(self.spriteSheet, (self.position.x - camera.position.x, self.position.y - camera.position.y), ((self.animationStage*32, self.direction*32), (32, 32)))
		else:
			screen.blit(self.spriteSheet, (self.position.x - camera.position.x, self.position.y - camera.position.y), ((0, 5*32), (32, 32)))
			if self.health > 0:
				health = pygame.Surface((int(float(self.health)/2.0), 10))
				health.fill((255, 0, 0))
				screen.blit(health, (self.position.x - camera.position.x, self.position.y - camera.position.y - 55))
			

	def __str__(self):
		return "Character " + str(self.position)
