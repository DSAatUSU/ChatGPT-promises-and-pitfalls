from PIL import Image

def grayscale_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Convert the image to grayscale using the convert() method
    gray_image = image.convert('L')
    
    # Save the grayscale image as a new file
    gray_image.save('grayscale.png')
    
    print("Image converted to grayscale successfully!")

if __name__ == "__main__":
    # Ask the user for the image file path
    image_path = input("Enter the path of the PNG image file: ")
    
    # Call the grayscale_image function with the provided image path
    grayscale_image(image_path)
