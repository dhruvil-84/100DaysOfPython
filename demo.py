from PIL import Image

# Updated dimensions for the grid and the final image
grid_width, grid_height = 570, 560  # Updated grid width to add one more column
square_size = 20
final_image_size = 600

# Colors
light_green = (169, 217, 81)  # Light green
dark_green = (162, 208, 73)      # Dark green
black = (0, 0, 0)             # Black for the border

# Create a new image with RGB mode and a black background
image = Image.new("RGB", (final_image_size, final_image_size), black)

# Set the starting coordinates based on the specified margins
start_x = 10  # 10 pixels from the left to center the grid horizontally
start_y = 30  # 30 pixels from the top

# Draw the checkerboard pattern within the grid area
for y in range(0, grid_height, square_size):
    for x in range(0, grid_width, square_size):
        # Choose color based on the position to create a checkerboard pattern
        color = light_green if (x // square_size + y // square_size) % 2 == 0 else dark_green
        # Draw the square
        for i in range(square_size):
            for j in range(square_size):
                image.putpixel((start_x + x + i, start_y + y + j), color)

# Save the image
image.save("green_field_centered.png")

# Display the image (optional)
image.show()