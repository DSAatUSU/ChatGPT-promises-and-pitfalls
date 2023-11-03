import os
import requests
from PIL import Image
from io import BytesIO
from google_images_download import google_images_download

# Create a function to download images from Google search
def download_images(keyword, num_images=5):
    response = google_images_download.googleimagesdownload()

    # Set the arguments for image download
    arguments = {"keywords": keyword, "limit": num_images, "print_urls": False}

    # Download images
    paths = response.download(arguments)

    print(paths)
    # Return the downloaded image paths
    return paths[keyword]


# Create a collage from downloaded images
def create_collage(images):
    # Calculate the size of the collage
    num_images = len(images)
    collage_width = 200 * num_images
    collage_height = 200

    # Create a new blank image for the collage
    collage = Image.new("RGB", (collage_width, collage_height))

    # Paste downloaded images onto the collage
    for i, image_path in enumerate(images):
        # Open the downloaded image
        image = Image.open(image_path)

        # Resize the image to fit the collage
        image = image.resize((200, 200), Image.ANTIALIAS)

        # Calculate the position to paste the image
        x = i * 200
        y = 0

        # Paste the image onto the collage
        collage.paste(image, (x, y))

    # Save the final collage image
    collage.save("collage.jpg")
    print("Collage created successfully!")


# Main function
def main():
    # Ask the user for a keyword
    keyword = input("Enter a keyword for image search: ")
    # Download images with the given keyword
    downloaded_images = download_images(keyword, num_images=5)

    # Create a collage from downloaded images
    create_collage(downloaded_images)


# Run the main function
if __name__ == "__main__":
    main()
