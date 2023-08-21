# Baixe as dependencias do programa com o comando:
# pip install -r requirements.txt

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

from tkinter import *
from tkinter import ttk


c = 0
navegador = None

def baixar(nome, rb1, rb2, rb3, bt_enviar, link):

    global c, navegador

    print(link.get())

    if link.get() != '':

        bt_enviar.configure(state=DISABLED)

        if c == 0:

            rb1.configure(state=DISABLED)
            rb2.configure(state=DISABLED)
            rb3.configure(state=DISABLED)

            default_browser = nome

            if default_browser == 'chrome':
                options = OptionsCR()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                service = ServiceCR(ChromeDriverManager().install())
                navegador = webdriver.Chrome(service=service, options=options)

            elif default_browser == 'firefox':
                options = OptionsFX()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                service = ServiceFX(GeckoDriverManager().install())
                navegador = webdriver.Firefox(service=service, options=options)

            elif default_browser == 'edge':
                options = OptionsED()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                service = ServiceED(EdgeChromiumDriverManager().install())
                navegador = webdriver.Edge(service=service, options=options)

            else:
                pass

            navegador.get('https://pt1.savefrom.net/59/')   
        c = 1

        navegador.get('https://pt1.savefrom.net/59/')
        url_video = link.get()

        while True:
            try:
                navegador.find_element('xpath', '//*[@id="sf_url"]').send_keys(url_video)
            except:
                pass
            else:
                break

        while True:
            try:
                navegador.find_element('xpath', '//*[@id="sf_submit"]').click()
            except:
                pass
            else:
                break

        print('Procurando o vídeo...')

        while True:
            try:
                linkDown = navegador.find_element('xpath', '//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
            except:
                pass
            else:
                print('Vídeo encontrado')
                break

        titulo = navegador.find_element('xpath', '//*[@id="sf_result"]/div/div[1]/div[2]/div[1]/div[1]')
        titulo = titulo.get_attribute('title')

        print('Baixando vídeo...')

        r = requests.get(linkDown.get_attribute('href'))
        with open(f'{titulo}.mp4', 'wb') as file:
            file.write(r.content)

        print('Video baixado!!!\n')

        bt_enviar.configure(state=NORMAL)
        link.delete(0, END)



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Incio da janela
root = Tk()

#Estilo da janela
style = ttk.Style()
style.theme_use("xpnative")
print(style.theme_names())


#Texto nome app
Label(root,text='Baixador e conversor de vídeo').pack()
Label(root,text='informe um link abaixo').pack()

#Campo de inserir o link
link = ttk.Entry(root, width=95)
link.pack(pady=5)


#Texto informar o navegador
txt = Label(text='Informe qual seu navegador padrão')
txt.pack(pady=5)

#Frame dos RadioButton
frame = Frame(root) ; frame.pack()
selecao = StringVar(value='edge')
rb1 = ttk.Radiobutton(frame, text='chrome', variable=selecao, value='chrome') ; rb1.grid(column=1,row=0)
rb2 = ttk.Radiobutton(frame, text='firefox', variable=selecao, value='firefox') ; rb2.grid(column=2,row=0)
rb3 = ttk.Radiobutton(frame, text='edge', variable=selecao, value='edge') ; rb3.grid(column=3,row=0)

#Botão baixar
bt = ttk.Button(text='baixar', command=lambda: baixar(selecao.get(), rb1, rb2, rb3, bt, link))
bt.pack(pady=5)


#Textos informativos
textoInfo = Label(root, text='Obs: Na primeira vez usando ao abrir o app, ele irá parar de responder até carregar os recursos, ainda vou otimizar isso :)')
textoInfo.pack()
Label(root,text='Feito por Hono. V0.1').pack()


#Loop da janela
root.mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
