#Created by Bradley Arnot
import pygame
from position import Position
from room import Room
from character import Character
from camera import Camera
from orbGenerator import OrbGenerator
from princess import Princess
from door import Door
from button import Button
from menu import Menu

class Level:
	
	def __init__(self, size):
		#Stores all the rooms in the current level
		self.levelMap = []
		#Holds the current level start at 0, main menu
		self.level = 0
		self.MAX_LEVEL = 4
		#The background color below all the objects
		self.background = pygame.Surface((size[0], size[1]))
		self.background.fill((200, 200, 200))
		#Holds the size of the window passed in from the game
		self.screenSize = size
		#Has the player won?
		self.win = False
		self.drawn = False
		self.score = 0
		self.timer = 0
		self.MAX_TIMER = 200
		self.menu = Menu(self.screenSize)
		self.displayHowPlay = False
		self.pressed = False
		self.testButton = pygame.Surface((32, 32))
		self.testButton.fill((255, 0, 0))
		self.monsters = pygame.image.load("img/monsters.png")
		self.princessImage = pygame.image.load("img/people.png")
		self.font = pygame.font.Font(None, 30)
		self.fontLevel = pygame.font.Font(None, 20)
		self.fontTitle = pygame.font.Font(None, 40)

	#generates a new level based on the current level variable
	def generateLevel(self):
		self.timer = 0
		if self.level == 0:
			pygame.key.set_repeat(1, 200)
		elif self.level == 1:
			self.generateLevel1()
			pygame.key.set_repeat(1, 80)
		elif self.level == 2:
			self.generateLevel2()
			pygame.key.set_repeat(1, 80)
		elif self.level == 3:
			self.generateLevel3()
			pygame.key.set_repeat(1, 80)
		elif self.level == 4:
			self.generateLevel4()
			pygame.key.set_repeat(1, 40)
		else:
			#If the player has passed all the levels
			#Draw the screen that tells them they won
			self.level = 0
			pygame.key.set_repeat(1, 200)
			self.menu.win(self.score)
			self.score = 0

	def generateLevel1(self):
		#The total size of the level
		#This is used for the camera motion
		self.mapSize = Position(500, 800)

		#Create the camera object that holds the view the player sees
		self.camera = Camera(0, 0, self.screenSize[0], self.screenSize[1], self.mapSize)

		#Create the character for this room
		self.character = Character(100, 100)

		#Create the rooms for this level
		self.currentRoom = Room(100, 100, 300, 400)
		room2 = Room(150, 500, 100, 200)

		#Add door and linked button
		door = Door(150, 550, 100, 50)	
		room2.addDoor(door)
		self.currentRoom.addButton(200, 350, (255, 0, 0), [door])
	
		#Connect the rooms, this removes all walls in the junction 
		#between them
		self.currentRoom.addConnection(room2)
		
		#Add all the rooms to the level map
		self.levelMap.append(self.currentRoom)
		self.levelMap.append(room2)
	
		#Add the princess to the room	
		self.princess = Princess(175, 650)

	def generateLevel2(self):
		self.mapSize = Position(1200, 1100)

		self.camera = Camera(0, 0, self.screenSize[0], self.screenSize[1], self.mapSize)

		orbGen = OrbGenerator()

		self.currentRoom = Room(150, 150, 300, 300)
		room2 = Room(300, 450, 100, 400)
		room3 = Room(400, 750, 500, 100)
		room4 = Room(900, 350, 100, 600)
		room5 = Room(800, 150, 200, 200)

		room2.addCollectables(orbGen.generateRect(45, 50, 1, 8))
		room3.addCollectables(orbGen.generateRect(10, 45, 15, 1))
		room4.addCollectables(orbGen.generateRect(45, 300, 1, 5))

		princessDoor = Door(900, 400, 100, 50)
		room4.addButton(34, 550, (255, 0, 0), [princessDoor])
		buttonDoor = Door(900, 850, 100, 30)
		room4.addButton(34, 200, (0, 255, 0), [buttonDoor])
		room4.addDoor(princessDoor)
		room4.addDoor(buttonDoor)

		self.currentRoom.addConnection(room2)
		room2.addConnection(room3)
		room4.addConnection(room3)
		room5.addConnection(room4)

		self.levelMap.append(self.currentRoom)
		self.levelMap.append(room2)
		self.levelMap.append(room3)
		self.levelMap.append(room4)
		self.levelMap.append(room5)

		#Adds the monster and the different nodes that he walks to
		self.currentRoom.addMonster(155, 400, 0, [Position(155, 300), Position(400, 300), Position(400, 400)])

		self.character = Character(175, 175)

		self.princess = Princess(850, 200)

	def generateLevel3(self):
		self.mapSize = Position(900, 1100)

		self.camera = Camera(0, 0, self.screenSize[0], self.screenSize[1], self.mapSize)

		orbGenerator = OrbGenerator()

		self.currentRoom = Room(300, 200, 500, 800)
		room2 = Room(100, 750, 200, 150)
		room3 = Room(500, 0, 150, 200)

		self.currentRoom.addCollectables(orbGenerator.generateRect(50, 50, 12, 1))
		self.currentRoom.addCollectables(orbGenerator.generateRect(45, 450, 1, 10))

		self.currentRoom.addWall(0, 200, 350, 200)
		self.currentRoom.addWall(150, 500, 350, 200)

		room2Door = Door(250, 750, 50, 150)
		princessDoor = Door(500, 100, 150, 50)
		self.currentRoom.addButton(400, 750, (0, 0, 255), [room2Door])
		room2.addButton(50, 50, (255, 0, 0), [princessDoor])
		room2.addDoor(room2Door)
		room3.addDoor(princessDoor)

		self.currentRoom.addMonster(300, 334, 1, [Position(668, 334), Position(668, 630), Position(300 , 630), Position(668, 630), Position(668, 334)])
		self.currentRoom.addMonster(768, 640, 2, [Position(400, 640), Position(400, 940), Position(768 , 940), Position(400, 940), Position(400, 640)])
		room2.addMonster(100, 750, 3, [Position(100, 868), Position(218, 868), Position(218, 750)])
		self.currentRoom.addMonster(300, 600, 3, [Position(400, 600), Position(400, 950), Position(300, 950)])

		self.currentRoom.addConnection(room2)
		self.currentRoom.addConnection(room3)

		self.levelMap.append(self.currentRoom)
		self.levelMap.append(room2)
		self.levelMap.append(room3)

		self.character = Character(300, 200)
		self.princess = Princess(566, 50)
	
	def generateLevel4(self) :
		self.mapSize = Position(800, 1000)
		self.camera = Camera(0, 0, self.screenSize[0], self.screenSize[1], self.mapSize)
		orbGenerator = OrbGenerator()

		room1 = Room(100, 300, 650, 650)
		room2 = Room(350, 0, 150, 300)

		room1.addCollectables(orbGenerator.generateRect(320, 10, 1, 10))
		room1.addCollectables(orbGenerator.generateRect(320, 360, 1, 10))
		room1.addCollectables(orbGenerator.generateRect(10, 320, 10, 1))
		room1.addCollectables(orbGenerator.generateRect(360, 320, 10, 1))

		door1 = Door(room2.position.x, room2.position.y+room2.height-100, room2.width, 50)
		door2 = Door(room2.position.x, room2.position.y+room2.height-150, room2.width, 50)
		room1.addButton(10, (room1.height/2) - 16, (255, 0, 0), [door1])
		room1.addButton(room1.width - 42, room1.height/2 - 16, (0, 0, 255), [door2])
		room2.addDoor(door1)
		room2.addDoor(door2)

		#Bats
		room1.addMonster(room1.position.x, room1.position.y, 3, [Position(room1.position.x, room1.position.y + room1.height - 32), Position(room1.position.x + room1.width - 32, room1.position.y + room1.height - 32), Position(room1.position.x + room1.width - 32, room1.position.y)])
		room1.addMonster(room1.position.x, room1.position.y + room1.height - 32, 3, [Position(room1.position.x + room1.width - 32, room1.position.y + room1.height - 32), Position(room1.position.x + room1.width - 32, room1.position.y), Position(room1.position.x, room1.position.y)])
		room1.addMonster(room1.position.x + room1.width - 32, room1.position.y + room1.height - 32, 3, [Position(room1.position.x + room1.width - 32, room1.position.y), Position(room1.position.x, room1.position.y), Position(room1.position.x, room1.position.y + room1.height - 32)])
		room1.addMonster(room1.position.x + room1.width - 32, room1.position.y, 3, [Position(room1.position.x, room1.position.y), Position(room1.position.x, room1.position.y + room1.height - 32), Position(room1.position.x + room1.width - 32, room1.position.y + room1.width - 32)])

		#Goblins
		room1.addMonster(room1.position.x + 64, room1.position.y + 64, 2, [Position(room1.position.x + 64, room1.position.y + room1.height - 96), Position(room1.position.x + room1.width - 96, room1.position.y + room1.height - 96), Position(room1.position.x + room1.width - 96, room1.position.y + 64)])
		room1.addMonster(room1.position.x + 64, room1.position.y + room1.height - 96, 2, [Position(room1.position.x + room1.width - 96, room1.position.y + room1.height - 96), Position(room1.position.x + room1.width - 96, room1.position.y + 64), Position(room1.position.x + 64, room1.position.y + 64)])
		room1.addMonster(room1.position.x + room1.width - 96, room1.position.y + room1.height - 96, 2, [Position(room1.position.x + room1.width - 96, room1.position.y + 64), Position(room1.position.x + 64, room1.position.y + 64), Position(room1.position.x + 64, room1.position.y + room1.height - 96)])
		room1.addMonster(room1.position.x + room1.width - 96, room1.position.y + 64, 2, [Position(room1.position.x + 64, room1.position.y + 64), Position(room1.position.x + 64, room1.position.y + room1.height - 96), Position(room1.position.x + room1.width - 96, room1.position.y + room1.height - 96)])
		
		#Skeletons
		room1.addMonster(room1.position.x + 148, room1.position.y + 148, 1, [Position(room1.position.x + 148, room1.position.y + room1.height - 180), Position(room1.position.x + room1.width - 180, room1.position.y + room1.height - 180), Position(room1.position.x + room1.width - 180, room1.position.y + 148)])
		room1.addMonster(room1.position.x + 148, room1.position.y + room1.height - 180, 1, [Position(room1.position.x + room1.width - 180, room1.position.y + room1.height - 180), Position(room1.position.x + room1.width - 180, room1.position.y + 148), Position(room1.position.x + 148, room1.position.y + 148)])
		room1.addMonster(room1.position.x + room1.width - 180, room1.position.y + room1.height - 180, 1, [Position(room1.position.x + room1.width - 180, room1.position.y + 148), Position(room1.position.x + 148, room1.position.y + 148), Position(room1.position.x + 148, room1.position.y + room1.height - 180)])
		room1.addMonster(room1.position.x + room1.width - 180, room1.position.y + 148, 1, [Position(room1.position.x + 148, room1.position.y + 148), Position(room1.position.x + 148, room1.position.y + room1.height - 180), Position(room1.position.x + room1.width - 180, room1.position.y + room1.height - 180)])
		
		#Ghosts
		room1.addMonster(room1.position.x + 212, room1.position.y + 212, 0, [Position(room1.position.x + 212, room1.position.y + room1.height - 244), Position(room1.position.x + room1.width - 244, room1.position.y + room1.height - 244), Position(room1.position.x + room1.width - 244, room1.position.y + 212)])
		room1.addMonster(room1.position.x + 212, room1.position.y + room1.width - 244, 0, [Position(room1.position.x + room1.width - 244, room1.position.y + room1.height - 244), Position(room1.position.x + room1.width - 244, room1.position.y + 212), Position(room1.position.x + 212, room1.position.y + 212)])
		room1.addMonster(room1.position.x + room1.width - 244, room1.position.y + room1.width - 244, 0, [Position(room1.position.x + room1.width - 244, room1.position.y + 212), Position(room1.position.x + 212, room1.position.y + 212), Position(room1.position.x + 212, room1.position.y + room1.height - 244)])
		room1.addMonster(room1.position.x + room1.width - 244, room1.position.y + 212, 0, [Position(room1.position.x + 212, room1.position.y + 212), Position(room1.position.x + 212, room1.position.y + room1.height - 244), Position(room1.position.x + room1.width - 244, room1.position.y + room1.height - 244)])

		room1.addConnection(room2)
		self.currentRoom = room1
		self.levelMap.append(room1)
		self.levelMap.append(room2)

		self.character = Character(room1.position.x + room1.width/2 - 16, room1.position.y + room1.height/2 - 16)
		self.princess = Princess(room2.position.x + (room2.width/2) -16, room2.position.y + 50)


	'''
	def generateLevel4(self):
		self.mapSize = Position(1050, 1200)

		self.camera = Camera(0, 0, self.screenSize[0], self.screenSize[1], self.mapSize)

		self.currentRoom = Room(500, 100, 150, 450)
		roomLeft = Room(100, 400, 400, 150)
		roomRight = Room(650, 400, 400, 150)

		prinDoor1 = Door(500, 375, 150, 25)
		prinDoor2 = Door(500, 300, 150, 25)
		roomLeft.addButton(50, 59, (255, 0, 0), [prinDoor1])
		roomRight.addButton(318, 59, (0, 0, 255), [prinDoor2])
		self.currentRoom.addDoor(prinDoor1)
		self.currentRoom.addDoor(prinDoor2)

		#Left room
		#
		junc1 = Room(400, 300, 50, 100)
		junc2 = Room(250, 250, 200, 50)
		junc3 = Room(250, 300, 50, 100)
		roomLeft.addConnection(junc1)
		roomLeft.addConnection(junc3)
		junc2.addConnection(junc1)
		junc2.addConnection(junc3)
		door1 = Door(450, 400, 25, 150, False)
		door2 = Door(350, 400, 25, 150)
		door3 = Door(225, 400, 25, 150, False)
		doorSide = Door(350, 250, 20, 50)
		roomLeft.addButton(284, 59, (250, 102, 0), [door1, door2, door3])
		roomLeft.addButton(184, 59, (0, 255, 0), [doorSide])
		roomLeft.addDoor(door1)
		roomLeft.addDoor(door2)
		roomLeft.addDoor(door3)
		junc2.addDoor(doorSide)
		#

		self.currentRoom.addConnection(roomLeft)
		self.currentRoom.addConnection(roomRight)
				
		self.levelMap.append(self.currentRoom)
		self.levelMap.append(roomLeft)
		self.levelMap.append(roomRight)
		#
		self.levelMap.append(junc1)
		self.levelMap.append(junc2)
		self.levelMap.append(junc3)
		#

		self.character = Character(559, 459)
		self.princess = Princess(559, 159)
	'''

	#Updates all objects that could change based on user input
	def update(self, event):
		#Makes sure after the display how to play menu key is pressed
		#it does not repeat until the user unpresses the key
		if self.level != 0 and not self.pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_h:
			self.displayHowPlay = not self.displayHowPlay
			self.pressed = True

		#If user presses the 'h' key, display the how to play overlay
		if event.type == pygame.KEYUP and event.key == pygame.K_h:
			self.pressed = False

		#if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.displayHowPlay and self.level == 0:
		#	self.displayHowPlay = False
		if self.level == 0:
			if not self.displayHowPlay:
				choice = self.menu.update(event)
				if choice == "Play Game!":
					self.level += 1
					self.destroyLevel()
					self.generateLevel()
				elif choice == "How to Play":
					self.displayHowPlay = True;
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
				self.displayHowPlay = False;


		if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
			self.level = 0
			self.win = False
			self.destroyLevel()
			self.generateLevel()

		#if self.timer < self.MAX_TIMER and self.level <= self.MAX_LEVEL:
		#	return

		#Exit the function if the player has won
		if self.displayHowPlay or self.level == 0:
			return

		#Update the positions for the camera and character for this event
		self.character.update(event, self.currentRoom)
		self.camera.update(self.character)

		#Check to see if any buttons have been pressed
		for button in self.currentRoom.buttons:
			button.checkButton(self.character.collider)


		#Check all the rooms in the map to see which one the character is in
		for room in self.levelMap:
			if room.collideRoom(self.character.position.x + 16, self.character.position.y + 16):
				self.currentRoom = room
				break


		#If the player wins the level i.e. finds the princess
		#Then increase the level var, destroy the current level,
		#and generate the next level
		if self.princess.checkWin(self.character):
			self.level += 1
			self.score += self.character.score
			self.destroyLevel()
			self.generateLevel()

		#If character is dead, show the dead screen
		if self.character.isDead():
			self.character.die()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
				self.destroyLevel()
				self.generateLevel()

	def drawHowPlay(self, screen):
			screen.blit(self.fontTitle.render("How to Play:", False, (0, 0, 0)), (self.screenSize[0]/2 - 75, 20))
			screen.blit(self.font.render("Movement", False, (0, 0, 0)), (self.screenSize[0]/4, 60))
			screen.blit(self.font.render("Up -- w", False, (0, 0, 0)), (self.screenSize[0]/4 + 50, 60 + (self.font.get_height())))
			screen.blit(self.font.render("Down -- s", False, (0, 0, 0)), (self.screenSize[0]/4 + 50, 60 + (2*self.font.get_height())))
			screen.blit(self.font.render("Right -- d", False, (0, 0, 0)), (self.screenSize[0]/4 + 50, 60 + (3*self.font.get_height())))
			screen.blit(self.font.render("Left -- a", False, (0, 0, 0)), (self.screenSize[0]/4 + 50, 60 + (4*self.font.get_height())))

			screen.blit(self.testButton, (self.screenSize[0]/4, 200))
			screen.blit(self.font.render("This is a button, press it to", False, (0, 0, 0)), (self.screenSize[0]/4 + 50, 200))
			screen.blit(self.font.render("open doors of the same color", False, (0, 0, 0)), (self.screenSize[0]/4 + 50, 200 + self.font.get_height()))

			screen.blit(self.monsters, (self.screenSize[0]/4, 260), ((0, 0), (32, 32)))
			screen.blit(self.monsters, (self.screenSize[0]/4+32, 260), ((0,32), (32, 32)))
			screen.blit(self.monsters, (self.screenSize[0]/4, 292), ((0, 64), (32, 32)))
			screen.blit(self.monsters, (self.screenSize[0]/4+32, 292), ((0, 96), (32, 32)))
			screen.blit(self.font.render("These are monsters, touch", False, (0, 0, 0)), (self.screenSize[0]/4 + 70, 260))
			screen.blit(self.font.render("them and they will hurt you", False, (0, 0, 0)), (self.screenSize[0]/4 + 70, 260 + self.font.get_height()))

			screen.blit(self.princessImage, (self.screenSize[0]/4, 370), ((128, 128), (32, 32)))
			screen.blit(self.fontTitle.render("Goal:", False, (0, 0, 0)), (self.screenSize[0]/2, 340))
			screen.blit(self.font.render("Find the princess", False, (0, 0, 0)), (self.screenSize[0]/4 + 50, 370))

	#Draws everything to the screen
	def draw(self, screen):
		#Exit the function if the player has won
		if(self.displayHowPlay):
			#Display controls on how to play over game
			if self.level == 0:
				screen.blit(self.background, (0, 0))
			self.drawHowPlay(screen)
		elif self.level == 0:
			self.menu.draw(screen)
		elif self.timer < self.MAX_TIMER and self.level <= self.MAX_LEVEL:
			self.timer += 1
			screen.blit(self.background, (0, 0))
			screen.blit(self.fontTitle.render("Level " + str(self.level), False, (0, 0, 0)), (self.screenSize[0]/2 - 75, 50))
		else:
			#Check if the character has been damaged
			self.character.checkDamage(self.currentRoom)

			#Draw the level background first
			screen.blit(self.background, (0, 0))

			#draw only the rooms that can be seen by the camera
			for room in self.levelMap:
				if room.rect().colliderect(self.camera.rect()):
					room.draw(screen, self.camera)

			#draw princess and character last so that they appear on top
			self.princess.draw(screen, self.camera)
			self.character.draw(screen, self.camera)

			if 0 < self.level <= self.MAX_LEVEL:
				screen.blit(self.fontLevel.render("Level: " + str(self.level), False, (0, 0, 0)), (150, self.screenSize[1] - self.font.get_height() + 8))

			#draw the character is dead screen if he is dead
			if self.character.isDead():
				screen.blit(self.font.render("You're Dead", False, (0, 0, 0)), (self.screenSize[0]/2 - 100, self.screenSize[1]/2 - self.font.get_height()-5))
				screen.blit(self.font.render("Press r to restart the level", False, (0, 0, 0)), (self.screenSize[0]/2 - 100, self.screenSize[1]/2))
				screen.blit(self.font.render("Press q to quit", False, (0, 0, 0)), (self.screenSize[0]/2 - 100, self.screenSize[1]/2 + self.font.get_height()+5))
				screen.blit(self.font.render("Press m to go to the menu", False, (0, 0, 0)), (self.screenSize[0]/2 - 100, self.screenSize[1]/2 + 2*self.font.get_height()+5))

	'''
	def drawWinScreen(self, screen):
		if not self.drawn:
			background = pygame.Surface((self.screenSize[0], self.screenSize[1]))
			background.fill((200, 200, 200))
			characterSprite = pygame.image.load("img/charactersheet.png")
			princessSprite = pygame.image.load("img/people.png")
			
			screen.blit(background, (0, 0))
			screen.blit(self.font.render("You Win!!!", False, (0, 0, 0)), (self.screenSize[0]/2 - 40, self.screenSize[1]/2 - self.font.get_height() - 5))
			screen.blit(self.font.render("Your score is " + str(self.score), False, (0, 0, 0)), (self.screenSize[0]/2 - 40, self.screenSize[1]/2))
			screen.blit(self.font.render("Press q to quit", False, (0, 0, 0)), (self.screenSize[0]/2 - 50, self.screenSize[1]/2 + self.font.get_height() + 5))
			screen.blit(characterSprite, (self.screenSize[0]/2 - 20, self.screenSize[1]/2 + 100), ((32, 64), (32, 32)))
			screen.blit(princessSprite, (self.screenSize[0]/2 + 20, self.screenSize[1]/2 + 100), ((128, 160), (32, 32)))
			self.drawn = True
	'''

	def destroyLevel(self):
		#Delete all the rooms in the map
		del self.levelMap[:]
