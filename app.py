from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# CONFIGURACIÓN PARA LA NUBE
app.config['MYSQL_HOST'] = '172.31.40.23' # IP Privada de tu instancia de BD
app.config['MYSQL_USER'] = 'markk'
app.config['MYSQL_PASSWORD'] = 'PasswordSeguro123' 
app.config['MYSQL_DB'] = 'formulario_db'

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form.get("nombre")
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO registros (nombre) VALUES (%s)", (nombre,))
            mysql.connection.commit()
            cur.close()
            mensaje = f"¡Enviado! Hola {nombre}, ya estás en la base de datos."
        except Exception as e:
            mensaje = f"Error de conexión: {str(e)}"
    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)