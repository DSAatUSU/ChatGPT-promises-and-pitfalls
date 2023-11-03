from PIL import Image, ImageEnhance
import glob, random
from bs4 import BeautifulSoup
import requests
import re
import urllib.request as urllib2
import os
import http.cookiejar as cookielib

# importing google_images_download module
from google_images_download import google_images_download

import json


def create_collage(img_paths, output, width=500, height=500):
    canvas_x = 2000
    canvas_y = 2000
    new = Image.new("RGB", (canvas_x, canvas_y))
    for img_path in img_paths:
        img = Image.open(img_path)
        img = img.resize((width, height))
        adj_x = random.randint(0, 2000 - width)
        adj_y = random.randint(0, 2000 - height)
        new.paste(img, (adj_x, adj_y))
    new.save(output)


def download_google_images(query):
    arguments = {
        "keywords": query.lower(),
        "format": "png",
        "limit": 10,
    }
    try:
        response.download(arguments)

    # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {
            "keywords": query.lower(),
            "format": "jpeg",
        }
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass


if __name__ == "__main__":
    response = google_images_download.googleimagesdownload()
    query = "Parrot"
    download_google_images(query)
    img_paths = glob.glob(f"./downloads/{query}/*")
    print("Found", len(img_paths), "images")
    create_collage(img_paths, "collage.jpg")
    print("Done!")
