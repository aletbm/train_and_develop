<div align="center"><img src="logo.png" width="300" /></div>

<h3 align="center">Plataforma ficticia de aprendizaje en línea.</h3>

<div align="center">
    <img src="https://img.shields.io/badge/Python-%E2%89%A53.9-blue?logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Django-v2.1.2-0c4b33?logo=django" />
    <img src="https://img.shields.io/badge/PostgreSQL-v14.2-2F5E8D?logo=postgresql&logoColor=white" />
    <img src="https://img.shields.io/badge/JQuery-v3.6.0-78CFF5?logo=jquery&logoColor=white" />
</div>

------

## 💡 Descripción

Plataforma ficticia que brinda cursos en linea por creadores de contenido audiovisual, inspirada en plataformas populares tales como Udemy o Coursera, este proyecto fue llevado adelante para poder trabajar y mejorar mis skills sin intenciones de generar ningun tipo de lucro, la plataforma se ha desarrollado sobre el *framework* Python Django y se hizo uso de la *BBDD* PostgreSQL.

## 👀 Visitando la plataforma

- Pagina principal: [Home](https://trainanddevelop.herokuapp.com/). Presenta la empresa ficticia, el acceso a algunos cursos gratuitos e informacion que avala el desempeño de la empresa
- Cursos: [Courses](https://trainanddevelop.herokuapp.com/courses/). Presenta los cursos disponibles y una seccion que filtra los cursos por categoria.
- Acerca de nosotros: [About Train&Develop](https://trainanddevelop.herokuapp.com/about_us/). Presenta la vision de la empresa y datos de alcance a nivel mundial.
- Blog: [Blog](https://trainanddevelop.herokuapp.com/blog/). Presenta noticias de relevacia relacionadas con la empresa y su entorno.
- Contacto: [Contact](https://trainanddevelop.herokuapp.com/contact/). Presenta las vias de contacto disponibles para el usuario para con la empresa y su ubicacion fisica.

La plataforma fue hosteada con [Heroku](https://www.heroku.com)

## 📂 Arbol basico del proyecto

+ [Train&Develop](https://github.com/aletbm/train_and_develop/tree/master/traindevelop)
    * [Home](https://github.com/aletbm/train_and_develop/tree/master/home)
        * [home.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/home.html) &#8594; [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)
        * [errors.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/errors.html)
        * [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)
    * [Courses](https://github.com/aletbm/train_and_develop/tree/master/courses)
        * [courses.html](https://github.com/aletbm/train_and_develop/blob/master/courses/templates/courses/courses.html) &#8594; [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)
        * [results.html](https://github.com/aletbm/train_and_develop/blob/master/courses/templates/courses/results.html) &#8594; [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)
        * [info_courses.html](https://github.com/aletbm/train_and_develop/blob/master/courses/templates/courses/info_course.html) &#8594; [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)
    * [About Train&Develop](https://github.com/aletbm/train_and_develop/tree/master/aboutus)
        * [about_us.html](https://github.com/aletbm/train_and_develop/blob/master/aboutus/templates/aboutus/about_us.html) &#8594; [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)
    * [Blog](https://github.com/aletbm/train_and_develop/tree/master/blog)
        * [blog.html](https://github.com/aletbm/train_and_develop/blob/master/blog/templates/blog/blog.html) &#8594; [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)
    * [Contact](https://github.com/aletbm/train_and_develop/tree/master/contact)
        * [contact.html](https://github.com/aletbm/train_and_develop/blob/master/contact/templates/contact/contact.html) &#8594; [base.html](https://github.com/aletbm/train_and_develop/blob/master/home/templates/home/base.html)

## 💻 Lanzar proyecto localmente

### 📋 Pre-requisitos

* El proyecto fue desarrollado sobre [Python v.3.9](https://www.python.org/downloads/release/python-390/) o superiores.
* Se utilizo el *framework* [Django v.2.1.2](https://www.djangoproject.com/download/) y la *BBDD* [PostgresSQL v.14.2](https://www.postgresql.org/download/)
* Se utilizaron las siguientes librerias:
    - [psycopg2 2.9.3](https://pypi.org/project/psycopg2/)
    - [Pillow](https://pypi.org/project/Pillow/)
    - [python-decouple](https://pypi.org/project/python-decouple/)
    - [whitenoise](https://whitenoise.evans.io/en/stable/index.html)
    
### 🔧 Instalación

Procedemos a instalar los paquetes:

```
pip install Django==2.1.2
pip install psycopg2
pip install Pillow
pip install python-decouple
pip install whitenoise
```

Ademas se debe instalar el servidor de [PostgresSQL v.14.2](https://www.postgresql.org/download/) desde su pagina.
Para el funcionamiento del mapa en la app de [Contact](https://github.com/aletbm/train_and_develop/tree/master/contact) se ha utilizado [Mapbox](https://www.mapbox.com) deben crearse una cuenta y obtener sus credenciales para acceder al mapa.

---

### ✏️ Variables de entorno

Para que el proyecto funcione correctamente debemos crear un archivo .env dentro del siguiente directorio  &#8594; [Train&Develop](https://github.com/aletbm/train_and_develop/tree/master/traindevelop) con el siguiente contenido:

```
DB_NAME=                #Nombre de la BBDD
DB_USER=                #Nombre de tu usuario
DB_USER_PASSWORD=       #Tu contraseña
DB_HOST=                #Host
DB_PORT=                #Puerto
EMAIL_HOST_USER=        #Direccion de correo de servicio
EMAIL_HOST_PASSWORD=    #Contraseña de correo de servicio
SECRET_KEY=             #Clave secreta de Django
MAPBOX_ACCESS_TOKEN=    #Token brindada por Mapbox
```

Si desea generar una SECRET_KEY puede utilizar el siguiente codigo en python:

```
import string
import random

chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])
```

Por ultimo debe modificar en [settings.py](https://github.com/aletbm/train_and_develop/blob/master/traindevelop/settings.py) la linea 27 por:

```
DEBUG = True
```

### Correr servidor local de Django y visualizacion de web localmente:

Dentro del directorio raiz del proyecto correr los siguiente comandos:

```
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
```

Si va a correr el proyecto en produccion debe modificar *'DEBUG = True'* y correr *'python manage.py collectstatic --noinput'*

A continuacion abra su navegador de preferencia e ingrese a la siguiente url http://127.0.0.1:8000/ si todo va bien deberia visualizar la pagina principal

## 📣 Modificaciones futuras

La plataforma aun se encuentra en desarrollo, tengo dos objetivos principales que alcanzar, integrar un sistema de logueo de usuarios y añadir un sistema de e-commerce, considero que estos dos puntos son vitales para concluir con el proyecto
