import matplotlib.pyplot as plt
from skimage.restoration import denoise_bilateral

def plot_comparison(original, modified, title):
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 5))
    ax1.imshow(original)
    ax1.set_title('Original image')
    ax1.axis('off')
    ax2.imshow(modified)
    ax2.set_title(title)
    ax2.axis('off')
    plt.show()

landscape_image = plt.imread('noisyImage.jpg')

denoised_image = denoise_bilateral(landscape_image, channel_axis = -1)

plot_comparison(landscape_image, denoised_image, 'Denoised Image')
