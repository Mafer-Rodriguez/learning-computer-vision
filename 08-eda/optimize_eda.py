import os
import cv2
from collections import Counter

DATASET = r"C:\Users\isaac\OneDrive\Escritorio\InteligenciaArtificial_Jesus\learning-computer-vision\data\lfw_funneled"

total_images = 0
formats = Counter()
sizes = Counter()
corrupted = 0
images_per_person = {}

for person in os.listdir(DATASET):
    path = os.path.join(DATASET, person)
    if not os.path.isdir(path): continue
    count = 0
    for image in os.listdir(path):
        image_path = os.path.join(path, image)
        img = cv2.imread(image_path)
        if img is None:
            corrupted += 1
            continue
        count += 1
        total_images += 1
        formats[image.split(".")[-1].lower()] += 1
        sizes[(img.shape[1], img.shape[0])] += 1
    images_per_person[person] = count

print("Images:", total_images)
print("People:", len(images_per_person))
print("Formats:", formats)
print("Sizes:", sizes)
print("Corrupted:", corrupted)
print("Images per person:", images_per_person)