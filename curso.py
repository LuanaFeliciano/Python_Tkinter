
from cProfile import label
from cgitb import text
from distutils.util import copydir_run_2to3
import email
from email import message
from logging import root
from tkinter import *
from tkinter import Tk, ttk
from tkinter import font
from tkinter import messagebox
from tkinter.tix import Tree
import webbrowser

#cores-------
cor0 = "#fce6f7"#janela
cor1 = "#faf7f9"
cor2 = "#bd55a3"
cor3 = "#38576b"
cor4 = "#403d3d"
#criando a janela

win_width, win_height =400,310
janela=Tk()
janela.title('1234')
janela.geometry('400x310')
janela.configure(background=cor0)
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='logo.png'))
img=PhotoImage(file="logo.png")

#dividindo janela
framecima = Frame(janela, width=410, height=50, bg=cor1, relief='flat')
framecima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

framebaixo = Frame(janela, width=410, height=250, bg=cor0, relief='flat')
framebaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurando o framecima
labellogin = Label(framecima, text='Bem Vindo!', anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
labellogin.place(x=5, y=5)
#linha
labellinha = Label(framecima, text='',width=375, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
labellinha.place(x=10, y=45)

credenciais = ['Luana', '18', '1234']
def verificar_senha():
    nome=enternome.get()
    idade=enteridade.get()
    senha=entersenha.get()

    if credenciais[0]==nome and credenciais[1]==idade and credenciais[2]==senha:
        messagebox.showinfo('Logar', 'Você Acertou')
        #deletar tudo pra aparecer a nova janela
        for widget in framebaixo.winfo_children():
            widget.destroy()

        for widget in framecima.winfo_children():
            widget.destroy()
        nova_janela()

    else:
        messagebox.showwarning('Erro','Alguma coisa está errada')

def janelahabilidades():
        for widget in framebaixo.winfo_children():
            widget.destroy()

        for widget in framecima.winfo_children():
            widget.destroy()
        Habilidades()
def janelacontatos():
        for widget in framebaixo.winfo_children():
            widget.destroy()

        for widget in framecima.winfo_children():
            widget.destroy()
        Contatos()
def grupos():
        for widget in framebaixo.winfo_children():
            widget.destroy()

        for widget in framecima.winfo_children():
            widget.destroy()
        janela_grupos()
def final():
        for widget in framebaixo.winfo_children():
            widget.destroy()

        for widget in framecima.winfo_children():
            widget.destroy()
        janela_final() 
def janela_quit():
    janela.destroy()          

def nova_janela():
    labelLUANA = Label(framecima, text='Sobre Mim', anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
    labelLUANA.place(x=5, y=5)

    labellinha = Label(framecima, text='',width=375, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
    labellinha.place(x=10, y=45)  
#frame baixo
    labelLUANA = Label(framebaixo,wraplength=win_width, text='Oi! Meu nome é Luana,tenho 18 anos de idade, sou da cidade de Marília e estudo Análise e Desenvolvimento de Sistemas na UNIMAR. Tenho muita vontade de aprender, buscar conhecimento e experiência na área de tecnologia. Sou uma pessoa muito dedicada nos estudos ainda mais envolvendo programação :D ', font=('Ivy 13 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=10)

    #botao da foto
    botao = Button(framebaixo,command=janelahabilidades, text='Minhas Habilidades',width=45,height=3, font=('Ivy 7 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
    botao.place(x=50, y=200)

def Habilidades():
    labelhab = Label(framecima, text='Habilidades', anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
    labelhab.place(x=5, y=5)

    labellinha = Label(framecima, text='',width=375, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
    labellinha.place(x=10, y=45)

    labelLUANA = Label(framebaixo,wraplength=win_width, text='1-Capacidade de Autoaprendizagem', font=('Ivy 10 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=10)
    
    labelLUANA = Label(framebaixo,anchor=NW, text='2-Conhecimento Básico em Programação', font=('Ivy 10 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=60)

    labelLUANA = Label(framebaixo,anchor=NW, text='3-Capacidade de Trabalhar em Equipe', font=('Ivy 10 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=110)

    labelLUANA = Label(framebaixo,anchor=NW, text='3-Capacidade de Trabalhar em Equipe', font=('Ivy 10 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=110)

    labelLUANA = Label(framebaixo,anchor=NW, text='4-Inglês Intermediário', font=('Ivy 10 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=160)

    botao = Button(framebaixo,command=grupos, text='Grupos que estou participando',width=45,height=3, font=('Ivy 7 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
    botao.place(x=50, y=195)

def Contatos():
    labelcont = Label(framecima, text='Entre em Contato', anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
    labelcont.place(x=5, y=5)

    labellinha = Label(framecima, text='',width=375, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
    labellinha.place(x=10, y=45)

    labelLUANA = Label(framebaixo,wraplength=win_width, text='Telefone celular  +55 (14)99857-3623', font=('Ivy 13 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=10)

    labelLUANA = Label(framebaixo,anchor=NW, text='E-mail luanagomesfeliciano@gmail.com', font=('Ivy 13 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=60)

    labelLUANA = Label(framebaixo,anchor=NW, text='Linkedin  https://www.linkedin.com/in/luana-feliciano/', font=('Ivy 11 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=110)

    labelLUANA = Label(framebaixo,anchor=NW, text='Github https://github.com/LuanaFeliciano', font=('Ivy 12 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=160)

    botao = Button(framebaixo,command=final,text='FINAL',width=40,height=2, font=('Ivy 9 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
    botao.place(x=50, y=195)

def janela_grupos():
    labelcont = Label(framecima, text='Grupos', anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
    labelcont.place(x=5, y=5)

    labellinha = Label(framecima, text='',width=375, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
    labellinha.place(x=10, y=45)

    labelLUANA = Label(framebaixo,wraplength=win_width, text='1. Grupo de Projetos Científicos, Tecnológicos e Empreendedores - LPTech', font=('Ivy 13 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=10)

    labelLUANA = Label(framebaixo,anchor=NW,wraplength=win_width, text='2. Grupo de treinamento para Maratona de Programação', font=('Ivy 13 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=110)

    botao = Button(framebaixo,command=janelacontatos, text='Contatos',width=40,height=2, font=('Ivy 8 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
    botao.place(x=50, y=195)
def janela_final():
    labelcont = Label(framecima, text='FINAL', anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
    labelcont.place(x=5, y=5)

    labellinha = Label(framecima, text='',width=375, anchor=NW, font=('Ivy 1'), bg=cor2, fg=cor4)
    labellinha.place(x=10, y=45)

    labelLUANA = Label(framebaixo,wraplength=win_width, text='OBRIGADA POR CHEGAR ATÉ AQUI!', font=('Ivy 15 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=10)

    labelLUANA = Label(framebaixo,anchor=NW,wraplength=win_width, text='Este projeto foi feito para o meu aprendizado de Python, decidi fazer no Python Tkinter para ficar mais divertido de interagir, espero que tenha gostado :D  Se quiser ver mais projetos meus aperte o botão Github e veja meu Github ou aperte Linkedin e veja meu Linkedin!' , font=('Ivy 10 bold'), bg=cor0, fg=cor4)
    labelLUANA.place(x=5, y=45)

    botao = Button(framebaixo, text='Github',command=lambda: webbrowser.open('https://github.com/LuanaFeliciano'),width=45,height=2, font=('Ivy 7 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
    botao.place(x=50, y=140)

    botao = Button(framebaixo, text='Linkedin',command=lambda: webbrowser.open('https://www.linkedin.com/in/luana-feliciano/'),width=45,height=2, font=('Ivy 7 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
    botao.place(x=50, y=180)

    botao = Button(framebaixo,command=janela_quit ,text='Fechar Janela',width=45,height=2, font=('Ivy 7 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
    botao.place(x=50, y=220)




#configurando o frame baixo
labelnome = Label(framebaixo, text='Acerte meu Nome', anchor=NW, font=('Ivy 10'), bg=cor0, fg=cor4)
labelnome.place(x=45, y=5)

enternome = Entry(framebaixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
enternome.place(x=50, y=25)

labelemail = Label(framebaixo, text='Acerte minha Idade', anchor=NW, font=('Ivy 10'), bg=cor0, fg=cor4)
labelemail.place(x=45, y=65)
#digitar o email
enteridade = Entry(framebaixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
enteridade.place(x=50, y=85)
#senha
labelsenha = Label(framebaixo, text='Ache a Senha na Janela', anchor=NW, font=('Ivy 10'), bg=cor0, fg=cor4)
labelsenha.place(x=45, y=123)
#digitar a senha
entersenha = Entry(framebaixo,show="*", width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
entersenha.place(x=50, y=143)
#botao de confirmar
botao = Button(framebaixo,command=verificar_senha, text='LOGAR',width=45,height=2, font=('Ivy 7 bold'), bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
botao.place(x=50, y=195)





janela.mainloop()
