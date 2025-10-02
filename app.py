from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta (URL) y qué función debe manejarla
@app.route('/')
def hello_world():
    return '¡Hola Mundo con Flask!'

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(debug=True)
