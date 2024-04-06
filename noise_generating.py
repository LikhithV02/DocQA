import cv2
import numpy as np
import os
import random
import tqdm
# , , 'speckle'
def add_random_noise(image):
    noise_type = random.choice(['gaussian','poisson','speckle' ])
    if noise_type == 'gaussian':
        row, col, ch = image.shape
        mean = 0
        var = 0.001
        sigma = var ** 0.05
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        noisy = image + gauss
    elif noise_type == 'salt_pepper':
        s_vs_p = 0.05
        amount = 0.04
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 1
        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
        out[coords] = 0
        noisy = out
    elif noise_type == 'poisson':
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
    elif noise_type == 'speckle':
        row, col, ch = image.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = image + (image * gauss) * 0.5
    return noisy

def random_rotation(image):
    angle = random.randint(-8, 8)
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

input_folder = '/home/asi/Main_proj/Dataset_preparation/processed/div-1099'
output_folder = '/home/asi/Main_proj/Dataset_preparation/processed/noised_div_1099/'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in tqdm.tqdm(os.listdir(input_folder)):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        noisy_image = add_random_noise(image)
        rotated_noisy_image = random_rotation(noisy_image)
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, rotated_noisy_image)