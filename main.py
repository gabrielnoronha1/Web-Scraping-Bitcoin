import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_crypto_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Executa o navegador em modo headless (sem abrir a janela)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Acessa o primeiro site e captura o valor
        driver.get("https://alternative.me/crypto/fear-and-greed-index/")
        time.sleep(3)
        fear_and_greed_value = driver.find_element(By.CLASS_NAME, "fng-circle").text
        print(f"Fear and Greed Index: {fear_and_greed_value}")

        # Acessa o segundo site e captura o valor
        driver.get("https://colintalkscrypto.com/cbbi/")
        time.sleep(3)
        cbbi_value = driver.find_element(By.CLASS_NAME, "confidence-score-value").text
        print(f"CBBI Index: {cbbi_value}")

    finally:
        driver.quit()

# Agendar para executar todos os dias às 21:01
schedule.every().day.at("21:01").do(get_crypto_data)

# Loop para manter o código rodando e verificando o agendamento
while True:
    schedule.run_pending()
    time.sleep(60)  # Espera um minuto antes de verificar novamente