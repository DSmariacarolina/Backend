import os
import requests
from dotenv import load_dotenv

class WeatherService:
    """Classe responsável pela comunicação com a WeatherAPI."""
    
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("Erro: WEATHER_API_KEY não encontrada no arquivo .env.")

    def obter_previsao(self, cidade: str):
        """Busca a previsão do tempo para uma cidade específica."""
        params = {
            "key": self.api_key,
            "q": cidade,
            "lang": "pt"
        }

        try:
            # timeout=10 evita que o código fique esperando indefinidamente
            resposta = requests.get(self.BASE_URL, params=params, timeout=10)
            resposta.raise_for_status() 
            
            dados = resposta.json()
            return {
                "cidade": dados['location']['name'],
                "temperatura": dados['current']['temp_c'],
                "condicao": dados['current']['condition']['text'],
                "umidade": dados['current']['humidity']
            }

        except requests.exceptions.HTTPError as e:
            print(f"Erro de HTTP (Verifique o nome da cidade): {e}")
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
        except (KeyError, TypeError):
            print("Erro ao processar os dados da API.")
        
        return None

# Bloco de execução principal
if __name__ == "__main__":
    try:
        service = WeatherService()
        cidade_input = input("Digite o nome da cidade: ").strip()

        if cidade_input:
            resultado = service.obter_previsao(cidade_input)
            if resultado:
                print(f"\n📍 Clima em {resultado['cidade']}:")
                print(f"🌡️ Temperatura: {resultado['temperatura']}°C")
                print(f"☁️ Condição: {resultado['condicao']}")
                print(f"💧 Umidade: {resultado['umidade']}%")
            else:
                print("Não foi possível carregar as informações.")
        else:
            print("Por favor, insira o nome de uma cidade.")
            
    except ValueError as e:
        print(e)