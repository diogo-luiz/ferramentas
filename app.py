import requests
import time


def monitor_api(url, interval=60):
    response = requests.get(url)
    
    while True:
        try:
            start_time = time.time()
            response_time = time.time() - start_time

            if response.status_code == 200:
                print(f"API disponível - tempo de resposta {response_time:.2f}s")
            else:
                print(f"Erro - status code {response.status_code}")
        except Exception as e:
            print(f"Falha na conexão: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_api("http://www.google.com/teste1")