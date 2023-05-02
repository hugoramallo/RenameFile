import os

# Directorio de trabajo
# Acordarse de poner el path con la barra inversa //
path = "Path"

# Bucle para renombrar archivos
i = 1
for filename in os.listdir(path):
    if filename.startswith("IMG_"):
        nombre_anterior = os.path.join(path, filename)
        nuevo_nombre = os.path.join(path, "nombrearchivo_" + str(i).zfill(2) + ".jpeg")
        os.rename(nombre_anterior, nuevo_nombre)
        i += 1

