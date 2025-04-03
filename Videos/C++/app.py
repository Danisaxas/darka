from flask import Flask, render_template

# Crea una instancia de la aplicación Flask.
# El primer argumento es el nombre del módulo o paquete.
# __name__ es una variable especial de Python que es el nombre del módulo actual.
app = Flask(__name__)

# Define una ruta para la página principal.
# El decorador @app.route('/') asocia la función hola_mundo con la ruta '/'.
# Cuando un usuario visita la ruta '/', se ejecuta la función hola_mundo.
@app.route('/')
def hola_mundo():
    """
    Esta función se llama cuando un usuario visita la página principal (/).
    Devuelve la cadena '¡Hola, Mundo!' que se mostrará en el navegador.
    """
    return render_template('index.html')

@app.route('/saludo/<nombre>')
def saludo(nombre):
    """
    Esta función se llama cuando un usuario visita la ruta /saludo/nombre.
    Recibe un parámetro 'nombre' de la URL y lo pasa a la plantilla 'saludo.html'.
    """
    return render_template('saludo.html', nombre=nombre)

# Este bloque principal asegura que el servidor de desarrollo de Flask se ejecute
# solo cuando el script se ejecuta directamente (no cuando se importa como módulo).
if __name__ == '__main__':
    # Inicia el servidor de desarrollo de Flask.
    # debug=True permite la recarga automática del servidor al guardar los cambios,
    # lo cual es útil durante el desarrollo.  NO USAR EN PRODUCCION.
    app.run(debug=True, host="0.0.0.0", port=5000)
    # Para acceder desde fuera de la máquina local, usa host="0.0.0.0"
    # y asegúrate de que el puerto 5000 esté abierto en tu firewall.
