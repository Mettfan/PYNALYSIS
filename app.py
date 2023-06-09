from flask import Flask
import socket
from Analytics.mostSold import showMostSold

app = Flask(__name__)

@app.route('/')
def hello_world():
    return showMostSold([{"name": "CocaCola2L", "price": 28}])

if __name__ == '__main__':
    # Obtener la dirección IP del servidor
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f'Servidor en ejecución en http://{ip_address}:5000/')
    print(f'Con nombre de host: {hostname}')
    
    # Ejecutar la aplicación
    app.run()