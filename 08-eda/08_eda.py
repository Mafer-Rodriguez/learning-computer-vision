#Exploration Data Analysis (EDA) for the dataset
import os 
from collections import Counter 
import cv2 

DATASET = r"C:\Users\isaac\OneDrive\Escritorio\InteligenciaArtificial_Jesus\learning-computer-vision\data\lfw_funneled" #Path to the dataset

total_images = 0
different_people = []
formats = Counter()
sizes = Counter()
corrupted_images = {}
images_per_person = {}

#Definimo las imagenes con las cuales si podemos trabajar 
extensions = (".jpeg", ".jpg", ".png")
print(os.listdir(DATASET))

#Para guardar los folders que no son carpetas, las personas repetidas y los archivos innecesarios
not_folders = []
people_repeated = []
unnecesary_files = []
#recorre persona por persona 
for folder in os.listdir(DATASET):
    # Uno, el nombre del folder y la dirección base.(contruye la ruta completa de la carpeta )
    path_person = os.path.join(DATASET, folder)
    # Se pregunta si es un folder.Verifica que realmente sea una carpeta
    if not os.path.isdir(path_person):
        not_folders.append(path_person)
        continue
        # Pregunto si ya tengo a esa persona dentro de mi arreglo de personas.
        #Evita personas repetidas 
    if folder in different_people:
        people_repeated.append(folder)
        continue
    #Guarda el nombre de la persona 
    different_people.append(folder)
    #Contador de imagenes por persona 
    count_person = 0
    #Recorre los archivos dentro de la carpeta de la persona
    for file in os.listdir(path_person):
        #Verifica que sea una imagen 
        if not file.lower().endswith(extensions):
            unnecesary_files.append(file)
            continue
        
        count_person += 1
        total_images += 1
        #Obtenemos el formato de la imagen 
        extension = file.split(".")[-1]
        formats[extension] += 1

         # Ruta completa de la imagen
        image_path = os.path.join(path_person, file)

        # Lee la imagen
        image = cv2.imread(image_path)

        # Verifica si la imagen está dañada
        if image is None:
            corrupted_images[file] = image_path
            continue

        # Obtiene el tamaño de la imagen
        height = image.shape[0]
        width = image.shape[1]

        sizes[(width, height)] += 1

    # Guarda cuántas imágenes tiene cada persona
    images_per_person[folder] = count_person
    
# How many images are there?
print("Total images:", total_images)

# How many people are there?
print("Total people:", len(different_people))

# What format are they in?
print("Image formats:")
print(formats)

# Are they all the same size?
print("Image sizes:")
print(sizes)

if len(sizes) == 1:
    print("All images have the same size.")
else:
    print("Images have different sizes.")

# Are there any corrupted images?
print("Corrupted images:", len(corrupted_images))

# Si existen imágenes dañadas las muestra
for image in corrupted_images:
    print(image)

# How many images does each person have?
print("Images per person:")

for person in images_per_person:
    print(person, ":", images_per_person[person])