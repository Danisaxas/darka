# Usa una imagen base de Python.  Esta imagen ya tiene Python preinstalado.
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor.
# Todas los comandos subsiguientes se ejecutarán dentro de este directorio.
WORKDIR /app

# Copia los archivos de requirements e instálalos.
# Primero copiamos solo el archivo de requirements para aprovechar la caché de Docker.
COPY requirements.txt ./
# Instala las dependencias de Python usando pip.
# --no-cache-dir reduce el tamaño de la imagen final al no guardar la caché de pip.
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación.
# Esto incluye tu código fuente de Flask (app.py) y cualquier otra cosa que necesite tu aplicación.
COPY . .

# Expone el puerto en el que la aplicación Flask escuchará.
# Por defecto, Flask usa el puerto 5000.
EXPOSE 5000

# Define el comando que se ejecutará cuando se inicie el contenedor.
# Este comando inicia el servidor de Flask.
CMD ["python", "app.py"]
