#Created by Bradley Arnot
from __future__ import print_function
import random
import pygame
from pygame import Surface
from wall import Wall
from position import Position
from orb import Orb
from monster import Monster
from ghost import Ghost
from skeleton import Skeleton
from goblin import Goblin
from bat import Bat 
from button import Button
from door import Door

class Room:
	
	def __init__(self, x, y, width, height):
		self.position = Position(x, y)
		self.height = height
		self.width = width
		self.walls = []
		self.collectables = []
		self.monsters = []
		self.adjRooms = []
		self.buttons = []
		#Wall Thickess
		self.wT = 100
		self.surface = pygame.Surface((width, height))
		self.generateRoom()
		#self.tileSet = pygame.image.load("img/dungeon.jpg")
		
	#generates square room with walls on all sides
	def generateRoom(self):
		self.surface.fill((128, 128, 128))
		self.walls.append(Wall(self.position.x - self.wT, self.position.y - self.wT, self.wT, self.wT + self.height))
		self.walls.append(Wall(self.position.x - self.wT, self.position.y + self.height, self.wT + self.width, self.wT))
		self.walls.append(Wall(self.position.x + self.width, self.position.y, self.wT, self.wT + self.height))
		self.walls.append(Wall(self.position.x, self.position.y - self.wT, self.wT + self.width, self.wT))

	def addCollectable(self, x, y):
		self.collectables.append(Orb(self.position.x + x, self.position.y + y))

	#Add list of collectables to room
	def addCollectables(self, orbs):
		size = len(self.collectables)
		self.collectables = self.collectables + orbs
		for i in range(size, len(self.collectables)):
			self.collectables[i].position.x += self.position.x
			self.collectables[i].position.y += self.position.y

	#Adds a monster to the room
	#	typ denotes type of monster
	#	nodeList is an optional list of nodes for the movement of the monster that can be passed
	def addMonster(self, x, y, typ, nodeList=[]):
		if typ == 0:
			self.monsters.append(Ghost(x, y, nodeList))
		elif typ == 1:
			self.monsters.append(Skeleton(x, y, nodeList))
		elif typ == 2:
			self.monsters.append(Goblin(x, y, nodeList))
		elif typ == 3:
			self.monsters.append(Bat(x, y, nodeList))

	#Adds wall to room
	def addWall(self, x, y, width, height):
		self.walls.append(Wall(self.position.x + x, self.position.y + y, width, height))

	def addDoor(self, door):
		self.walls.append(door)

	def addButton(self, x, y, color, doors=[]):
		self.buttons.append(Button(self.position.x + x, self.position.y + y, color, doors))

	#For checking if position (x, y) are inside this room
	def collideRoom(self, x, y):
		return (x >= self.position.x and x <= self.position.x + self.width) and (y >= self.position.y and y <= self.position.y + self.height)

	#Purpose: to make level building easier
	#Adds a connecting room to the current room and deletes and splits walls accordingly
	def addConnection(self, room):
		self.adjRooms.append(room)
		room.adjRooms.append(self)
		#For holding the position of the two corners that the rooms collide at
		collisions = []
		#find collision points
		if self.collideRoom(room.position.x, room.position.y):
			collisions.append(Position(room.position.x, room.position.y))
		if self.collideRoom(room.position.x + room.width, room.position.y):
			collisions.append(Position(room.position.x + room.width, room.position.y))
		if self.collideRoom(room.position.x, room.position.y + room.height):
			collisions.append(Position(room.position.x, room.position.y + room.height))
		if self.collideRoom(room.position.x + room.width, room.position.y + room.height):
			collisions.append(Position(room.position.x + room.width, room.position.y + room.height))
		
		#If there are more or less collisions then the room placement is incorrect
		if len(collisions) != 2:
			print("ERROR: Adding " + str(room) + " connection to " + str(self) + ". " + str(len(collisions)) + " collisions with rooms.")

		#Sort collision points in ascending order
		if collisions[0].x > collisions[1].x or collisions[0].y > collisions[1].y:
			collisions[0].swap(collisions[1])

		#Delete the wall obstructing the connecting room
		#Create two new walls on either side of the junction
		for wall in self.walls:
			if wall.collideWall(collisions[0].x, collisions[0].y) and wall.collideWall(collisions[1].x, collisions[1].y):
				if wall.height == self.wT:
					self.walls.append(Wall(wall.position.x, wall.position.y, collisions[0].x - wall.position.x, self.wT))
					self.walls.append(Wall(collisions[1].x, wall.position.y, wall.width - (collisions[1].x - wall.position.x), self.wT))
				else:
					self.walls.append(Wall(wall.position.x, wall.position.y, self.wT, collisions[0].y - wall.position.y))
					self.walls.append(Wall(wall.position.x, collisions[1].y, self.wT, wall.height - (collisions[1].y - wall.position.y)))
				self.walls.remove(wall)
				break

		#Destroy the wall obstructing the junction on the connecting room
		for wall in room.walls:
			#print str(wall) + "\n" + str(wall.rect())
			if wall.collideWall(collisions[0].x, collisions[0].y) and wall.collideWall(collisions[1].x, collisions[1].y) and not isinstance(wall, Door):
				room.walls.remove(wall)

		#Trim the length of walls for clean connection
		for wall in room.walls:
			if pygame.Rect((self.position.x, self.position.y), (self.width, self.height)).colliderect(wall.rect()):
				#print "Collision between: " + str(self) + " and " + str(wall)
				if wall.height == self.wT:
					if wall.position.x < self.position.x + self.width and wall.position.x > self.position.x:
						wall.position.x += self.wT
					wall.width -= self.wT
				else:
					if wall.position.y < self.position.y + self.height and wall.position.y > self.position.y:
						wall.position.y += self.wT
					wall.height -= self.wT
	
		for wall in self.walls:
			if not isinstance(wall, Door):
				wall.updateImage()
		for wall in room.walls:
			if not isinstance(wall, Door):
				wall.updateImage()
		#print	

	#This draws the room background, walls, and everything that is inside of the room with exception to the player and princess
	def draw(self, screen, camera):
		screen.blit(self.surface, (self.position.x - camera.position.x, self.position.y - camera.position.y))
		for wall in self.walls:
			wall.draw(screen, camera)
		
		for button in self.buttons:
			button.draw(screen, camera)

		for collectable in self.collectables:
			collectable.draw(screen, camera)

		for monster in self.monsters:
			monster.move()
			monster.draw(screen, camera)

	def rect(self):
		return pygame.Rect((self.position.x, self.position.y), (self.width, self.height))

	#For printing purposes, creates an informational string based on the room
	def __str__(self):
		return "Room: (" + str(self.position.x) + ", " + str(self.position.y) + ") (" + str(self.position.x + self.width) + ", " + str(self.position.y + self.height) + ")"
