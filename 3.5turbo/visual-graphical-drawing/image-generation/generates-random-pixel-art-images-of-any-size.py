from PIL import Image
import random

def generate_pixel_art(width, height):
    # Create a new image with the given dimensions
    image = Image.new(mode="RGB", size=(width, height))
    pixels = image.load()

    # Generate random pixel colors
    for x in range(width):
        for y in range(height):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            pixels[x, y] = (red, green, blue)

    return image

if __name__ == "__main__":
    # Get user input for image dimensions
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # Generate and save the pixel art image
    pixel_art = generate_pixel_art(width, height)
    pixel_art.show()
