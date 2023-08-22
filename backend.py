from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ServiceCR
from selenium.webdriver.chrome.options import Options as OptionsCR

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as ServiceED
from selenium.webdriver.edge.options import Options as OptionsED

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as ServiceFX
from selenium.webdriver.firefox.options import Options as OptionsFX

import requests
from time import sleep

class Automacao():

    def __init__(self):
        pass

    def set_browser(self, browser):
        try:
            self.close()
        except:
            pass
        try:
            if browser == 'chrome':
                options = OptionsCR()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                service = ServiceCR(ChromeDriverManager().install())
                self.navegador = webdriver.Chrome(service=service, options=options)

            elif browser == 'firefox':
                options = OptionsFX()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                service = ServiceFX(GeckoDriverManager().install())
                self.navegador = webdriver.Firefox(service=service, options=options)

            elif browser == 'edge':
                options = OptionsED()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                service = ServiceED(EdgeChromiumDriverManager().install())
                self.navegador = webdriver.Edge(service=service, options=options)
        except Exception as e:
            print(e)

    def close(self):
        try:
            self.navegador.quit()
        except Exception as e:
            print(e)

    def savefrom(self, link):

        self.navegador.get('https://pt1.savefrom.net/59/')
        url_video = link

        # insere o link do video
        print('insere o link do video')
        while True:
            try:
                self.navegador.find_element('xpath', '//*[@id="sf_url"]').send_keys(url_video)
            except:
                sleep(0.5)
            else:
                break

        # clicka em procurar o link do video
        print('clicka em procurar o link do video')
        while True:
            try:
                self.navegador.find_element('xpath', '//*[@id="sf_submit"]').click()
            except:
                sleep(0.5)
            else:
                break

        # Procura o link de download
        print('Procura o link de download')
        while True:
            try:
                linkDown = self.navegador.find_element('xpath', '//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
                linkDown = linkDown.get_attribute('href')
            except:
                sleep(0.5)
            else:
                print('Vídeo encontrado')
                break

        # Procura e salva o título do vídeo
        print('Procura e salva o título do vídeo')
        while True:
            try:
                titulo = self.navegador.find_element('xpath', '//*[@id="sf_result"]/div/div[1]/div[2]/div[1]/div[1]')
                titulo = titulo.get_attribute('title')
            except:
                pass
            else:
                print('Titulo encontrando')
                break

        return linkDown, titulo

    def baixar(self, servico, link):
        try:
            if servico == 'savefrom':
                linkDown, titulo = self.savefrom(link)
                pass

            r = requests.get(linkDown)
            with open(f'{titulo}.mp4', 'wb') as file:
                file.write(r.content)

            print('Video baixado!!!\n')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    print("oi")
