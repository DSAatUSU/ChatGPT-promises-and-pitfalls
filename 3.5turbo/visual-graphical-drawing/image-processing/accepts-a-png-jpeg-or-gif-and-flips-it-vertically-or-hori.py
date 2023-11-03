from PIL import Image

def flip_image(image_path, flip_type):
    # Open the image file
    image = Image.open(image_path)
    
    # Flip the image vertically
    if flip_type == 'vertical':
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # Flip the image horizontally
    elif flip_type == 'horizontal':
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return "Invalid flip type. Please choose 'vertical' or 'horizontal'."
    
    # Save the flipped image
    flipped_image.save("flipped_image.png")  # You can change the output file name if needed
    return "Image flipped successfully."

# Ask for user input
image_path = input("Enter the path to the image file: ")
flip_type = input("Enter the flip type (vertical/horizontal): ")

# Flip the image and display the result
print(flip_image(image_path, flip_type))
