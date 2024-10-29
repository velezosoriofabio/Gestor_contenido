### 1. Clonar el repositorio:

git clone https://github.com/tu-usuario/nombre-del-repo.git

cd nombre-del-repo

### 2. Crea un entorno virtual (opcional pero recomendado):

python -m venv venv

source venv/bin/activate  

Para activar el ambiente virtual en Windows, se usa 

venv\Scripts\activate

### 3. Instalar las dependencias:

pip install -r requirements.txt

### 4. Configurar la base de datos:

Asegúrate de tener una base de datos MySQL configurada y actualiza las configuraciones en `settings.py`:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'nombre_base_datos',
                'USER': 'tu_usuario',
                'PASSWORD': 'tu_contraseña',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }

### 5. Realiza las migraciones:

python manage.py migrate


### 6. Ejecuta el servidor de desarrollo:

python manage.py runserver
