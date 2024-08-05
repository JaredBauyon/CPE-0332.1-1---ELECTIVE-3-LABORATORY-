import cv2
import numpy as np
from PIL import Image

# Load the image
img = cv2.imread('randImg1.jpg')

cv2.imwrite('compressedImg.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])

def compressedImage(imgPath, k):
    compImg = Image.open(imgPath).convert('RGB')  
    imgArray = np.array(compImg) / 255.0

    compressed_channels = []
    for i in range(3):  # 
        U, s, V = np.linalg.svd(imgArray[:, :, i], full_matrices = False)
        S = np.diag(s[:k])
        compressed_channel = np.dot(U[:, :k], np.dot(S, V[:k, :]))
        compressed_channels.append(compressed_channel)

    # Stack the channels back together
    compressedImage = np.stack(compressed_channels, axis = 2)
    return Image.fromarray((compressedImage * 255).astype(np.uint8))

# Compress and save the image
compressImage = compressedImage('compressedImg.jpg', 50)
compressImage.save('compressedImage.jpg')  

# Convert PIL image to OpenCV format
compressImage_cv = cv2.cvtColor(np.array(compressImage), cv2.COLOR_RGB2BGR)

# Display the image
cv2.imshow('Compressed Image', compressImage_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
