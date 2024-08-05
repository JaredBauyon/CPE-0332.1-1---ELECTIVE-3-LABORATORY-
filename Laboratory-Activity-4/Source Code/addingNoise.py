import matplotlib.pyplot as plt
from skimage.util import random_noise

def plot_comparison(original, modified, title):
    fig, (ax1, ax2) = plt.subplots(ncols = 2, figsize = (10, 5))
    ax1.imshow(original, cmap = 'gray')
    ax1.set_title('Original image')
    ax1.axis('off')
    ax2.imshow(modified, cmap='gray')
    ax2.set_title(title)
    ax2.axis('off')
    plt.show()

fruit_image = plt.imread('randImg1.jpg')

# Add noise to the image
noisy_image = random_noise(fruit_image)

# Show the original and resulting image
plot_comparison(fruit_image, noisy_image, 'Noisy image')

plt.imsave('noisyImage.jpg', noisy_image)