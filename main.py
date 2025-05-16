from flask import Flask, request, render_template, url_for, redirect

app =Flask(__name__)

usuarios=[]
id_contador=1

@app.route("/",methods=["GET","POST"])
def crud():
    global id_contador
    if request.method=='POST':  #Si accedemos a la ruta con datos del formulario
        nombre=request.form.get("nombre")
        correo=request.form.get("correo")
        usuarios.append({"id":id_contador,"nombre_usuario":nombre,"correo_usuario":correo}) #inserta un usuario
        id_contador+=1
        return redirect(url_for("crud"))  
    
    id_eliminar=request.args.get("borrar")  #para que lo pase a enteros
    if id_eliminar:
        #TODO: Eliminar el usuario con el id del parametro de la lista
        for item in usuarios:
             if str(item['id'])==id_eliminar:
                usuarios.remove(item)
                break
        return redirect(url_for("crud"))      
   
    return render_template("registro.html",usuarios=usuarios)

if __name__=="main":
	app.run(debug=True)