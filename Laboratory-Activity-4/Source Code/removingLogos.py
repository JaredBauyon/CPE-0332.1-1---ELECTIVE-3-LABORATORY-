import numpy as np
import matplotlib.pyplot as plt

from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color

def plot_comparison(img_original, img_filtered, img_title_filtered):
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 8), sharex = True, sharey = True)
    ax1.imshow(img_original, cmap = plt.cm.gray)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(img_filtered, cmap = plt.cm.gray)
    ax2.set_title(img_title_filtered)
    ax2.axis('off')

image_with_logo = plt.imread('imgWithLogo.jpg')

mask = np.zeros(image_with_logo.shape[:-1])

mask[500:2000, 40:200] = 1
mask = resize(mask, image_with_logo.shape[:2], anti_aliasing = True)
mask = (mask > 0.5).astype(np.uint8)

image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo, mask, channel_axis = -1)

plot_comparison(image_with_logo, image_logo_removed, 'Image with logo removed')
plt.show()