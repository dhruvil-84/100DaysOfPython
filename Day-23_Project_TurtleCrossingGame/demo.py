from PIL import Image, ImageDraw
import random


# Function to create a grass texture using parrot green and additional shades of green
def create_grass_texture(size):
    base_green = (0, 255, 102)  # Parrot green RGB value
    texture = Image.new("RGB", (size, size), base_green)  # Start with the parrot green color
    draw = ImageDraw.Draw(texture)

    for x in range(0, size, 4):
        for y in range(0, size, 4):
            # Generate variations around parrot green
            green_variation = random.randint(-50, 50)  # Variation range for realism
            # Ensure the green value remains within 0-255
            green_value = max(0, min(255, base_green[1] + green_variation))
            draw.rectangle([x, y, x + 2, y + 2], fill=(0, green_value, 0))  # Only green channel

    # Adding some noise to the texture for realism
    for x in range(size):
        for y in range(size):
            if random.random() < 0.05:  # 5% chance to add noise
                noise_shade = random.randint(-20, 20)  # Adjust the noise range
                r, g, b = texture.getpixel((x, y))
                new_color = (0,  # Keep red channel as 0
                             max(0, min(255, g + noise_shade)),  # Adjust only green channel
                             0)  # Keep blue channel as 0
                texture.putpixel((x, y), new_color)

    return texture


# Function to create a realistic road texture with different shades of gray and white borders
def create_road_texture(size):
    texture = Image.new("RGB", (size, size), (128, 128, 128))  # Base gray color for road
    draw = ImageDraw.Draw(texture)

    # Add slight variations in the road color for a more textured look
    for x in range(0, size, 2):
        for y in range(0, size, 2):
            shade = random.randint(110, 140)
            draw.rectangle([x, y, x + 1, y + 1], fill=(shade, shade, shade))

    # Draw dashed center line
    for x in range(0, size, 4):
        draw.line([(x, size // 2 - 1), (x + 2, size // 2 - 1)], fill=(255, 255, 255))

    # Draw solid white border lines on the edges of the road
    draw.line([(0, 0), (size, 0)], fill=(255, 255, 255), width=2)  # Top border at the edge
    draw.line([(0, size - 2), (size, size - 2)], fill=(255, 255, 255), width=2)  # Bottom border

    return texture


# Set the size of the main image
width = 450
height = 600
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Create the textures
grass_texture = create_grass_texture(20)
road_texture = create_road_texture(20)

# Height for each section
section_height = 20

# Define sections based on the pattern provided
sections = [
    grass_texture, road_texture, grass_texture, road_texture, grass_texture,
    road_texture, grass_texture, road_texture, grass_texture, road_texture,
    grass_texture, road_texture, grass_texture, road_texture, grass_texture,
    road_texture, road_texture, grass_texture, road_texture, grass_texture,
    road_texture, grass_texture, road_texture, grass_texture, road_texture,
    grass_texture, road_texture, road_texture, grass_texture
]

# Draw each section with textures, starting from y = 10 instead of 0
y_start = 10
for index, texture in enumerate(sections):
    for y in range(y_start, y_start + section_height, texture.size[1]):
        for x in range(0, width, texture.size[0]):
            image.paste(texture, (x, y))
    # Draw a thin black border (2px) between sections for visibility
    if index < len(sections) - 1:  # Avoid drawing after the last section
        draw.line([(0, y_start + section_height), (width, y_start + section_height)], fill=(0, 0, 0), width=2)
    y_start += section_height

# Save and show the image
image.save("hop_mania_road_with_visible_borders.png")
image.show()