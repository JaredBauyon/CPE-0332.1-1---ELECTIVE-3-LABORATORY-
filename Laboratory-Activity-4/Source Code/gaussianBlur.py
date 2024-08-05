import cv2
import numpy as np

# Load the image
img = cv2.imread('noisyImage.jpg')

# Apply Gaussian Blur
denoised_img = cv2.GaussianBlur(img, (5, 5), 0)

# Save the result
cv2.imshow('Gaussian Blur', denoised_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
