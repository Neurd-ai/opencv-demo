import os
import cv2
import argparse
import time

def edge_detector(image):
    """Detect edges in an image"""
    edges = cv2.Canny(image, 100, 200)
    return edges


if __name__ == '__main__':
    # argument parser that takes in an image and an output directory
    parser = argparse.ArgumentParser(description='Edge detection')
    parser.add_argument('image_dir', type=str, help='Path to image directory')
    parser.add_argument('output_dir', type=str, help='Path to output directory')
    args = parser.parse_args()

    # look for all images in image_dir, run edge detection on them, and save them to output_dir
    for image in os.listdir(args.image_dir):
        img = cv2.imread(os.path.join(args.image_dir, image))
        edges = edge_detector(img)
        cv2.imwrite(os.path.join(args.output_dir, image), edges)
        # sleep for 1 second to simulate a long running process
        time.sleep(1)
