from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
from time import sleep
from pytube import YouTube
from pytube import Playlist
import datetime
import calendar

import requests
from tkinter import font
from tkinter import messagebox
import  customtkinter
import os
from tkinter.ttk import Progressbar

janela = Tk()
janela.config(bg='white')
janela.geometry("650x400")
janela.title("Download")
janela.resizable(width=False,height=False)
cont_mp3 = []
cont_mp4_hd = []
cont_mp4_sd = []
frame3 = Frame(janela,bg='red')
bar = Progressbar(frame3, length=190, style='black.Horizontal.TProgressbar')

def mp3():
    frame3.place_forget()
    bar.place_forget()
    status.place_forget()

    link = teste
    url = YouTube(link)
    os.chdir(os.path.join(os.path.expanduser('~'), 'desktop'))
    ys = url.streams.get_audio_only()
    arquivo = ys.download()
    base, ext = os.path.splitext(arquivo)
    novoarquivo = base + '.mp3'

    try:
        os.rename(arquivo, novoarquivo)
    except:
        cont_mp3.append(1)
        print(sum(cont_mp3))
        novoarquivo = base + f' {sum(cont_mp3)}' + '.mp3'
        os.rename(arquivo, novoarquivo)

    #e_url.delete(0, 'end')




def hd():

    link = entra.get()
    url = YouTube(link)
    ys = url.streams.get_highest_resolution()
    ys.download()


def playlist():
    link = str(entra.get())
    yt = Playlist(link)
    for url in yt.video_urls:
        ys = YouTube(url)
        v = ys.streams.get_highest_resolution()
        v.download()
def pesquisar(event=None):
    cont_mp4_hd.clear()
    cont_mp4_sd.clear()
    cont_mp3.clear()

    global teste
    teste = entra.get()
    status['text']=" "
    if (entra.get()==""):
        messagebox.showinfo("Status", "Campo Vazio")
    else:
        global img
        frame3.place_forget()
        yt = YouTube(entra.get())

        
        titulo=yt.title
        l_titulob['text'] = titulo
        #visualizações
        #view = yt.views
        #l_viewsb['text'] = (f"Views: {view:,.0f}")
        #Duração do video
        duracao = str(datetime.timedelta(seconds=yt.length))
        l_timeb['text'] = "Duração: "+ duracao
        #Imagem do video
        foto = yt.thumbnail_url
        img = Image.open(requests.get(foto, stream=True).raw)
        img = img.resize((375,210), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        l_imagemb['image'] = img

app_nome = Label(janela,text="Youtube vídeo downloader",bg="white",fg="#1F2024",font=("Calibri 14 bold"))
app_nome.place(x=180,y=38)

lin=customtkinter.CTkLabel(janela,text_color="black",text="@Emaricar progrmmer",height=0,corner_radius=1)
lin.place(x=510,y=10)

entra=customtkinter.CTkEntry(master=janela,height=30,width=400,relief="flat",border_width=1,corner_radius=2,placeholder_text="Insira a url aqui")
entra.place(x=60,y=100)
procurar= customtkinter.CTkButton(master=janela,command=pesquisar,fg_color="#DD171E",hover_color="#BC171E",text_color="white",text="Procurar Vídeo",width=110,height=35,border_width=0,corner_radius=5,relief="flat",highlightthickness=0)
procurar.place(x=470,y=96)

bt= customtkinter.CTkButton(master=janela,fg_color="#DD171E",command=hd,hover_color="#BC171E",text_color="white",text="Download Video MP4",width=145,height=35,border_width=0,corner_radius=5,relief="flat",highlightthickness=0)
bt.place(x=450,y=170)
bt1= customtkinter.CTkButton(master=janela,command=playlist,fg_color="#DD171E",hover_color="#BC171E",text_color="white",text="Download Playlist MP4",width=110,height=35,border_width=0,corner_radius=5,relief="flat",highlightthickness=0)
bt1.place(x=450,y=310)
bt3= customtkinter.CTkButton(master=janela,fg_color="#DD171E",hover_color="#BC171E",text_color="white",command=mp3,text="Download Vídeo MP3",width=150,height=35,border_width=0,corner_radius=5,relief="flat",highlightthickness=0)
bt3.place(x=450,y=240)




l_imagemb = Label(janela, image="", bg="white",compound=LEFT,font=('Ivy 10 bold'), anchor='nw')
l_imagemb.place(x=60, y=150)

l_titulob = Label(janela, text="", height=2, wraplength=355, compound=LEFT, bg="white", fg="black", font=('Ivy 10 bold'),
                  anchor='nw')
l_titulob.place(x=80, y=0)

# l_viewsb = Label(frame_baixo, text="", bg=fundo, fg=co1 ,font=('Ivy 8 bold'), anchor='nw')
# l_viewsb.place(x=10,y=340)

l_timeb = Label(janela, text="", bg="white", fg="black", font=('Ivy 8 bold'), anchor='nw')
l_timeb.place(x=80, y=370)



status = Label(janela, text="", font=('Arial Black', 10), bg="white", fg="black")
status.place(x=0)




logo = Image.open('p.png')
logo = logo.resize((70,70), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

l_logo = Label(janela, image=logo, compound=LEFT, bg='white', font=('Ivy 10 bold'), anchor='nw')
l_logo.place(x=50,y=20)













janela.bind('<Return>', pesquisar)

janela.mainloop()
