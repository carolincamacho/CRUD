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
        return redirect(url_for("crud"))   #llamar al nombre de la función
   
    return render_template("registro.html",usuarios=usuarios)  #lista que entrega el html

@app.route("/update/<int:id>",methods=["GET","POST"]) #ruta con parametros
def update(id):
    print(usuarios)
    estudiante_editar=''
    #TODO: Identificar el diccionario del usuario con id entrega

    for diccionario in usuarios:
        if diccionario ['id']==id:
             estudiante_editar=diccionario
             print("el estudiante a editar es: ", estudiante_editar)
             break
    if request.method=="POST":
         #TODO Actualizar el diccionacio de estudiante,
        estudiante_editar['nombre_usuario']=request.form.get("nombre")
        estudiante_editar['correo_usuario']=request.form.get("correo")
        return redirect(url_for("crud"))

    if estudiante_editar =='':
        return f"no existe el usuario con el id: {id}"
    
    return render_template('editar.html',estudiante_editar=estudiante_editar)
    #return f"el id del uduario a actualizar es: {id}"


if __name__=="main":
	app.run(debug=True)