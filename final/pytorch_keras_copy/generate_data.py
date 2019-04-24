import argparse
import numpy as np
import random
from PIL import Image
import os
from random import randint, seed
import itertools
import cv2

action_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def _generate_mask(height, width, channels):
    """Generates a random irregular mask with lines, circles and elipses"""

    img = np.zeros((height, width, channels), np.uint8)

    # Set size scale
    size = int((width + height) * 0.03)
    if width < 64 or height < 64:
        raise Exception("Width and Height of mask must be at least 64!")

    # Draw random lines
    for _ in range(randint(1, 10)):
        x1, x2 = randint(1, width), randint(1, width)
        y1, y2 = randint(1, height), randint(1, height)
        thickness = randint(3, size)
        cv2.line(img, (x1, y1), (x2, y2), (1, 1, 1), thickness)

    # Draw random circles
    for _ in range(randint(1, 10)):
        x1, y1 = randint(1, width), randint(1, height)
        radius = randint(3, size)
        cv2.circle(img, (x1, y1), radius, (1, 1, 1), -1)

    # Draw random ellipses
    for _ in range(randint(1, 10)):
        x1, y1 = randint(1, width), randint(1, height)
        s1, s2 = randint(1, width), randint(1, height)
        a1, a2, a3 = randint(3, 180), randint(3, 180), randint(3, 180)
        thickness = randint(3, size)
        cv2.ellipse(img, (x1, y1), (s1, s2), a1, a2, a3, (1, 1, 1), thickness)

    return 1 - img


# def random_walk(canvas, ini_x, ini_y, length):
#     x = ini_x
#     y = ini_y
#     img_size = canvas.shape[-1]
#     x_list = []
#     y_list = []
#     for i in range(length):
#         r = random.randint(0, len(action_list) - 1)
#         x = np.clip(x + action_list[r][0], a_min=0, a_max=img_size - 1)
#         y = np.clip(y + action_list[r][1], a_min=0, a_max=img_size - 1)
#         x_list.append(x)
#         y_list.append(y)
#     canvas[np.array(x_list), np.array(y_list)] = 0
#     return canvas


if __name__ == '__main__':
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('--image_size', type=int, default=512)
    parser.add_argument('--N', type=int, default=10000)
    parser.add_argument('--save_dir', type=str, default='train_masks')
    args = parser.parse_args()

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    for i in range(args.N):
        # canvas = np.ones((args.image_size, args.image_size)).astype("i")
        # ini_x = random.randint(0, args.image_size - 1)
        # ini_y = random.randint(0, args.image_size - 1)
        mask = _generate_mask(args.image_size, args.image_size, 3)
        print("save:", i, np.sum(mask))

        img = Image.fromarray(mask * 255).convert('1')
        img.save('{:s}/{:06d}.jpg'.format(args.save_dir, i))
