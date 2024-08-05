import pywt
import cv2
from matplotlib import pyplot as plt

#Read in the image
image = cv2.imread('randImg1.jpg', 0)

#Find the coefficients
coeffs = pywt.dwt2(image, 'bior1.3')
cA, (cH, cV, cD) = coeffs

#Plot the images
plt.subplot(121), plt.imshow(cA, cmap='gray')
plt.title('Approximation Coefficient'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cH, cmap='gray')
plt.title('Horizontal Detail Coefficient'), plt.xticks([]),
plt.yticks([])
plt.show()
