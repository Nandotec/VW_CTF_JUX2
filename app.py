"""Modulos/Paquetes"""
import html, sqlite3, re
from flask import abort, flash, Flask, make_response, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, LoginManager, logout_user, UserMixin
from flask_wtf.csrf import CSRFProtect

"""Variables"""
app = Flask(__name__)
app.secret_key = "MCS10AED_JJ"
login_manager = LoginManager()
login_manager.init_app(app)
csrf = CSRFProtect(app)
piezas = ["sWYh", "TXdp", "F3Zu", "rXSD", "0#mQ", "v0AD", "UHr%"]

#Base de Datos de Sesiones
usuarios = [
	{
        "id": 1,
        "usuario": "usuario",
        "contrasena": "S4f3!pwd*",
        "dolares": 3000,
        "cuenta": "91825176"
    },
    {
        "id": 2,
        "usuario": "juanita",
        "contrasena": "S4f3r!pwd*jaja",
        "dolares": 1850,
        "cuenta": "26013023"
    },
    {
        "id": 3,
        "usuario": "enrique",
        "contrasena": "3v3nS4f3r!pwd*_*",
        "dolares": 1900,
        "cuenta": "51928341"
    },
    {
        "id": 4,
        "usuario": "panchito",
        "contrasena": "NotS4f33nuf!pwd",
        "dolares": 1800,
        "cuenta": "79182374"
    }
]


"""Elementos para manejo de sesiones con flask_login"""
class User(UserMixin):
    ...

def usuario_por_id(id_usuario: int):
	for usuario in usuarios:
		if int(usuario["id"]) == int(id_usuario):
			return usuario
	return None

def usuario_por_cuenta(num_cuenta):
	for usuario in usuarios:
		if usuario["cuenta"] == num_cuenta:
			return usuario
	return None

@login_manager.user_loader
def user_loader(id: int):
	usuario = usuario_por_id(id)
	if usuario:
		m_usuario = User()
		m_usuario.id = usuario["id"]
		m_usuario.usuario = usuario["usuario"]
		m_usuario.contrasena = usuario["contrasena"]
		m_usuario.dolares = usuario["dolares"]
		m_usuario.cuenta = usuario["cuenta"]
		return m_usuario
	return None
	
@login_manager.unauthorized_handler
def unauthorized_callback():
	return redirect('/')

"""Funciones Globales"""
#Apertura de Cofre
def recompensa(clave=0):
	data = request.form.get("iRespuesta")
	if data == clave:
		return "img/chest_open_bgl.png"
	else:
		return "img/chest_closed_bgl.png"

#Cargar la pagina con contenido de la derecha
def carga(indice, nombre, identificador, clave=0):
	data = request.form.get("iRespuesta")
	if data == clave:
		flash("ENHORABUENA! Esta es tu pieza: " + piezas[indice], "recompensa")
	elif data != None:
		flash("Responde la clave en el campo arriba para obtener tu recompensa!", "ayuda")
		flash("La clave ingresada no fue correcta.", "error")
	else:
		flash("Responde la clave en el campo arriba para obtener tu recompensa!", "ayuda")
	return nombre+identificador+".html"

def limpiarbd():
	with open("static/db/init_main.py") as f:
		exec(f.read())

"""Llamadas por ruta"""
#Landing Page/login
@app.route("/", methods=['GET','POST'])
@csrf.exempt
def login():
	if request.method == "POST":
		usuario = request.form.get("usuario")
		contrasena = request.form.get("contrasena")
		for user in usuarios:
			if user["usuario"] == usuario and user["contrasena"] == contrasena:
				m_usuario = User()
				m_usuario.id = user["id"]
				login_user(m_usuario)
				return redirect("/home")
		return abort(401)
	if current_user.is_authenticated:
		return redirect('/home')
	return render_template('login.html')

#Logout
@app.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
	logout_user()
	return redirect("/")


#Home
@app.route("/home", methods=["POST", "GET"])
@login_required
@csrf.exempt
def landing():
	return render_template("home.html")

#Fugas de Informacion 1
@app.route("/fugas1", methods=["POST", "GET"])
@login_required
@csrf.exempt
def fugas1():
	clave="ud+HYH%&1p6xKQzpEFfyoVSS"
	return render_template(carga(0, "fugas", "1", clave), chest=recompensa(clave))

#Fugas de Informacion 2
@app.route("/fugas2", methods=["POST", "GET"])
@login_required
@csrf.exempt
def fugas2():
	clave="zpDJ#@o5jRZ#R9jBetKkpVJA"
	response = make_response(render_template(carga(1, "fugas", "2", clave), chest=recompensa(clave)))
	response.headers['clave']="zpDJ#@o5jRZ#R9jBetKkpVJA"
	return response

#Fugas de Información 3
@app.route("/fugas3", methods=["POST", "GET"])
@login_required
@csrf.exempt
def fugas3():
	clave="n7dc86SRVGY&901UpJNTjp1N"
	data = request.form.get("iFugas3")
	if data != None:
		conn = sqlite3.connect('static/db/database.db')
		conn.row_factory = sqlite3.Row
		if len(data) == 1 and data.isnumeric():
			resultados = conn.execute('SELECT * FROM SALON WHERE id='+data).fetchall()
			conn.close()
			return render_template(carga(2, "fugas", "3", clave), chest=recompensa(clave), resultados=resultados)
		else:
			if len(data) > 1:
				flash("Exceso de caracteres", "SQLError")
			conn.close()
			return render_template(carga(2, "fugas", "3", clave), chest=recompensa(clave))
	else:
		return render_template(carga(2, "fugas", "3", clave), chest=recompensa(clave))

#Fugas de Informacion 4 (Ejemplo Seguro)
@app.route("/fugas4", methods=["POST", "GET"])
@login_required
@csrf.exempt
def fugas4():
	return render_template("fugas4.html")

#SQL Injection 1
@app.route("/SQLi1", methods=["POST", "GET"])
@login_required
@csrf.exempt
def SQLi1():
	clave="=nb&v=HUsFBNoShbcfWNB+%C"
	data = request.form.get("iSQL1")
	data2 = []
	for i in range(1, 8):
		data2.append(request.form.get("iC" + str(i)))
	if data != None:
			if len(data) < 100:
				data = request.form.get("iSQL1").lower()
				for x in ["SELECT", "FROM", "INSERT", "INTO", "WHERE", "UNION", "DELETE", "UPDATE", "EXEC", "AND", "OR", "-", "/", "*" "#"]:
					if x.lower() in data:
						data = data.replace(x.lower(), "")			
				conn = sqlite3.connect('static/db/SQLi.db')
				conn.row_factory = sqlite3.Row
				try:
					resultados = conn.execute('SELECT *, SUM(calificacion4) AS SUMA FROM SALON4 GROUP BY id4, nombre4, apellido4, calificacion4 HAVING id4='+data+' ORDER BY nombre4 LIMIT 3').fetchall()
					flash("Success", "SQLSuccess")
					conn.close()
					return render_template(carga(3, "SQLi", "1", clave), chest=recompensa(clave), resultados=resultados)
				except sqlite3.DatabaseError as err:
					flash(err, "SQLError")
					conn.close()
					return render_template(carga(3, "SQLi", "1", clave), chest=recompensa(clave))
			else:
				return render_template(carga(3, "SQLi", "1", clave), chest=recompensa(clave))
		
	elif data2[0] != None: 
		if (data2[0] == "SQLite" and data2[1] == "nombre4" and data2[2] == "5"
		and data2[3] == "3" and data2[4] == "SALON4" and data2[5] == "6" and data2[6] == "4"):
			flash(clave, "SQLError")
		return render_template(carga(3, "SQLi", "1", clave), chest=recompensa(clave))
	else:
		return render_template(carga(3, "SQLi", "1", clave), chest=recompensa(clave))

#SQL Injection 2
@app.route("/SQLi2", methods=["POST", "GET"])
@login_required
@csrf.exempt
def SQLi2():
	clave="f7e9050c92a851b0016442ab604b0488"
	data = request.form.get("iSQL2")
	if data != None:
		if data.isnumeric():
			if len(data) == 1 and int(data) in range(1, 7):
				conn = sqlite3.connect('static/db/database.db')
				conn.row_factory = sqlite3.Row
				resultados = conn.execute("""SELECT nombre,apellido,calificacion FROM SALON WHERE id= ? ORDER BY nombre LIMIT 1""", [data]).fetchall()
				conn.close()
				return render_template("SQLi2.html", resultados=resultados)
			else:
				return render_template("SQLi2.html")
		else:
			return render_template("SQLi2.html")
	else:
		return render_template("SQLi2.html")

#Cross Site Scripting 1
@app.route("/XSS1", methods=["POST", "GET"])
@login_required
@csrf.exempt
def XSS1():
	clave="nqJvYu17rWR+pcNCx+UWjWc#"
	data = request.form.get("iNombre")
	data2 = request.form.get("iApellido")
	dataURL = request.args.get('nombre')
	dataURL2 = request.args.get('apellido')
	if data != None and data2 != None:
		if data == html.escape(data) and data2 == html.escape(data2):
			return redirect("/XSS1?nombre=" + data + "&apellido=" + data2)
		else:
			return render_template(carga(4, "XSS", "1", clave), chest=recompensa(clave))
	elif dataURL != None and dataURL2 != None:
		if len(dataURL) > 25 or len(dataURL2) > 25:
			flash("Error inesperado: Número de caracteres excesivo.", "saludo")
			return render_template(carga(4, "XSS", "1", clave), chest=recompensa(clave))
		else:
			dataUlt = dataURL+dataURL2
			if (dataUlt.find("alert('0110001101101100')") != -1 and dataUlt != html.escape(dataUlt, quote=False)
			and re.search("(<\w+>)", dataUlt) != None):
				flash(dataUlt.replace("0110001101101100", clave), "saludo")
			else:
				flash("Buen Día " + dataURL + " " + dataURL2 + ", te deseamos una excelente semana.", "saludo")
			return render_template(carga(4, "XSS", "1", clave), chest=recompensa(clave))
		return render_template(carga(4, "XSS", "1", clave), chest=recompensa(clave))
	else:
		return render_template(carga(4, "XSS", "1", clave), chest=recompensa(clave))

#Cross Site Scripting 2
@app.route("/XSS2", methods=["POST", "GET"])
@login_required
@csrf.exempt
def XSS2():
	clave="pbHc4JDME+tP=ZU053nPmDfp"
	limpiar = request.form.get("iLimpiar")
	data = request.form.get("iNombre")
	data2 = request.form.get("iEnlace")
	data3 = request.form.get("iRadio")
	if request.form.get("iLimpiar") != None:
		if limpiar == "limpiar":
			limpiarbd()
	if data2 == None:
		data2 = "#"	
	conn = sqlite3.connect('static/db/database.db')
	conn.row_factory = sqlite3.Row	
	if data != None and data3 != None:
		if data3 not in ["1", "0"]:
			data3 = 1
		else:
			data3 = int(data3)
		index = data2.lower().find("javascript:")
		if index != -1:
			data2 = data2[:index + 11] + "alert('pbHc4JDME+tP=ZU053nPmDfp'); " +  data2[index + 11:]
		try:
			conn.execute("INSERT INTO JUEGOS (juego, enlace, recomendacion) VALUES(?,?,?)",
			(html.escape(data), html.escape(data2, quote=False), data3))
			conn.commit()
			flash("Se ha agregado la entrada exitosamente.", "Insert")
		except sqlite3.DatabaseError as err:
			flash("Error al agregar la entrada al foro.", "Insert")
	resultados = conn.execute("SELECT * FROM JUEGOS").fetchall()
	conn.close()
	return render_template(carga(5, "XSS", "2", clave), chest=recompensa(clave), resultados = resultados)

#Cross Site Scripting 3 (Ejemplo Seguro)
@app.route("/XSS3", methods=["POST", "GET"])
@login_required
@csrf.exempt
def XSS3():
	clave="871c14878fa75bc327ba87d2d284d596"
	data = request.form.get("iNombre")
	data2 = request.form.get("iApellido")
	if data != None and data2 != None:
		if len(data) < 25 and len(data2) < 25:
			if data == html.escape(data) and data2 == html.escape(data2):
				flash("Buen Día " + data + " " + data2 + ", te deseamos una excelente semana.", "saludo")
		return render_template("XSS3.html")
	else:
		return render_template("XSS3.html")

#Cross Site Request Forgery 1
@app.route("/CSRF1", methods=["POST", "GET"])
@login_required
@csrf.exempt
def CSRF1():
	clave="bxp4#$65r1r0H5GraoJjoyWm"
	data = request.form.get("cuenta")
	data2 = request.form.get("transferencia")
	data3 = request.form.get("confirma")
	url1 = request.args.get("cuenta")
	url2 = request.args.get("transferencia")
	url3 = request.args.get("confirma")
	ghost = False
	usuario = usuario_por_id(current_user.id)
	if data3 != None and data2 != None and data != None:
			if len(data) == 8 and data2.isnumeric() and usuario["dolares"] > int(data2):
				destino = usuario_por_cuenta(data)
				if destino != None:
					usuario["dolares"] -= int(data2)
					destino["dolares"] += int(data2)
					flash("Transferencia Realizada!", "Success")
				else:
					flash("Cuenta destino inexistente", "Errores")
			else:
				flash("Error en monto o cuenta", "Errores")

	elif url3 != None and url1 != None and url2 != None:
		if len(url1) == 8 and url2.isnumeric():
			flash("Confirma la transferencia de " + url2 + " dolares a cuenta #" + url1, "Confirma")
			ghost = True
		else:
			flash("Error en monto o cuenta", "Errores")
		return render_template(carga(6, "CSRF", "1", clave), chest=recompensa(clave), dolares = usuario["dolares"], cuenta = url1, monto = url2)
	elif url1 != None and url2 != None:
		if len(url1) == 8 and url2.isnumeric():
			if int(url2) <= 350:
				if usuario["dolares"] > int(url2):
					destino = usuario_por_cuenta(url1)
					if destino != None:
						usuario["dolares"] -= int(url2)
						destino["dolares"] += int(url2)
						flash("Transferencia Realizada!", "Success")
					else:
						flash("Cuenta destino inexistente", "Errores")
				else:
					flash("Monto insuficiente", "Errores")
			else:
				return redirect("/CSRF1?cuenta=" + url1 + "&transferencia=" + url2 + "&confirma=1")
		else:
			flash("Error en monto o cuenta", "Errores")

	elif data != None and data2 != None:
		if len(data) == 8 and data2.isnumeric():
			return redirect("/CSRF1?cuenta=" + data + "&transferencia=" + data2)
		else:
			flash("Error en monto o cuenta", "Errores")
	if not ghost:
		flash("1", "forma")
	if usuario["dolares"] >= 5000 and usuario["id"] == 1:
		flash(clave, "clave")
	return render_template(carga(6, "CSRF", "1", clave), chest=recompensa(clave), dolares = usuario["dolares"])

#Cross Site Request Forgery 2 (Ejemplo Seguro)
@app.route("/CSRF2", methods=["POST", "GET"])
@login_required
def CSRF2():
	usuario = usuario_por_id(current_user.id)
	if request.method == "POST":
		data = request.form.get("cuenta")
		data2 = request.form.get("transferencia")
		data3 = request.form.get("confirma")
		if data3 != None:
			if len(data) == 8 and data2.isnumeric() and usuario["dolares"] > int(data2):
				destino = usuario_por_cuenta(data)
				if destino != None:
					usuario["dolares"] -= int(data2)
					destino["dolares"] += int(data2)
					flash("Transferencia Realizada!", "Success")
				else:
					flash("Cuenta destino inexistente", "Errores")
			else:
				flash("Error en monto o cuenta", "Errores")

		elif data != None and data2 != None:
			if len(data) == 8 and data2.isnumeric():
				flash("Confirma la transferencia de " + data2 + " dolares a cuenta #" + data, "Confirma")
				return render_template("CSRF2.html", dolares = usuario["dolares"], cuenta = data, monto = data2)
			else:
				flash("Error en monto o cuenta", "Errores")
	flash("1", "forma")
	return render_template("CSRF2.html", dolares = usuario["dolares"])

#Flag 
@app.route("/flag", methods=["POST", "GET"])
@login_required
def flag():
	clave = "sWYhTXdpF3ZurXSD0#mQv0ADUHr%"
	if request.method == "POST":
		clave_usuario = request.form.get("flag")
		if clave_usuario == clave:
			return render_template("flag.html", success = [1], flag = 'img/flag.png')
		else:
			flash("Clave incorrecta", "Error")
	return render_template("flag.html", form = [1])