from imutils import build_montages
from imutils import paths
import argparse
import random
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--images', required=True, help="path to input directory of images")
ap.add_argument('-s', '--sample', type=int, default=21, help='# of images to sample')

args = vars(ap.parse_args())

# grab the paths to the images, then randomly select a sample of them
imgPaths = list(paths.list_images(args["images"]))
random.shuffle(imgPaths)
imgPaths = imgPaths[:args["sample"]]


imgs = []

for imgPath in imgPaths:
    img = cv2.imread(imgPath)
    imgs.append(img)



montages = build_montages(imgs, (123, 196), (7, 3))


for mon in montages:
    cv2.imshow('montage', mon)
    cv2.waitKey(0)

