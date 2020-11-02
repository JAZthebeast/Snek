#Import Modules
import pygame
import random
#Initialize Pygame & Window
pygame.init()
display = pygame.display.set_mode((410, 460))
pygame.display.update()
pygame.display.set_caption("Snek")
#Define Variables
clock = pygame.time.Clock()
game_over = False
x = 85
y = 215
body = [(x, y), (x - 20, y), (x - 40, y)]
x_change = 20
y_change = 0
apple_x = random.randrange(15, 395, 20)
apple_y = random.randrange(65, 440, 20)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
length = 3
score = 0
#Load Assets
font = pygame.font.Font("Assets/atari-classic-font/AtariClassicExtrasmooth-LxZy.ttf", 25)
scoreFont = pygame.font.Font("Assets/atari-classic-font/AtariClassicExtrasmooth-LxZy.ttf", 20)
#Game Loop
while True:
	#Set Game Speed
	clock.tick(15)
	#Score Board
	text = scoreFont.render("Score:", False, white, black)
	scoreText = scoreFont.render(str(score), True, red, black)
	name = font.render("SNEK!", True, white, black)
	textRect = text.get_rect()
	scoreTextRect = scoreText.get_rect()
	nameRect = name.get_rect()
	textRect = (225, 17)
	scoreTextRect = (350, 17)
	nameRect = (40, 15)
	display.blit(text, textRect)
	display.blit(scoreText, scoreTextRect)
	display.blit(name, nameRect)
	#Borders
	for i in range(0, 51, 50):
		pygame.draw.rect(display, white, (0, i, 410, 5))
	for i in range(0, 406, 405):
		pygame.draw.rect(display, white, (i, 0, 5, 455))
	pygame.draw.rect(display, white, (0, 455, 410, 5))
	pygame.draw.rect(display, white, (205, 0, 5, 55))
	#Recognizing Events
	for event in pygame.event.get():
		#Recognizing The Exit Button
		if event.type == pygame.QUIT:
			break
		#Get Movement Keys/Initialize Direction
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT and x + 20 != body[1][0]: 
				x_change = 20
				y_change = 0
			elif event.key == pygame.K_LEFT and x - 20 != body[1][0]: 
				x_change = -20
				y_change = 0
			elif event.key == pygame.K_UP and y - 20 != body[1][1]:
				y_change = -20
				x_change = 0
			elif event.key == pygame.K_DOWN and y + 20 != body[1][1]:
				y_change = 20
				x_change = 0
	#Draw Apple
	pygame.draw.circle(display, red, (apple_x, apple_y), 10)
	#Apple Collision Detection
	if body[0][0] + 10 == apple_x and body[0][1] + 10 == apple_y:
		#Update Length
		length = length + 1
		#Update Score
		score = score + 1
		#New Apple
		apple_x = random.randrange(15, 395, 20)
		apple_y = random.randrange(65, 440, 20)
	#Moves Snake Head
	x += x_change
	y += y_change
	#Body Hit Detection
	if body[0] in body[1:]:
		break
	#Border Collision Detection
	if x < 5 or x > 385 or y < 55 or y > 450:
		break 
	#Inserts Snake Head Into Body & Deletes Tail
	body.insert(0, (x, y))
	if length < len(body):
		del body[-1]
	#Displays Snake
	for i in range(len(body)):
			pygame.draw.rect(display, blue, (body[i][0], body[i][1], 20, 20))
	#Refresh Screen
	pygame.display.update()
	display.fill(black)
#Exits Game
pygame.display.quit()
pygame.quit()