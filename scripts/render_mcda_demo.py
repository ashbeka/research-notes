import argparse
import os
import numpy as np
import matplotlib.pyplot as plt


def normalize(arr, axis=None, eps=1e-8):
    arr = arr.astype(np.float32)
    minv = arr.min(axis=axis, keepdims=True)
    maxv = arr.max(axis=axis, keepdims=True)
    return (arr - minv) / (maxv - minv + eps)


def mcda_demo(ny=8, nx=8, seed=0):
    rng = np.random.default_rng(seed)
    # Three criteria: severity, sensitivity, access (higher is better after normalization)
    severity = rng.uniform(0, 1, size=(ny, nx))
    sensitivity = rng.uniform(0, 1, size=(ny, nx))
    access = rng.uniform(0, 1, size=(ny, nx))
    # Normalize each criterion to [0,1]
    sev_n = normalize(severity)
    sen_n = normalize(sensitivity)
    acc_n = normalize(access)
    # Weights (sum to 1)
    w = np.array([0.5, 0.3, 0.2], dtype=np.float32)
    # Score: s = w^T q
    s = w[0] * sev_n + w[1] * sen_n + w[2] * acc_n
    return sev_n, sen_n, acc_n, s


def render_heatmaps(sev, sen, acc, score, save_path=None):
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    titles = ["severity", "sensitivity", "access", "score (w^T q)"]
    for ax, img, title in zip(axes, [sev, sen, acc, score], titles):
        im = ax.imshow(img, cmap="magma")
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
    ap = argparse.ArgumentParser(description="Render toy MCDA heatmaps")
    ap.add_argument("--save", type=str, default=None, help="Path to save PNG (optional)")
    ap.add_argument("--ny", type=int, default=8)
    ap.add_argument("--nx", type=int, default=8)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    sev, sen, acc, score = mcda_demo(args.ny, args.nx, seed=args.seed)
    render_heatmaps(sev, sen, acc, score, save_path=args.save)


if __name__ == "__main__":
    main()

