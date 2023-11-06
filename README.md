# bloody-buddy

## Proceso de Instalación

El siguiente proceso de instalación muestra como desplegar en una instancia de AWS
un sistema de Django.

1. Crear una instancia de AWS EC2 (_free tier_).
    - Configurar la instancia con nuestra propia llave de SSH.
    - Crear nuevas reglas de **_Inbound Security Group_** y agregarlas a la instancia.
        ```
        HTTP | TCP | 80   | 0.0.0.0/0
        TCP  | TCP | 8001 | 0.0.0.0/0
        ```
    - Conectarse a la nueva instancia EC2 con tu llave privada.
        ```
        $ ssh -i ~/.ssh/id_rsa ubuntu@<your-ec2-public-ip-address>
        ```
2. Actualiza tu nueva instancia.
    ```
    $ sudo apt update

    $ sudo apt -y upgrade
    ```
3. Instala los pre-requisitos.
    ```
    $ sudo apt install git python3.10-venv -y
    ```
4. Clona el repositorio.
    ```
    $ mkdir projects
    
    $ cd projects
    
    $ git clone https://github.com/cibervicho/bloody-buddy.git
    
    $ cd bloody-buddy/
    ```
5. Crea y activa un ambiente virtual.
    ```
    $ python3 -m venv env

    $ source env/bin/activate
    ```
6. Instala los requerimientos del proyecto.
    ```
    $ pip install -r requirements.txt
    ```
7. Ejecuta las migraciones para generar la Base de Datos.
    ```
    $ python manage.py migrate
    ```
8. Actualiza la configuración del sistema para que puedas acceder desde Internet.
    ```
    $ sed -i '/ALLOWED_HOSTS*/c\ALLOWED_HOSTS = ["<your-ec2-public-ip-address>"]' bloodybuddy/settings.py
    ```
    **_NOTA: Reemplaza el comando con la dirección pública de la instancia EC2_**

9. Configura las siguientes variables de entorno.
    ```
    $ export USERNAME_FIELD=admin@admin.com
    
    $ export DJANGO_SUPERUSER_PASSWORD=AdminPassword123
    
    $ export DJANGO_SUPERUSER_NAME=Admin
    
    $ export DJANGO_SUPERUSER_LAST_NAME=Administer
    ```

    **_NOTA: Estas variables de entorno se utilizan para generar el Super Usuario en modo no interactivo_**

10. Crea la cuenta de _Super Usuario_ en modo _no interactivo_.
    ```
    $ python manage.py createsuperuser --no-input --email $USERNAME_FIELD
    ```
11. Ejecuta el servidor.
    ```
    $ python manage.py runserver 0.0.0.0:8001
    ```
12. En un navegador, abre la página de la aplicación.
    ```
    http://<your-ec2-public-ip-address>:8001/api/v2/usuarios
    ```

    **_NOTA: Reemplaza la URL con la dirección pública de la instancia EC2_**
