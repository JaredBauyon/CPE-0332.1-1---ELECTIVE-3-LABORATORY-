import numpy as np
import matplotlib.pyplot as plt
from skimage import restoration, io

# Load the image
img = io.imread('randImg2.jpg', as_gray = True)

# Apply Wiener filter
deblurred_img = restoration.wiener(img, psf = np.ones((5, 5)) / 25, balance = 0.1)

plt.figure(figsize = (5, 5))
plt.imshow(deblurred_img)
plt.axis('off')
plt.title('Color Image')
plt.show()