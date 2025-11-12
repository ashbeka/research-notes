import argparse
import os
import numpy as np
import matplotlib.pyplot as plt


def bytes_per_sec_raw(T, H, W, d_bits=16):
    # raw 16-bit imagery by default
    return T * H * W * (d_bits // 8)


def bytes_per_sec_embed(T, H, W, m, dtype_bits=32):
    # embedded float features of dimension m
    return T * H * W * m * (dtype_bits // 8)


def main():
    ap = argparse.ArgumentParser(description="Render uplink payload vs embedding dim m")
    ap.add_argument("--save", type=str, default=None, help="Path to save PNG (optional)")
    ap.add_argument("--H", type=int, default=512)
    ap.add_argument("--W", type=int, default=512)
    ap.add_argument("--T", type=float, default=2.0, help="tiles per second")
    ap.add_argument("--d_bits", type=int, default=16, help="raw bit depth per channel (e.g., 16)")
    ap.add_argument("--m_min", type=int, default=8)
    ap.add_argument("--m_max", type=int, default=256)
    ap.add_argument("--m_step", type=int, default=8)
    args = ap.parse_args()

    ms = np.arange(args.m_min, args.m_max + 1, args.m_step)
    raw_bps = bytes_per_sec_raw(args.T, args.H, args.W, d_bits=args.d_bits)
    emb_bps = bytes_per_sec_embed(args.T, args.H, args.W, ms)
    reduction = raw_bps / np.maximum(emb_bps, 1e-9)

    fig, ax1 = plt.subplots(figsize=(6, 4))
    ax2 = ax1.twinx()

    l1 = ax1.plot(ms, emb_bps / 1e6, label="embedded (MB/s)", color="tab:blue")
    l2 = ax1.hlines(raw_bps / 1e6, xmin=ms.min(), xmax=ms.max(), colors="tab:gray", linestyles="dashed", label="raw (MB/s)")
    l3 = ax2.plot(ms, reduction, label="reduction (raw/embedded)", color="tab:orange")

    ax1.set_xlabel("embedding dim m")
    ax1.set_ylabel("bytes/sec (MB/s)")
    ax2.set_ylabel("reduction ratio (x)")
    ax1.set_title("Uplink payload vs embedding dimension")

    lines = l1 + l3
    labels = [ln.get_label() for ln in lines]
    ax1.legend(lines, labels, loc="upper right")
    plt.tight_layout()

    if args.save:
        os.makedirs(os.path.dirname(args.save), exist_ok=True)
        plt.savefig(args.save, dpi=200)
    else:
        plt.show()


if __name__ == "__main__":
    main()

