from PIL import Image, ImageOps, ImageEnhance
import glob, os


def deep_fry_png(IMG_PATH):
    # Check if extension is png
    print(f"Loading image from {IMG_PATH}")
    if IMG_PATH[-4:] == ".png":
        img = Image.open(IMG_PATH)
    else:
        raise Exception("Image is not a png")

    img = img.convert("RGB")
    width, height = img.width, img.height
    img = img.resize((int(width**0.75), int(height**0.75)), resample=Image.LANCZOS)
    img = img.resize((int(width**0.88), int(height**0.88)), resample=Image.BILINEAR)
    img = img.resize((int(width**0.9), int(height**0.9)), resample=Image.BICUBIC)
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, 4)

    # Generate colour overlay
    r = img.split()[0]
    r = ImageEnhance.Contrast(r).enhance(2.0)
    r = ImageEnhance.Brightness(r).enhance(1.5)
    r = ImageOps.colorize(r, (254, 0, 2), (255, 255, 15))
    # Overlay red and yellow onto main image and sharpen the hell out of it
    img = Image.blend(img, r, 0.75)
    img = ImageEnhance.Sharpness(img).enhance(100.0)

    img.save(IMG_PATH[:-4] + "_fried.png", "PNG")


if __name__ == "__main__":
    print("Current Working Directory: ", os.getcwd())
    IMG_PATH = str(input("Enter the path to the image: "))
    IMG_PATH = glob.glob(IMG_PATH)[0]
    print("Found image: ", IMG_PATH)
    deep_fry_png(IMG_PATH)
    print("Done!")
