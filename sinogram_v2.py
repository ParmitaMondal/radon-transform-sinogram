from __future__ import print_function, division
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage
from scipy import ndimage, misc
from skimage.transform import radon, rescale

image = skimage.data.shepp_logan_phantom()
image = rescale(image, scale=0.4, mode='reflect')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))

ax1.set_title("Original")
ax1.imshow(image, cmap=plt.cm.Greys_r)

theta = np.arange(0., 360., 1.0)
empty_array = np.empty((180, 1), float)
b = 359

for i in range(0, b):
    rotated = ndimage.rotate(image, angle=i) 
    a = [sum(k) for k in zip(*rotated)] 
    z = np.array(a) 
    b = z.reshape(-1, 1) 
    z1 = np.concatenate((empty_array, b), axis=1) 
    empty_array = z1



ax2.set_title("Radon transform\n(Sinogram)")
ax2.set_xlabel("Projection angle (deg)")
ax2.set_ylabel("Projection pos (pixels)")
ax2.imshow(empty_array, cmap=plt.cm.Greys_r,
           extent=(0, 360, 0, empty_array.shape[0]), aspect='auto')

fig.tight_layout()
plt.show()
