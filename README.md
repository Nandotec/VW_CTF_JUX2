# Vulnerabilidades Web - CTF
## Autores: Juan Fernando Ulloa y Jose Luis Ulloa

Usuarios

Solo es necesario usar un usuario distinto a "usuario" para el ejercicio de CSRF.
* usuario - S4f3!pwd*
* juanita - S4f3r!pwd*jaja
* enrique - 3v3nS4f3r!pwd*_*
* panchito - NotS4f33nuf!pwd

Video de Uso - https://youtu.be/lPlKtXeWPU0 

Metodo de Instalacion / Setup de Ambiente

Nosotros usamos solamente Windows mientras creabamos esta herramienta, por lo que solo detallamos como hacerlo en Windows.

* Clonar el repositorio localmente a su maquina en una ubicación de su preferencia. (extraer del zip si lo descargas de esa manera)
* Abrir una consola de comandos y moverse a la carpeta del repositorio.

Con una versión de python superior a 3.9.16 (la herramienta no fue probado con versiones menores, así que se recomienda usar esa como minimo)

Crear un ambiente para instalar los requisitos del requirements.txt (estos comandos son de Windows)
* cd /ruta/al/clon/para/el/ambiente
* python -m venv /ruta/al/clon/para/el/ambiente
* /ruta/al/clon/para/el/ambiente/Scripts/activate.bat 
* pip install -r requirements.txt

Si no usas Windows, visita https://docs.python.org/3/library/venv.html para realizar ajustes correspondientes.

De aqui en adelante, tras activar el ambiente (el segundo comando) y estar en la carpeta del repositorio:
* flask run

Finalmente se abre el enlace que aparece en la consola, y ya se puede empezar a usar la aplicación.

Si se desea reiniciar por completo la base de de datos en algun momento, se puede ejecutar el fichero init.py en la ruta static/db.
