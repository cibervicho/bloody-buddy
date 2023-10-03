# bloody-buddy

Para soportar MariaDB/MySQL
https://www.digitalocean.com/community/tutorials/how-to-install-mariadb-on-ubuntu-22-04
1. Instalar MariaDB
sudo apt update && sudo apt upgrade -y
sudo apt install -y mariadb-server

2. Configurar MariaDB
sudo mysql_secure_installation

3. etc
...

https://docs.djangoproject.com/en/4.2/ref/databases/#mariadb-notes
1. Instalar los drivers de MySQL
pip install mysqlclient

2. Crear una Base de Datos
CREATE DATABASE <dbname> CHARACTER SET utf8;

4. Conectarse a la BD
https://docs.djangoproject.com/en/4.2/ref/databases/#connecting-to-the-database
