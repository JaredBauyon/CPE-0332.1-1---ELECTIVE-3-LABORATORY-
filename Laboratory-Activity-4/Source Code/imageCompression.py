from PIL import Image

# Open an image file
with Image.open('randImg1.jpg') as img:

# Compress the image
    img.save('compressedRandImg.jpg', quality = 85, optimize = True)

img.show()
