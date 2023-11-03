def compress_file(filename):
    archiveName = input("Input zip archive name: ")
    with zipfile.ZipFile(archiveName, 'w') as zip:
        zip.write(os.path.join('./', filename))
        zip.close()

