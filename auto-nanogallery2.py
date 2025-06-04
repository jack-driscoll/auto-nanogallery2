#!/usr/bin/env python

import os
import json
import re
import argparse
from PIL import Image

def slugify(filename):
    name, ext = os.path.splitext(filename)
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '-', name)
    return f"{name.strip('-')}{ext.lower()}"

def make_thumbnail(src_path, thumb_path, size):
    with Image.open(src_path) as img:
        img.thumbnail(size)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save(thumb_path, 'JPEG', quality=95, subsampling=0)

def process_images(img_dir, thumb_dir, outfile, thumb_size):
    os.makedirs(thumb_dir, exist_ok=True)
    items = []
    filenames = sorted(os.listdir(img_dir))
    for idx, fname in enumerate(filenames, start=1):
        if not fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            continue
        if fname == 'favicon.png':
            continue

        original_path = os.path.join(img_dir, fname)
        slugged_name = slugify(fname)

        slugged_path = os.path.join(img_dir, slugged_name)
        if fname != slugged_name and not os.path.exists(slugged_path):
            os.rename(original_path, slugged_path)
        elif fname != slugged_name and os.path.exists(slugged_path):
            print(f"Skipping rename: {slugged_name} already exists.")
            continue

        thumb_path = os.path.join(thumb_dir, slugged_name)
        make_thumbnail(slugged_path, thumb_path, thumb_size)

        print(f"Processing {slugged_name}")

        items.append({
            "src": f"{img_dir}/{slugged_name}",
            "srct": f"{thumb_dir}/{slugged_name}",
            "title": f"{idx:02d} - {fname}",
            "description": f"img-{idx:02d}"
        })

    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a nanogallery2-compatible gallery.json with thumbnails.",
        epilog="USE: python make-slugged-gallery.py [--images DIR] [--thumbs DIR] [--output FILE] [--size WIDTH HEIGHT]"
    )
    parser.add_argument("--images", default="images", help="Directory containing input images (default: images)")
    parser.add_argument("--thumbs", default="thumbs", help="Directory to save thumbnails (default: thumbs)")
    parser.add_argument("--output", default="gallery.json", help="Output JSON file (default: gallery.json)")
    parser.add_argument("--size", type=int, nargs=2, default=(300, 300), metavar=("WIDTH", "HEIGHT"),
                        help="Thumbnail size as WIDTH HEIGHT (default: 300 300)")

    args = parser.parse_args()

    try:
        process_images(args.images, args.thumbs, args.output, tuple(args.size))
    except Exception as e:
        print("Error:", e)
        print("USE: python make-slugged-gallery.py [--images DIR] [--thumbs DIR] [--output FILE] [--size WIDTH HEIGHT]")

# Everyone say "Thanks, Lupa!"
# - Fitz (2025-06-04)
