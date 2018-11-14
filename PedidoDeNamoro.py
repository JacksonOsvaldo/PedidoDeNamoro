import tkinter as tk
from tkinter import *
from tkinter import messagebox as msb

janela = tk.Tk()

def Sim():
    sim = msb.askquestion(title="Operação concluida", message='Ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh <3 Nos vemos amanhã?')
    if sim == 'yes':
        msb.showinfo(title=":)", message='Cedinho estarei aí.')
    else:
        msb.showinfo(title=":)", message='Tudo bem então... :(')
    return sim

def Nao():
    nao = msb.askquestion(title="Operação concluida", message='Tem certeza?')
    if nao == 'no':
        msb.showinfo(title=":)", message='Te convecerei do contrário. Que tal um açaí no final de semana?')
    else:
        msb.showinfo(title=":)", message='Tudo bem... Ainda assim, você é a mulher mais linda que tive a oportunidade de conhecer. Nunca te esquecerei.')
    return nao

def sair():
    msb.showinfo(title=":)", message='Até a próxima...')
    janela.destroy()

label = tk.Label(janela, text="Quer namorar comigo?", font='54')
label.pack()

btn1 = tk.Button(janela,text="Sim", font='42', command=Sim)
btn1.pack()

btn2 = tk.Button(janela,text="Não", font='42', command=Nao)
btn2.pack()

button = tk.Button(janela,text="Sair", font='42', command=sair)
button.pack()

janela.title('Mensagem')
janela.geometry('400x150')
janela.mainloop()
