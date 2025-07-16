from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def inicio():
    return '✅ App Flask funcionando correctamente'

@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        datos = request.json
        if not datos:
            return jsonify({'error': 'No se recibió JSON'}), 400

        url = 'https://script.google.com/macros/s/AKfycbzVSUJLPZT-MFqPbbyttNoTYxLt3IUh_7kivZuPHALAlLqUEbOGfarWDlVF5p6wXsBTIw/exec'
        respuesta = requests.post(url, data=datos)
        return jsonify({'respuesta_script': respuesta.text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
