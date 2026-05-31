from flask import Flask, render_template, request
import socket
import os

app = Flask(__name__)

# Configurações do túnel
TUNEL_IP = os.getenv('TUNEL_IP', 'SEU_HOST_AQUI')
TUNEL_PORTA = int(os.getenv('TUNEL_PORTA', 12345))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    comando = request.form.get('comando') # Pega o valor do botão (ex: 'iniciar_controle')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((TUNEL_IP, TUNEL_PORTA))
            s.sendall(comando.encode())
        return f"Comando '{comando}' enviado com sucesso ao Android!"
    except Exception as e:
        return f"Erro de conexão: {e}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
