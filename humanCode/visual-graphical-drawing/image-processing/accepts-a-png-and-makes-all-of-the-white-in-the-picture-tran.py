from PIL import Image
import glob, os


def make_white_transparent(IMG_PATH):
    # Check if extension is png
    print(f"Loading image from {IMG_PATH}")
    if IMG_PATH[-4:] == ".png":
        img = Image.open(IMG_PATH)
    else:
        raise Exception("Image is not a png")

    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(IMG_PATH[:-4] + "_transparent.png", "PNG")


if __name__ == "__main__":
    print("Current Working Directory: ", os.getcwd())
    IMG_PATH = str(input("Enter the path to the image: "))
    IMG_PATH = glob.glob(IMG_PATH)[0]
    print("Found image: ", IMG_PATH)
    make_white_transparent(IMG_PATH)
    print("Done!")
