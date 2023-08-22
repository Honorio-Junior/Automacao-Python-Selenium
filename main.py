from tkinter import *
from tkinter import ttk
from threading import Thread
from time import sleep




def baixar(browser, link):
    print(browser, link)
    sleep(2)


def click(browser, rb1, rb2, rb3, bt_enviar, link):

    bt_enviar.configure(state=DISABLED)
    rb1.configure(state=DISABLED);rb2.configure(state=DISABLED);rb3.configure(state=DISABLED)
    thr = Thread(target=lambda: baixar(browser, link))
    thr.start()
    #bt_enviar.configure(state=NORMAL)







#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Incio da janela
root = Tk()

#Estilo da janela
style = ttk.Style()
style.theme_use("xpnative")
print(style.theme_names())


#Texto nome app
Label(root,text='Baixar vídeo').pack()
Label(root,text='informe um link abaixo').pack()

#Campo de inserir o link
link = ttk.Entry(root, width=90)
link.pack(pady=5, padx=5)


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
bt = ttk.Button(text='baixar', command=lambda: click(selecao.get(), rb1, rb2, rb3, bt, link.get()))
bt.pack(pady=5)


#Loop da janela
root.mainloop()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
