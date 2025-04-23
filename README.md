Proyecto de Formulario con Flask y WTForms

Este es un proyecto básico de un formulario de registro de usuario utilizando Flask y WTForms, con validaciones personalizadas para los campos de nombre, correo electrónico y contraseña.

📁 Estructura del Proyecto
```plaintext
formulario_app/
│
├── app.py                # Código principal de la aplicación Flask
├── forms.py              # Formulario con validaciones WTForms
├── requirements.txt      # Dependencias del proyecto
│
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base
│   └── register.html     # Formulario de registro
│
└── static/               # Archivos estáticos (CSS)
    └── styles.css        # Estilos para el formulario
```

🚀 Instrucciones para Ejecutar el Proyecto
Clona este repositorio o descarga el proyecto.

Crea un entorno virtual (opcional, pero recomendado):

```plaintext
python -m venv venv
```

En Windows:
```plaintext
venv\Scripts\activate
```

En Mac/Linux:
```plaintext
source venv/bin/activate
```

Instala las dependencias utilizando el archivo requirements.txt:
```plaintext
pip install -r requirements.txt
```
Ejecuta la aplicación:
```plaintext
python app.py
```
La aplicación se ejecutará en http://127.0.0.1:5000

✍️ Funcionalidades
Validaciones de Formulario
El formulario contiene tres campos de validación:

Nombre:

Obligatorio.

Mínimo de 3 caracteres.

Correo electrónico:

Obligatorio.

Debe ser un correo electrónico válido.

Contraseña:

Obligatoria.

Mínimo de 6 caracteres.

Mensajes de Error
Si el usuario no cumple con las reglas de validación, se mostrará un mensaje de error personalizado en la página.

Diseño de la Aplicación
Se utiliza Flask para el Back-End.

WTForms para la creación y validación de formularios.

Plantillas HTML con Jinja2 para renderizar datos dinámicos.

Estilos CSS personalizados en la carpeta static.

⚙️ Requisitos
Python 3.x

Flask

Flask-WTF

email-validator

📝 Autores
Noel Yadiel Cordero Rivera
Profesor: Javier Dastas

