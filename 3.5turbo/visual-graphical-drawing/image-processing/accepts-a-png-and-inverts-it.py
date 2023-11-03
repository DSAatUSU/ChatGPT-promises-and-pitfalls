from PIL import Image

def invert_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Invert the image
    inverted_image = Image.eval(image, lambda x: 255 - x)

    # Save the inverted image
    inverted_image.save("inverted.png")
    print("Image inverted and saved as inverted.png")


# Prompt the user for the image file path
image_path = input("Enter the path to the PNG image: ")

# Call the invert_image function with the provided path
invert_image(image_path)
