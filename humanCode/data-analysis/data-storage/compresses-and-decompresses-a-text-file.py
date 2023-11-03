import zipfile
import os

def compress_file(filename):
    archiveName = input("Input zip archive name: ")
    with zipfile.ZipFile(archiveName, 'w') as zip:
        zip.write(os.path.join('./', filename))
        zip.close()


def decompress_file(filename):
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('./')

option = input("Decompress or compress? [dC]: ")
filename = input("Filename: ")

if option == "d":
    decompress_file(filename)
else:
    compress_file(filename)
