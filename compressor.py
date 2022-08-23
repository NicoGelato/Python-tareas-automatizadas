from distutils import extension
from pickletools import optimize
from PIL import Image
import os

downloadsFolder = r"C:/Users/gelat/Downloads/"
picturesFolder = r"C:/Users/gelat/Downloads/Imagenes comprimidas/"
pdfFolder = r"C:/Users/gelat/Downloads/PDFs/"

try:
    os.mkdir(picturesFolder)
    os.mkdir(pdfFolder)
except OSError as e:
    if e.errno != e.errno.EEXIST:
        raise


if __name__ == "__main__":
    for fileName in os.listdir(downloadsFolder):

        name, extension = os.path.splitext(downloadsFolder + fileName)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + fileName)
            picture.save(picturesFolder + "comprimida_" +
                         fileName, optimize=True, quality=60)
            print(f"{name}: {extension}")

        if extension in ['.pdf']:
            os.rename(downloadsFolder+fileName, pdfFolder+fileName)
            print(f"{name}: {extension}")
