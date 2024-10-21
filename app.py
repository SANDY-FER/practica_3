from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Simulación de almacenamiento de datos de inscritos
inscritos = []

# Ruta para la página de registro
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']
        turno = request.form['turno']
        seminarios = request.form.getlist('seminario')
        
        # Almacenar en la sesión para simular base de datos
        inscritos.append({
            'fecha': fecha,
            'nombre': nombre,
            'apellido': apellido,
            'turno': turno,
            'seminarios': ", ".join(seminarios)
        })
        
        session['inscritos'] = inscritos
        return redirect(url_for('listado'))
    
    return render_template('register.html')

# Ruta para mostrar el listado de inscritos
@app.route('/inscritos')
def listado():
    if 'inscritos' in session:
        return render_template('inscritos.html', inscritos=session['inscritos'])
    return redirect(url_for('register'))

if __name__ == "__main__":
    app.run(debug=True)
