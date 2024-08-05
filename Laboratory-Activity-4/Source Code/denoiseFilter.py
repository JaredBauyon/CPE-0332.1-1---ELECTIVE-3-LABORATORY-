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

img = plt.imread('denoised_image.jpg')

denoisedImg = denoise_bilateral(img, channel_axis = -1)

# Show the noisy and denoised image
plot_comparison(img, denoisedImg, 'Denoised Image')