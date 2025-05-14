from flask import Flask, request, render_template, url_for

app =Flask(__name__)

usuarios=[]

@app.route("/",methods=["GET","POST"])
def crud():
    nombre=request.form.get("nombre")
    correo=request.form.get("correo")
    usuarios.append({"nombre_usuario":nombre,"correo_usuario":correo})

    return render_template("registro.html",usuarios=usuarios)


if __name__=="main":
	app.run(debug=True)