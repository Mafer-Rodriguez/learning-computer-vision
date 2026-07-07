import cv2
img = cv2.imread('C:\\Users\\isaac\\OneDrive\\Escritorio\\InteligenciaArtificial_Jesus\\computervision-basics\\02-using-images\\assets\\paisajebonito.jpg') #imread se utiliza para leer una imagen desde el disco. el parametro es la ruta de la imagen que se desea leer. la funcion imread devuelve una matriz de pixeles que representa la imagen. cada pixel tiene un valor de color en formato BGR (Blue, Green, Red).

if img is None:
    print("No se detecto la imagen")
    exit()

alto, ancho, color_patrones = img.shape #shape se utiliza para obtener las dimensiones de la imagen. la funcion shape devuelve una tupla con el alto, ancho y numero de canales de color de la imagen. en este caso, se asigna el alto a la variable alto, el ancho a la variable ancho y el numero de canales de color a la variable color_patrones.
print(f"Mi imagen tiene un alto (filas) de: {alto} pixeles, un ancho (columnas) de: {ancho} pixeles")
print(f"La cantidad de numeros que componen un pixel: {color_patrones}")

print("Esto es nuestra imagen ", img)

first_pixel = img[0, 0] #para acceder a un pixel especifico de la imagen, se utiliza la sintaxis img[fila, columna]. en este caso, se accede al pixel en la fila 0 y columna 0 (esquina superior izquierda) y se asigna a la variable first_pixel
print(first_pixel)


centro_x = ancho // 2 #se calcula el centro de la imagen dividiendo el ancho total entre 2 usando una division entera. esto nos da la columna exacta que divide la imagen a la mitad.
grosor = 100 #se define el ancho de la franja negra en pixeles. puedes modificar este valor si quieres que la linea en medio sea mas delgada o mas gruesa.
img[:, (centro_x - (grosor // 2)):(centro_x + (grosor // 2))] = [0, 0, 0] #se accede a un rango de pixeles usando slicing. el primer parametro ':' indica que se seleccionan todas las filas (el alto completo). el segundo parametro selecciona las columnas desde la mitad menos la mitad del grosor hasta la mitad mas la mitad del grosor, y se les asigna el color negro [0,0,0] en formato BGR.

cv2.imshow("Mi imagen", img) #imshow se utiliza para mostrar una imagen en una ventana. el primer parametro es el nombre de la ventana y el segundo parametro es la imagen que se desea mostrar. en este caso, se muestra la imagen modificada con

cv2.waitKey(0) #waitKey se utiliza para esperar a que el usuario presione una tecla. el parametro es el tiempo en milisegundos que se desea esperar. si se establece en 0, la funcion esperara indefinidamente hasta que el usuario presione una tecla.

cv2.destroyAllWindows() #destroyAllWindows se utiliza para cerrar todas las ventanas abiertas por OpenCV. esta funcion se llama despues de waitKey para asegurarse de que la ventana se cierre correctamente.