# Imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo hello.py al contenedor
COPY hello.py .

# Comando que se ejecutará al iniciar el contenedor
CMD ["python", "hello.py"]

# Exponer el puerto en el que corre la app
EXPOSE 8090
