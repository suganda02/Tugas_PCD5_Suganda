import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter, laplace

# Fungsi untuk menerapkan filter low-pass, high-pass, dan high-boost
def apply_filters(image):
    # Filter Low-Pass (Gaussian Blur)
    low_pass = gaussian_filter(image, sigma=3)

    # Filter High-Pass (Laplacian)
    high_pass = image - gaussian_filter(image, sigma=3)

    # Filter High-Boost (Original + High-Pass)
    high_boost = image + high_pass

    return low_pass, high_pass, high_boost

# Baca citra berwarna
image_path = 'C:/Users/HP/Documents/Tugas Kampus Unsp/Semester 5/Pengolahan Citra Digital/PCD/IMG_20230908_200823 - Copy.jpg' # Ganti dengan path citra Anda
image_color = imageio.v2.imread(image_path)

# Konversi ke grayscale
image_gray = np.dot(image_color[..., :3], [0.299, 0.587, 0.114])

# Terapkan filter pada citra grayscale
low_pass_gray, high_pass_gray, high_boost_gray = apply_filters(image_gray)

# Terapkan filter pada setiap saluran warna (R, G, B) pada citra berwarna
low_pass_color = np.zeros_like(image_color)
high_pass_color = np.zeros_like(image_color)
high_boost_color = np.zeros_like(image_color)

for i in range(3):  # Terapkan pada setiap saluran RGB
    low_pass_color[..., i], high_pass_color[..., i], high_boost_color[..., i] = apply_filters(image_color[..., i])

# Visualisasi hasil
fig, axes = plt.subplots(4, 3, figsize=(15, 15))
titles = ["Original", "Low-Pass", "High-Pass", "High-Boost"]

# Plot citra grayscale
axes[0, 0].imshow(image_gray, cmap='gray')
axes[0, 0].set_title(titles[0] + " (Grayscale)")
axes[1, 0].imshow(low_pass_gray, cmap='gray')
axes[1, 0].set_title(titles[1] + " (Grayscale)")
axes[2, 0].imshow(high_pass_gray, cmap='gray')
axes[2, 0].set_title(titles[2] + " (Grayscale)")
axes[3, 0].imshow(high_boost_gray, cmap='gray')
axes[3, 0].set_title(titles[3] + " (Grayscale)")

# Plot citra berwarna
axes[0, 1].imshow(image_color)
axes[0, 1].set_title(titles[0] + " (Color)")
axes[1, 1].imshow(low_pass_color)
axes[1, 1].set_title(titles[1] + " (Color)")
axes[2, 1].imshow(high_pass_color)
axes[2, 1].set_title(titles[2] + " (Color)")
axes[3, 1].imshow(high_boost_color)
axes[3, 1].set_title(titles[3] + " (Color)")

# Hilangkan sumbu
for ax in axes.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()