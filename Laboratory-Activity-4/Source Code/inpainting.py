import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from skimage.restoration import inpaint
from skimage.transform import resize
from skimage import color

plt.rcParams['figure.figsize'] = (10, 8)

def show_image(image, title = 'Image', cmap_type = 'gray'):
    plt.imshow(image, cmap = cmap_type)
    plt.title(title)
    plt.axis('off')

def plot_comparison(img_original, img_filtered, img_title_filtered):
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 8), sharex = True, sharey = True)
    ax1.imshow(img_original, cmap = plt.cm.gray)
    ax1.set_title('Original')
    ax1.axis('off')
    ax2.imshow(img_filtered, cmap = plt.cm.gray)
    ax2.set_title(img_title_filtered)
    ax2.axis('off')

defect_image = plt.imread('randImg2.jpg')
defect_image = resize(defect_image, (100, 100))

maskPath = 'randImg2.csv'

mask = pd.read_csv(maskPath, header = None).to_numpy()
mask = resize(mask, defect_image.shape[:2], anti_aliasing = True)
mask = (mask > 0.5).astype(np.uint8)

# Apply the restoration function to the image using the mask
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, channel_axis = -1)

# Show ther defective image
plot_comparison(defect_image, restored_image, 'Restored image')
plt.show()
