#Exploration Data Analysis (EDA) for the dataset
import os 
from collections import Counter 
import cv2 

DATASET = "lfw_funneled" #Path to the dataset

total_images = 0
different_people = []
formats = Counter()
sizes = Counter()
corrupted_images = {}
images_per_person = {}

#Definimo las imagenes con las cuales si podemos trabajar 
extensions = (".jpeg", ".jpg", ".png")
print(os.listdir(DATASET))
not_folders = []
people_repeated = []
unnecesary_files = []
#recorre persona por persona 
for folder in os.listdir(DATASET):
    # Uno, el nombre del folder y la dirección base.
    path_person = os.path.join(DATASET, folder)
    # Se pregunta si es un folder.
    if not os.path.isdir(path_person):
        not_folders.append(path_person)
        continue
        # Pregunto si ya tengo a esa persona dentro de mi arreglo de personas.
    if folder in different_people:
        people_repeated.append(folder)
        continue
    different_people.append(folder)
    count_person = 0
    for file in os.listdir(path_person):
        if not file.lower().endswith(extensions):
            unnecesary_files.append(file)
            continue
        
        count_person += 1
        total_images += 1
        
        extension = file.split(".")[-1]
        formats[extension] += 1
        

#How many images are there?

#How many people are there?
#What format are they in?
#Are they all the same size?
#Are there any corrupted images?
#How many images does each person have?
