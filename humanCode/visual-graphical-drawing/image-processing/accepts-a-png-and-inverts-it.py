from PIL import Image, ImageOps

im = Image.open('image.png')
im_invert = ImageOps.invert(im)
im_invert.save('image_invert.png', quality=95)
