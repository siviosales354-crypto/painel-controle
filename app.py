from flask import Flask, render_template, request
import socket
import os

app = Flask(__name__)

# O Render vai ler essas variáveis lá na aba 'Environment'
TUNEL_IP = os.getenv('TUNEL_IP', 'SEU_HOST_AQUI')
TUNEL_PORTA = int(os.getenv('TUNEL_PORTA', 12345))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    comando = request.form.get('comando')
    try:
        # Tenta conectar no túnel TCP da Localtonet
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((TUNEL_IP, TUNEL_PORTA))
            s.sendall(comando.encode())
        return f"Comando '{comando}' enviado com sucesso!"
    except Exception as e:
        return f"Erro: {e}"

if __name__ == '__main__':
    # CORREÇÃO: O Render define a porta pela variável de ambiente 'PORT'
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
