'''
1)Randomly generating food with different weights
2)Foods which are disappearing after some time(timer)
3)Comment your code
'''


import pygame  # Import the Pygame library
# from color_palette import *  # Import color constants from color_palette module
import time  # Import the time module for time-related functions
import random  # Import the random module for random number generation

pygame.init()  # Initialize Pygame

# Define constants for the game window size and cell size
WIDTH = 600
HEIGHT = 600
CELL = 30

# Initialize variables for game level, score, snake speed and super food status
level = 1
score = 0
snake_speed = 5
super_food_active = False

#Init colors
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)
colorBLUE = (0, 0, 255)
colorGRAY = (128, 128, 128)
colorBLACK = (0, 0, 0)




# Function to draw the grid lines
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# Function to draw a chessboard pattern on the grid
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Create the game window surface
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Define a Point class to represent coordinates
class Point:
    def __init__(self, x, y):  # Initialize with x and y coordinates
        self.x = x
        self.y = y

    def __str__(self):  # Define a string representation for debugging
        return f"{self.x}, {self.y}"

# Define the Snake class
class Snake:
    def __init__(self):  # Initialize the snake with a starting body
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # Initial snake body
        self.dx = 1  # Initial movement direction along x-axis
        self.dy = 0  # Initial movement direction along y-axis

    def move(self):  # Method to move the snake
        for i in range(len(self.body) - 1, 0, -1):  # Iterate through the snake's body
            self.body[i].x = self.body[i - 1].x  # Move each segment of the body
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx  # Move the head of the snake based on direction
        self.body[0].y += self.dy

        # Check if the snake hits the boundary, return False to indicate game over
        if self.body[0].x == -1 or self.body[0].x == 20 or self.body[0].y == -1 or self.body[0].y == 20:
            return False

    def draw(self):  # Method to draw the snake on the screen
        head = self.body[0]  # Get the head of the snake
        pygame.draw.rect(screen, colorGREEN, (head.x * CELL, head.y * CELL, CELL, CELL))  # Draw the head
        for segment in self.body[1:]:  # Iterate through the body segments
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))  # Draw each segment

    def check_collision(self, food, super_food):  # Method to check collision with food
        head = self.body[0]  # Get the head of the snake
        if head.x == food.pos.x and head.y == food.pos.y:  # If snake head overlaps with food
            print("Got food!")  # Print message indicating food is eaten
            self.body.append(Point(head.x, head.y))  # Add a new segment to the snake's body
            pygame.display.update()  # Update the display
            food.change_pos()  # Change the position of the food
        if head.x == super_food.pos.x and head.y == super_food.pos.y:  # If snake head overlaps with food
            global super_food_active
            global score
            print("Got super-food!")  # Print message indicating food is eaten
            self.body.append(Point(head.x, head.y))  # Add a new segment to the snake's body
            pygame.display.update()  # Update the display
            super_food.change_pos()
            super_food_active = False 
            score += 2  # Increment the score when super food is eaten

# Define the Food class
class Food:
    def __init__(self):  # Initialize food with a random position
        self.pos = Point(random.randrange(0, 19), random.randrange(0, 19))  # Random position within grid

    def generate_new_position(self):  # Method to generate a new position for food
        new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))  # Generate a new random position
        while new_pos in snake.body:  # Keep generating until position is not inside snake's body
            new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))
        return new_pos  # Return the valid new position

    def change_pos(self):  # Method to change food position
        global score  # Access the global score variable
        self.pos = self.generate_new_position()  # Generate a new valid position for food
        score += 1  # Increment the score when food is eaten

    def draw(self):  # Method to draw the food on the screen
        pygame.draw.rect(screen, colorRED, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Draw the food
# Define the Super_Food class

class Super_Food(Food): # Inherit from the Food class
    def __init__(self):  # Initialize super food with a random position
        self.pos = Point(random.randrange(0, 19), random.randrange(0, 19))  # Random position within grid
    
    def generate_new_position(self):  # Method to generate a new position for super food
        new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))  # Generate a new random position
        while new_pos in snake.body:  # Keep generating until position is not inside snake's body
            new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))
        return new_pos  # Return the valid new position
    
    def change_pos(self):  # Method to change super food position
        global score  # Access the global score variable
        self.pos = self.generate_new_position()  # Generate a new valid position for super food
        

    def draw(self):  # Method to draw the super food on the screen
        pygame.draw.rect(screen, colorBLUE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Draw the super food



# Create a clock object to control game speed
clock = pygame.time.Clock()

# Create instances of Food and Snake classes
food = Food()  # Initialize food
snake = Snake()  # Initialize snake
super_food = Super_Food()

Super_Food_Event  = pygame.USEREVENT + 1
pygame.time.set_timer(Super_Food_Event, 3000)  #

# Define the font and text for game over message
font = pygame.font.SysFont("Verdana", 60)
game__over = font.render("Game Over", True, colorBLACK)

# Main game loop
done = False
while not done:  # Continue loop until done is True
    for event in pygame.event.get():  # Iterate through events
        if event.type == pygame.QUIT:  # If user closes the window
            done = True  # Set done to True to exit the loop
        if event.type == pygame.KEYDOWN:  # If a key is pressed
            if event.key == pygame.K_RIGHT and snake.dx != -1:  # Right arrow key
                snake.dx = 1  # Set direction to move right
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:  # Left arrow key
                snake.dx = -1  # Set direction to move left
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:  # Down arrow key
                snake.dx = 0  # Set direction to move down
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:  # Up arrow key
                snake.dx = 0  # Set direction to move up
                snake.dy = -1
        if event.type == Super_Food_Event:
            super_food_active = True
            super_food.change_pos()
    
    draw_grid_chess()  # Draw the chessboard grid

    font = pygame.font.SysFont(None, 25)  # Define font for score and level display
    text = font.render("Score: " + str(score) + "   Level: " + str(level), True, colorBLACK)  # Render score and level text
    screen.blit(text, (10, 10))  # Draw the text on the screen

    if snake.move() == False:  # If snake movement returns False (game over condition)
        done = True  # Set done to True to exit the loop
        
        screen.fill(colorRED)  # Fill the screen with red
        screen.blit(game__over, (125, 225))  # Display game over message
        
        pygame.display.update()  # Update the display
        time.sleep(2)  # Pause for 2 seconds before exiting

    snake.check_collision(food,super_food)  # Check collision with food
    if super_food_active:
        super_food.draw() #
            
    if score > level * 3:  # If score exceeds three times the level
        level += 1  # Increase the level
        snake_speed += 3  # Increase the snake's speed

    snake.draw()  # Draw the snake
    food.draw()  # Draw the food
    
    pygame.display.flip()  # Update the entire display
    clock.tick(snake_speed)  # Control game speed based on snake's speed