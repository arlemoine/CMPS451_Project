# quicklooks.py
import tifffile as tiff, numpy as np, matplotlib.pyplot as plt
from pathlib import Path

base_path = "./zebrafish-data/"
paths = [base_path + "ZS-1.tif", base_path + "ZS-2.tif", base_path + "ZS-3.tif"]  # pass multiple files if you want

# Create output folder
output_folder = Path("quicklook_images")
output_folder.mkdir(exist_ok=True)

for p in paths:
    arr = tiff.imread(p)  # (Z, Y, X)
    # Contrast for viewing only
    lo, hi = np.percentile(arr, (2, 99.8))
    mid = arr.shape[0] // 2
    zmax = arr.max(axis=0)

    stem = Path(p).with_suffix("").name

    # Middle slice
    plt.imshow(np.clip((arr[mid]-lo)/(hi-lo+1e-9),0,1), cmap="gray")
    plt.axis("off"); plt.title(f"{stem} – middle Z")
    plt.savefig(output_folder / f"{stem}_middle.png", dpi=300, bbox_inches="tight"); plt.close()

    # Max-Z
    plt.imshow(np.clip((zmax-lo)/(hi-lo+1e-9),0,1), cmap="gray")
    plt.axis("off"); plt.title(f"{stem} – max Z")
    plt.savefig(output_folder / f"{stem}_maxZ.png", dpi=300, bbox_inches="tight"); plt.close()

    print(f"Saved {output_folder}/{stem}_middle.png and {output_folder}/{stem}_maxZ.png")