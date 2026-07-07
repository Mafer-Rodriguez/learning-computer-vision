#vamos a acceser a las imagenes que tenemos guardadas en la carpeta 
#Data Set, usaremos nuevas librerias, una llamada PiLLOW
#Pillow sirve para abrir imagenes que tien en local y manipularla, en este caso vamos a convertir las imagenes a escala de grises, para que el algoritmo de reconocimiento facial funcione mejor.
#Ademas usaremos la libreria os para acceder a los archivos de la carpeta dataset, y la libreria numpy para convertir las imagenes a un formato que pueda ser utilizado por el algoritmo de reconocimiento facial.
#OS sirve para minipular los directorios de su computadora
#Finalmente procesaremos todos essos datos con OPENCV y NUMPY
#Recuerden que NUMPY sirve ára hacer calculos o operaciones matematicos, de manera rapida e 
#eficiente, ademas de que manipula matrices de manera muy flexible 

import cv2
import numpy as np
import os
from PIL import Image



#Primero vamos a definir el path donde tenemos guardados nuetras imgenes 
#Despues vamos a crear la instancia de nuetro nuevo modelo 
#Luego vamos a inicializar el detector de rostros 

PATH = 'Dataset - Programacion para IA' #ruta donde tenemos guardadas nuestras imagenes
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

#Hacer un listado de las imagenes guardadas en el path
#despues recorrer cada imagen, convertirla a escala de grises, y luego detectar el rostro en la imagen, para finalmente agregar el rostro detectado a una lista de rostros, y el ID del usuario a una lista de IDs.
#detectar rostros dentro de la imagen 
#extrar el ID de cada imagen 
#finalmente guardamos cada imagen en un arreglo 
#para despues pasarlas al modelo con su respectivo ID 

# Todos esos pasos los haremos con una funcion llamada get_imagenes_and_labels, que recibe como parametro el path donde tenemos guardados nuestras imagenes, y devuelve dos listas: una con los rostros detectados en las imagenes, y otra con los IDs de cada usuario.
def get_imagenes_and_labels(path):
    #listas comprensivas , se compone se componen de tres cosas 
    #la primera es :
    #investigar ruta absoluta 
    # en esta parte se esta colocando PATH en mayusculas, porque recordemos que es una constante 
    images_paths = [os.path.join(PATH, image_path) for image_path in os.listdir(path)] #obtenemos el path de cada imagen en la carpeta dataset
    sample_images = []
    labels_ids = []

    #A continuacion realizaremos un ciclo, que recorra cada imagen guardada en la 
    #variable "images_path" y accederemos a cada imagen con pillow y cambiaremos su 
    #tonalidad a blanco y negro. 
    for ip in images_paths: 
        #Entrar a la imagen y convertir a blanco y negro 
        PIL_image = Image.open(ip).convert("L")
        #convertir la imagen abierta a una matriz de pixeles 
        image_matrix = np.array(PIL_image, 'uint8')

        #Ahora vamos a extrar el ID de las imagenes 
        id = int(os.path.split(ip)[1])
        faces = detector.detectMultiScale(
            image_matrix,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30,30)

        )
        #pasamos por cada rostro detectado y agregamos al sample images 
        for (x,y,w,h) in faces:
            sample_images.append(image_matrix[y:y+h,x:x+w])
            labels_ids.append(id)

        #def get_imagenes_and_labels(PATH):
    return sample_images, labels_ids 
        
faces, labels =get_imagenes_and_labels(PATH)
  
#Obtener un arreglo de IDS, pasarlos al recognizer y despues entrenar el modelo 
 #con las caras contronaldas 
    
recognizer.train(faces, np.array(labels))
#escribir el archivo en nuestro falder
recognizer.write('trainer/trainer.yml')
#Mensaje de termino 
print(f"\n [INFO] {len(np.unique(labels))}")#Rostros almacenados.Termino el programa.
        

