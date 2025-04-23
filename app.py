from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistroUsuarioForm

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

@app.route('/', methods=['GET', 'POST'])
def registrar():
    form = RegistroUsuarioForm()
    if form.validate_on_submit():
        flash(f"Usuario {form.nombre.data} registrado exitosamente.", "success")
        return redirect(url_for('registrar'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)