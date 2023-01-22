import math
import pygame
import random
from pygame import mixer
#Always initialize the pygame
pygame.init()

#Setting the screen size
screen = pygame.display.set_mode((800,600))

background = pygame.image.load("background1.png")

mixer.music.load("background.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon0.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX  = []
enemyY  = []
enemyX_change = []
enemyY_change = []

number_of_enemies = 6

for i in range(number_of_enemies):

	enemyImg.append(pygame.image.load("enemy.png"))
	enemyX.append(random.randint(0,735))
	enemyY.append(random.randint(50,150))
	enemyX_change.append(3)
	enemyY_change.append(40)


bulletImg = pygame.image.load("bulletnew.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready"

score_value = 0

font = pygame.font.Font("freesansbold.ttf",32)

final_score = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf",64)


def show_score(x,y):
	score = font.render("SCORE : "+ str(score_value),True, (255,255,255))
	screen.blit(score,(x,y))

def player(x,y):
	screen.blit(playerImg,(x,y))

def enemy(x1,y1,i):
	screen.blit(enemyImg[i],(x1,y1))

def fire_bullet(x,y):
	global bullet_state 
	bullet_state = "fire"
	screen.blit(bulletImg,(x+16,y+10))

def finalscore():
	final = final_score.render("TOTAL SCORE : " + str(score_value), True, (255,255,255))
	screen.blit(final,(300,300))

def game_over_text():

	over_text = over_font.render("GAME OVER !!!",True,(255,255,255))
	screen.blit(over_text,(200,200))

def isCollision(enemyX,enemyY,bulletX,bulletY):

	distance = ((enemyX[i] - bulletX)**2 + (enemyY[i] - bulletY)**2)**0.5

	if distance <= 27:
		return True
	else:
		return False



# Game Loop
running = True

while running:

	screen.fill((190,10,10))

	screen.blit(background,(0,0))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		if  event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				playerX_change = -5
			if event.key == pygame.K_RIGHT:
				playerX_change = 5
			if event.key == pygame.K_SPACE:

				if bullet_state == "ready":
					bullet_Sound = mixer.Sound("laser.wav") 
					bullet_Sound.play()

					bulletX = playerX
					fire_bullet(bulletX,bulletY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0


	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	for i in range(number_of_enemies):

		if enemyY[i] > 440:
			for j in range(number_of_enemies):
				enemyY[j] = 2000
			game_over_text()
			finalscore()
			break

		enemyX[i] += enemyX_change[i]

		if score_value > 120:

			if enemyX[i] <= 0:
				enemyX_change[i] = 4
				enemyY[i] += enemyY_change[i]
			elif enemyX[i] >= 736:
				enemyX_change[i] = -4
				enemyY[i] += enemyY_change[i]

		elif score_value > 550:

			if enemyX[i] <= 0:
				enemyX_change[i] = 5
				enemyY[i] += enemyY_change[i]
			elif enemyX[i] >= 736:
				enemyX_change[i] = -5
				enemyY[i] += enemyY_change[i]
				
		elif score_value > 650:

			if enemyX[i] <= 0:
				enemyX_change[i] = 6
				enemyY[i] += enemyY_change[i]
			elif enemyX[i] >= 736:
				enemyX_change[i] = -6
				enemyY[i] += enemyY_change[i]

		elif score_value > 320:

			if enemyX[i] <= 0:
				enemyX_change[i] = 4.5
				enemyY[i] += enemyY_change[i]
			elif enemyX[i] >= 736:
				enemyX_change[i] = -4.5
				enemyY[i] += enemyY_change[i]

		else:

			if enemyX[i] <= 0:
					enemyX_change[i] = 3
					enemyY[i] += enemyY_change[i]
			elif enemyX[i] >= 736:
					enemyX_change[i] = -3
					enemyY[i] += enemyY_change[i]

		collision = isCollision(enemyX,enemyY,bulletX,bulletY)

		if collision == True:
			bulletY = 480
			bullet_state = "ready"
			score_value += 10
			collision_Sound = mixer.Sound("explosion.wav") 
			collision_Sound.play()
			enemyX[i] = random.randint(0,735)
			enemyY[i] = random.randint(50,150)	
	
		enemy(enemyX[i],enemyY[i],i)
		

	if bulletY < 0:
		bullet_state = "ready"
		bulletY = 480

	if bullet_state == "fire":

		fire_bullet(bulletX,bulletY)
		bulletY -= bulletY_change

	show_score(textX,textY)

	player(playerX,playerY)	
	
	pygame.display.update()