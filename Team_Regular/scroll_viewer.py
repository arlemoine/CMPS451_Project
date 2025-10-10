# scroll_viewer.py
import tifffile as tiff, numpy as np, matplotlib.pyplot as plt
from matplotlib.widgets import Slider

arr = tiff.imread("./zebrafish-data/ZS-2.tif")  # change path as needed  (Z, Y, X)

# Normalize to 0–1 just for viewing (keeps data unchanged in memory)
vmin, vmax = np.percentile(arr, (2, 99.8))
arr_vis = np.clip((arr - vmin) / (vmax - vmin + 1e-9), 0, 1)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)
z = arr_vis.shape[0] // 2
im = ax.imshow(arr_vis[z], cmap="gray")
ax.set_title(f"Slice {z+1}/{arr_vis.shape[0]}")
ax.axis("off")

ax_slider = plt.axes([0.15, 0.05, 0.7, 0.03])
slider = Slider(ax_slider, "Z", 1, arr_vis.shape[0], valinit=z+1, valstep=1)

def on_change(val):
    idx = int(val) - 1
    im.set_data(arr_vis[idx])
    ax.set_title(f"Slice {idx+1}/{arr_vis.shape[0]}")
    fig.canvas.draw_idle()

slider.on_changed(on_change)
plt.show()