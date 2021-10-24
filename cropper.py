#!/bin/env python3

from PIL import Image
import argparse

parser = argparse.ArgumentParser(description="crop an image to 16:9")
parser.add_argument("image", metavar="image", type=str)

args = parser.parse_args()

if not args.image.endswith(".jpg"):
    print("image must be of type jpg")
    exit(1)

img = Image.open(args.image)
if img.format != "JPEG":
    print("image must be of type jpg")
    exit(1)


def new_name(name):
    parts = name.split("/")
    parts[-1] = "crop_" + parts[-1]
    return "/".join(parts)

def calc_crop(w, h):
    if w >= h:
        new_h = w / 16 * 9
        y = (h - new_h) / 2
        return (0, y, w, new_h + y)
    else:
        new_w = h / 16 * 9
        x = (w - new_w) / 2
        return (x, 0, new_w + x, h)

cropped = img.crop(calc_crop(*img.size))
cropped.save(new_name(img.filename))
