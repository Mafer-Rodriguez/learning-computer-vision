import cv2 #esta es la libreria de opencv
import numpy as np

#buscamos la camara activa o disponible, con regularidad la camara esta en la posicion es la que tenemos instalada
cap = cv2.VideoCapture(0)

#iniciamos un ciclo while infinito para ejecutar nuestra camara, es infinito por que queremos que se mantenga abierta hasta que el usuario decida cerrarla (q)
while True:

    #obtenemos dos variables
    is_working, frame = cap.read()

    
    if not is_working:
        print("la camara no se esta iniciando")
        break

    cam_orange = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #definimos el rango de colores que queremos detectar, en este caso el naranja
    naranja_bajo = np.array([10, 100, 100], dtype=np.uint8)
    naranja_alto = np.array([25, 255, 255], dtype=np.uint8)

    #definimos la mascara detectar los colores
    mask = cv2.inRange(cam_orange, naranja_bajo, naranja_alto) #para crear una mascara que detecte los colores naranjas, se utiliza la funcion inRange de OpenCV, que toma como parametros la imagen en el espacio de color HSV, el valor minimo del color a detectar (naranja_bajo) y el valor maximo del color a detectar (naranja_alto). la funcion inRange devuelve una mascara binaria, donde los pixeles que cumplen con el rango de colores especificado se establecen en 255 (blanco) y los pixeles que no cumplen con el rango se estable
  
    #No sabia si teniamos que poner solo una o las dos ventanas, asi que las puse las dos, una con la imagen original y otra con la mascara para que se vea mejor el resultado.
    #si esta funcionando, abrimos una ventana con la informacion de cada frame que detecta nuestra camara
    cv2.imshow("Mi primera vez abrindo la camara", frame)
    #aqui es donde el naranja se vera blanco y lo demas negro. 
    cv2.imshow("Ventana de mi mascara ", mask)


    #si esta funcionando, abrimos la ventana  y para cerrar la ventana, tenemos que presionar la letra q
    if cv2.waitKey(1) &  0XFF  == ord('q'):
        break
#una vez fuera del ciclo, debemos liberar la camara
cap.release()
#y destruir toda las ventanas que abrimos
cv2.destroyAllWindows()