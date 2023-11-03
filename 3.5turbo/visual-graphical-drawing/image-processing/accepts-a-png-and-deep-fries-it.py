from PIL import Image, ImageEnhance

# Function to deep fry the image
def deep_fry_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Increase the saturation
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(2)

    # Increase the contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)

    # Increase the sharpness
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2)

    # Save the deep fried image
    fried_image_path = image_path.replace('.png', '_fried.png')
    img.save(fried_image_path)
    print(f"Deep fried image saved as {fried_image_path}")

# Ask user for the path of the PNG image
image_path = input("Enter the path of the PNG image: ")

# Deep fry the image
deep_fry_image(image_path)
