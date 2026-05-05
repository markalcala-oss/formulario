from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form.get("nombre")
        mensaje = f"Hola {nombre}, formulario recibido "
    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
