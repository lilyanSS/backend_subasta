# Subasta Backend
### paso 1 ###

# Instalar python en ubuntu
sudo apt update
sudo apt install python3.7 python3-dev python3-pip

### paso 2 ###
   # Crear entorno virtual en ubuntu  desde la linea de comandos en la carpeta del proyecto

    python3 -m venv myvenv

   # crear entorno virtual en Windows  desde la linea de comandos en la carpeta del proyecto

    python -m venv myvenv

### paso 3 ###

   # Ejecutar entorno virtual en ubuntu desde la linea de comandos en la carpeta del proyecto
source myvenv/bin/activate

   # ejecutar entorno virtual en Windows desde la linea de comandos en la carpeta del proyecto
myvenv\Scripts\activate

### paso 4 ##
   # Instalar requerimintos 
    pip install -r requirements.txt

### paso 5 ### 
   # agregar las credenciales para conectar a mysql en la carpeta subasta en el archivo settings.py 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'DB_NAME',
            'USER': 'DB_USER',
            'PASSWORD': 'admin',
            'HOST': 'localhost',   # o  una direccion  IP donde esta la base de datos
            'PORT': '3306',
        }
    }

### paso 6 ###
   # crear migraciones
    python manage.py migrate

### paso 7 ###
   # correr el servidor
    python manage.py runserver

### aplicar migraciones
        python manage.py makemigrations      