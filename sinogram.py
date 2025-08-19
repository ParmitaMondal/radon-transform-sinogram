
from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt
import skimage
from scipy import ndimage, misc
from skimage.transform import radon, rescale

image = skimage.data.shepp_logan_phantom()
image = rescale(image, scale=0.4, mode='reflect')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))

ax1.set_title("original")
ax1.imshow(image, cmap=plt.cm.Greys_r)

theta = np.arange(0., 360., 1.0)
sinogram = radon(image, theta=theta, circle=True)
ax2.set_title("Radon transform\n(Sinogram)")
ax2.set_xlabel("Projection angle (deg)")
ax2.set_ylabel("Projection position (pixels)")
ax2.imshow(sinogram, cmap=plt.cm.Greys_r,
           extent=(0, 360, 0, sinogram.shape[0]), aspect='auto')

fig.tight_layout()
plt.show()
