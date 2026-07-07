import cv2
import numpy as np #sirve para trabajar con matrices, en este caso con las imagenes. funciona como un contenedor de datos, es decir, una imagen es una matriz de pixeles, y cada pixel tiene un valor de color.

cap = cv2.VideoCapture(0)

while True:
    is_working, frame = cap.read()
    break
    if not is_working:
        print("La camara no se a inicializo por alguna razon")
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#cvtColor se utiliza para convertir una imagen de un espacio de color a otro. en este caso, se convierte la imagen de BGR (Blue, Green, Red) a HSV (Hue, Saturation, Value). el espacio de color HSV es mas facil de trabajar para detectar colores, ya que el tono (Hue) se puede utilizar para detectar colores especificos, mientras que la saturacion (Saturation) y el valor (Value) se pueden utilizar para ajustar la deteccion de colores.

    verde_bajo = np.array([35, 40, 40], dtype=np.uint8)
    verde_alto = np.array([85, 255, 255], dtype=np.uint8)

    # Definimos la mascara detectar los colores
    mask = cv2.inRange(hsv, verde_bajo, verde_alto) #para crear una mascara que detecte los colores verdes, se utiliza la funcion inRange de OpenCV, que toma como parametros la imagen en el espacio de color HSV, el valor minimo del color a detectar (verde_bajo) y el valor maximo del color a detectar (verde_alto). la funcion inRange devuelve una mascara binaria, donde los pixeles que cumplen con el rango de colores especificado se establecen en 255 (blanco) y los pixeles que no cumplen con el rango se estable

    cv2.imshow("Mi primera vez abrindo la camara", frame)
    cv2.imshow("Ventana de mi mascara ", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):#waitKey se utiliza para esperar a que el usuario presione una tecla. en este caso, se espera a que el usuario presione la tecla "q" para salir del bucle. el & 0xFF se utiliza para obtener el valor de la tecla presionada, ya que waitKey devuelve un valor entero que representa la tecla presionada.  
        break
    # el codigo 0xFF es para obtener el valor de la tecla presionada, ya que waitKey devuelve un valor entero que representa la tecla presionada. el & 0xFF se utiliza para obtener el valor de la tecla presionada, ya que waitKey devuelve un valor entero que representa la tecla presionada. 
cap.release()#release se utiliza para liberar la camara, es decir, para cerrar la camara y liberar los recursos que esta utilizando. es importante liberar la camara para evitar problemas de rendimiento y para evitar que otras aplicaciones puedan utilizar la camara.
cv2.destroyAllWindows()#destroyAllWindows se utiliza para cerrar todas las ventanas que se han abierto con OpenCV. es importante cerrar las ventanas para evitar problemas de rendimiento y para evitar que otras aplicaciones puedan utilizar las ventanas.

