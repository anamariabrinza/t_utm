from PIL import Image, ImageEnhance

import random

import os

SRC_PATH = "dataset/"
DST_PATH = "aug_dataset/"

if not os.path.exists(DST_PATH):
    os.mkdir(DST_PATH)

def augment_img(img):
    if random.randint(0, 1) == 1:
        img = ImageEnhance.Brightness(img).enhance(random.choice([0.2, 0.5, 1.2, 1.5]))
    if random.randint(0, 1) == 1:
        img = ImageEnhance.Contrast(img).enhance(random.choice([0.2, 0.5, 1.2, 1.5]))

    return img

for img_path in os.listdir(SRC_PATH):
    image = Image.open(SRC_PATH + img_path)
    for idx in range(5):
        aug_img = augment_img(image)
        aug_img.save(DST_PATH + str(idx) + "_" + img_path)
