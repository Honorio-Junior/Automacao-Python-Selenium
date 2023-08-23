from tkinter import *
from tkinter import ttk
from threading import Thread
from time import sleep
import backend



browser_select = ''
selenium = backend.Automacao()

def baixar(browser, link, bt_baixar, rb1,rb2,rb3):
    global browser_select
    url = link.get()

    link.delete(0, END)
    if browser_select != browser:
        link.insert(0, 'Iniciando serviço... Esse processo só ocorre uma vez por navegador!')
        selenium.set_browser(browser)
    
    link.delete(0, END)
    if url != '' and browser != '' and not(' ' in url):
        link.insert(0, 'Baixando o vídeo... Aguarde')
        selenium.baixar('savefrom', url)
        link.delete(0, END)
        link.insert(0, 'Concluído!!!')
        sleep(0.5)
    else:
        link.delete(0, END)
        link.insert(0, 'Informe um LINK e um NAVEGADOR!')
        sleep(1)

    browser_select = browser
    link.delete(0, END)
    bt_baixar.configure(state=NORMAL)
    rb1.configure(state=NORMAL) ; rb2.configure(state=NORMAL) ; rb3.configure(state=NORMAL)



def click(browser, bt_baixar, link, rb1,rb2,rb3):
    bt_baixar.configure(state=DISABLED)
    rb1.configure(state=DISABLED) ; rb2.configure(state=DISABLED) ; rb3.configure(state=DISABLED)
    thr = Thread(target=lambda: baixar(browser, link, bt_baixar, rb1,rb2,rb3)).start()
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Incio da janela
root = Tk()

#Estilo da janela
style = ttk.Style()
style.theme_use("xpnative")
print(style.theme_names())

#Texto informar o navegador
txt = Label(text='ATENÇÃO! Informe seu navegador')
txt.pack(pady=5)

#Frame dos RadioButton
frame = Frame(root) ; frame.pack()
selecao = StringVar(value='')
rb1 = ttk.Radiobutton(frame, text='chrome', variable=selecao, value='chrome') ; rb1.grid(column=1,row=0)
rb2 = ttk.Radiobutton(frame, text='firefox', variable=selecao, value='firefox') ; rb2.grid(column=2,row=0)
rb3 = ttk.Radiobutton(frame, text='edge', variable=selecao, value='edge') ; rb3.grid(column=3,row=0)

#Texto nome app
Label(root,text='Informe o link do vídeo: (instagram, youtube, twitter, facebook)').pack()

#Campo de inserir o link
link = ttk.Entry(root, width=80)
link.pack(pady=5, padx=10)

#Botão baixar
bt_baixar = ttk.Button(text='baixar', width=80, command=lambda: click(selecao.get(), bt_baixar, link, rb1, rb2, rb3))
bt_baixar.pack(pady=5)

#Loop da janela
root.mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
selenium.close()
