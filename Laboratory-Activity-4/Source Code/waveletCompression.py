import pywt
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('randImg1.jpg', 0)

coeffs = pywt.dwt2(image, 'bior1.3')
cA, (cH, cV, cD) = coeffs

threshold = 20

cA_thresholded = pywt.threshold(cA, threshold, mode = 'soft')
cH_thresholded = pywt.threshold(cH, threshold, mode = 'soft')

coeffs_thresholded = (cA_thresholded, (cH_thresholded, cV, cD))
img_compressed = pywt.idwt2(coeffs_thresholded, 'bior1.3')

plt.imshow(img_compressed, cmap = 'gray')
plt.title('Compressed Image'), plt.xticks([]), plt.yticks([])
plt.show()