from paaraksts_nojauna import create
import pygame
import numpy as np
import copy

pygame.font.init()			# initialise the pygame font

screen = pygame.display.set_mode((500,650))			# Total window

pygame.display.set_caption("Eksāmena piekļuves darbs")		# Title

x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
grad = create()
grid = grad.generate()
backupgrid = copy.deepcopy(grid)

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif

def draw_box():			# Highlight the cell selected
	for i in range(2):
		pygame.draw.line(screen, (243, 135, 47,20), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
		pygame.draw.line(screen, (243, 135, 47,20), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)

def draw():		# Function to draw required lines for making Sudoku grid	
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0: #iekrāso maināmos lauciņus
				pygame.draw.rect(screen, (255, 215, 0), (i * dif, j * dif, dif + 1, dif + 1))
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif + 15, j * dif + 0))
			
			if (backupgrid[i][j]) !=0:			#iekrāso stock grid krāsu
				pygame.draw.rect(screen, (25, 215, 0), (i * dif, j * dif, dif + 1, dif + 1))
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif + 15, j * dif + 0))
				
	for i in range(10):				# Draw lines horizontally and verticallyto form grid	
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	
		
def draw_val(val):		# Fill value entered in cell	
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif
	text1 = font1.render(str(val), 1, (0, 0, 0))

	screen.blit(text1, (x * dif + 15, y * dif + 15))
	pygame.draw.rect(screen, (2, 2, 0), (x * dif, y * dif, dif + 1, dif + 1))


def raise_error1():		# Raise error when wrong value entered
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))
def raise_error2():
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))


def valid(m, i, j, val): 		# Check if the value entered in board is valid
		for it in range(9):
			if m[i][it]== val:
				return False
			if m[it][j]== val:
				return False
		it = i//3
		jt = j//3
		for i in range(it * 3, it * 3 + 3):
			for j in range (jt * 3, jt * 3 + 3):
				if m[i][j]== val:
					return False
		return True

# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
	
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump()
	
	for it in range(1, 10):
		if valid(grid, i, j, it)== True:
			grid[i][j]= it
			global x, y
			x = i
			y = j
			# white color background\
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(1)
			if solve(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			# white color background\
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(50)
	return False

def instruction(): # Display instruction for the game
	text1 = font2.render("PRESS D TO RESET TO DEFAULT", 1, (0, 0, 0))
	text2 = font2.render("PRESS R TO EMPTY THE GRID", 1, (0, 0, 0))
	text3 = font2.render("PRESS ENTER TO SOLVE GRID", 1, (0, 0, 0))
	screen.blit(text1, (30, 520))	
	screen.blit(text2, (30, 540))
	screen.blit(text3, (30, 560))

def result():	# Display options when solved
	text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
	screen.blit(text1, (10, 580))
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:	# The loop thats keep the window running
	screen.fill((255, 255, 255)) # White color background
	for event in pygame.event.get():	# Loop through the events stored in event.get()
		if event.type == pygame.QUIT:	# Quit the game window
			run = False
		if x < 9 and y < 9:		# Get the mouse position to insert number
			if event.type == pygame.MOUSEBUTTONDOWN:
				flag1 = 1
				pos = pygame.mouse.get_pos()
				get_cord(pos)

		if event.type == pygame.KEYDOWN:		# Get the number to be inserted if key pressed
			if event.key == pygame.K_LEFT:
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT:
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP:
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN:
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			if event.key == pygame.K_RETURN:
				flag2 = 1
			if event.key == pygame.K_r:		# If R pressed clear the sudoku board
				rs = 0
				error = 0
				flag2 = 0
				grid =[
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0]
				]
			if event.key == pygame.K_d:		# If D is pressed reset the board to default
				rs = 0
				error = 0
				flag2 = 0
				grid = copy.deepcopy(backupgrid)

	if flag2 == 1:
		if solve(grid, 0, 0)== False:
			error = 1
		else:
			rs = 1
		flag2 = 0
	if val != 0:		
		draw_val(val)
		# print(x)
		# print(y)
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2()
		val = 0

	if error == 1:
		raise_error1()
	if rs == 1:
		result()	
	draw()
	if flag1 == 1:
		draw_box()	
	instruction()
	pygame.display.update()		# Update window
pygame.quit()	# Quit pygame window