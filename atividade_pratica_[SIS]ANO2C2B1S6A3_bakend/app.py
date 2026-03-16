from flask import Flask, render_template, request, jsonify
from api_python import  WeatherService # Importa a classe que refatoremos

app = Flask(__name__)
weather_service = WeatherService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clima', methods=['GET'])
def clima():
    cidade = request.args.get('cidade')
    if not cidade:
        return jsonify({"erro": "Cidade não informada"}), 400
    
    resultado = weather_service.obter_previsao(cidade)
    
    if resultado:
        return jsonify(resultado)
    return jsonify({"erro": "Não foi possível obter a previsão"}), 404

if __name__ == '__main__':
    app.run(debug=True)