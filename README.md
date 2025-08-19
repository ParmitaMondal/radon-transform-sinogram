# Radon Transform and Sinogram Visualization

This repository contains a simple Python script that demonstrates how to:
- Generate a **Shepp-Logan phantom** (a standard test image for tomography).
- Apply the **Radon transform** to simulate X-ray projections.
- Visualize both the **original phantom** and its **sinogram** side by side.

---

## 🚀 How it Works
1. Loads the Shepp-Logan phantom using `skimage`.
2. Rescales the phantom image.
3. Computes the **Radon transform** (sinogram) for projection angles 0° → 360°.
4. Plots:
   - Left: Original phantom
   - Right: Sinogram representation

---

