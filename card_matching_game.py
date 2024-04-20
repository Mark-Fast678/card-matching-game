# the imports
import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size and caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Image Memory Card Game")

# Load the images
image1 = pygame.image.load("1.png")
image2 = pygame.image.load("2.png")
image3 = pygame.image.load("3.png")
image4 = pygame.image.load("4.png")

# Create a list of image pairs
images = [[image1, image2], [image3, image4]]

# Shuffle the image pairs
random.shuffle(images)

# Create a list to store the flipped cards
flipped = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Get the coordinates of the clicked card
        x, y = pygame.mouse.get_pos()

        # Get the index of the clicked card
        index = x // (size[0] // len(images))

        # Flip the card
        flipped.append(index)

        if len(flipped) > 2:
            # Hide the flipped cards
            flipped = []

        if len(flipped) == 2:
            # Check if the flipped cards match
            if images[flipped[0]] == images[flipped[1]]:
            # Increment the player's score or perform any other action for a match
                print("Not implemented yet")
            else:
                pygame.time.wait(1000)

    # Draw the game
    screen.fill((255, 255, 255))

    for i, image in enumerate(images):
        if i in flipped:
            # Draw the flipped card
            screen.blit(image, (i * (size[0] // len(images)), 0))
        else:
            # Draw the back of the card (black rectangle)
            pygame.draw.rect(screen, (0, 0, 0), (i * (size[0] // len(images)), 0, (size[0] // len(images)), size[1]))

        # Update the display
        pygame.display.flip()

        # End the game when done playing
        pygame.quit()