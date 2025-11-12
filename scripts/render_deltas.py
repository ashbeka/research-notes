import argparse
import os
import numpy as np
import matplotlib.pyplot as plt


def make_synthetic_tile(h=128, w=128, seed=42):
    rng = np.random.default_rng(seed)
    base = rng.normal(0.0, 0.2, size=(h, w))
    grad_y, grad_x = np.mgrid[0:h, 0:w]
    grad = (grad_x / w) * 0.5
    blob = np.exp(-(((grad_x - w * 0.6) ** 2) + ((grad_y - h * 0.4) ** 2)) / (2 * (0.1 * w) ** 2))
    img = base + grad + 0.8 * blob
    return img.astype(np.float32)


def compute_deltas(pre, mid, post):
    d1 = post - pre
    d2 = post - 2.0 * mid + pre
    return d1, d2


def render_grid(pre, mid, post, d1, d2, save_path=None):
    fig, axes = plt.subplots(1, 5, figsize=(14, 3))
    ims = [pre, mid, post, d1, d2]
    titles = ["pre (t1)", "mid (t2)", "post (t3)", "Delta1 (t3 - t1)", "Delta2 (t3 - 2*t2 + t1)"]
    cmaps = ["viridis", "viridis", "viridis", "seismic", "seismic"]
    for ax, img, title, cmap in zip(axes, ims, titles, cmaps):
        im = ax.imshow(img, cmap=cmap)
        ax.set_title(title, fontsize=9)
        ax.axis("off")
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=200)
    else:
        plt.show()


def main():
    ap = argparse.ArgumentParser(description="Render Delta1/Delta2 grid from synthetic tiles")
    ap.add_argument("--save", type=str, default=None, help="Path to save PNG (optional)")
    ap.add_argument("--h", type=int, default=128)
    ap.add_argument("--w", type=int, default=128)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    pre = make_synthetic_tile(args.h, args.w, seed=args.seed)
    mid = make_synthetic_tile(args.h, args.w, seed=args.seed + 1)
    post = make_synthetic_tile(args.h, args.w, seed=args.seed + 2)
    d1, d2 = compute_deltas(pre, mid, post)
    render_grid(pre, mid, post, d1, d2, save_path=args.save)


if __name__ == "__main__":
    main()

