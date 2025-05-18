# Usa una imagen oficial de Python
FROM python:3.11-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos y lo instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia todos los archivos del proyecto
COPY . .

# Comando que se ejecutará al correr el contenedor
CMD ["python", "app.py"]
