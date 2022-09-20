from tkinter import filedialog
import tweepy
import Datos
from tkinter import *

client = tweepy.Client(bearer_token=Datos.bearer_token, 
                       consumer_key=Datos.consumer_key, 
                       consumer_secret=Datos.consumer_secret, 
                       access_token=Datos.access_token, 
                       access_token_secret=Datos.access_token_secret)

auth = tweepy.OAuthHandler(Datos.consumer_key, Datos.consumer_secret)
auth.set_access_token(Datos.access_token, Datos.access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth)
    

def TwitSimple():

    def Exit():
        miFrame2.pack_forget()
        miFrame.pack()
        return

    def TwitFancy():

        def restart():
            miFrame3.pack_forget()
            miFrame2.pack()
            cuadroTexto1.delete("1.0",END)
            return

        Twit = cuadroTexto1.get("1.0","end-1c")
        client.create_tweet(text=Twit)

        miFrame3=Frame()
        miFrame3.pack()
        miFrame3.config(bg='Blue')
        miFrame3.config(width="650",height="350")
        miFrame2.pack_forget()

        Lable1=Label(miFrame3, text="Éxito")
        Lable1.place(x=275,y=100)
        Lable1.config(bg='Light Blue',fg="Blue",font=("Arial",34),relief='raised')

        start=Button(miFrame3, text="Escribir Otro Twit",command=restart)
        start.place(x=230,y=200)
        start.config(bg='Light Gray',fg="Blue",font=("Arial",18),relief='raised')

    miFrame2=Frame()
    miFrame2.pack()
    miFrame2.config(bg='Blue')
    miFrame2.config(width="650",height="350")
    miFrame.pack_forget()


    #Crea el título
    Title=Label(miFrame2, text="Twitter Python Interface")
    Title.place(x=190,y=10)
    Title.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    #Crea las entradas
    Lable1=Label(miFrame2, text="Escribe el twit")
    Lable1.place(x=10,y=80)
    Lable1.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    #Crea los cuadros de texto para introducir las playlists
    cuadroTexto1=Text(miFrame2)
    cuadroTexto1.place(x=10,y=130)
    cuadroTexto1.config(width="78",height='7')

    #Crea el botón de Empezar
    start=Button(miFrame2, text="Twittear",command=TwitFancy)
    start.place(x=230,y=260)
    start.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    exit=Button(miFrame2, text="Exit",command=Exit)
    exit.place(x=350,y=260)
    exit.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    #Copyright
    copy=Label(miFrame2, text="Copyright 2022 Diego Cuenca Prieto, created using python, tweepy and tkinter. All rights reserved.")
    copy.place(x=10,y=320)
    copy.config(bg="Blue")

def TwitRespuesta():
    def Exit():
        miFrame2.pack_forget()
        miFrame.pack()
        return

    def TwitFancy():

        def restart():
            miFrame3.pack_forget()
            miFrame2.pack()
            cuadroTexto1.delete("1.0",END)
            cuadroTexto2.delete("1.0",END)
            return

        Twit = cuadroTexto1.get("1.0","end-1c")
        ID = cuadroTexto2.get("1.0","end-1c")
        client.create_tweet(text=Twit,in_reply_to_tweet_id=ID)

        miFrame3=Frame()
        miFrame3.pack()
        miFrame3.config(bg='Blue')
        miFrame3.config(width="650",height="350")
        miFrame2.pack_forget()

        Lable1=Label(miFrame3, text="Éxito")
        Lable1.place(x=275,y=100)
        Lable1.config(bg='Light Blue',fg="Blue",font=("Arial",34),relief='raised')

        start=Button(miFrame3, text="Escribir Otro Twit",command=restart)
        start.place(x=230,y=200)
        start.config(bg='Light Gray',fg="Blue",font=("Arial",18),relief='raised')

    miFrame2=Frame()
    miFrame2.pack()
    miFrame2.config(bg='Blue')
    miFrame2.config(width="650",height="350")
    miFrame.pack_forget()


    #Crea el título
    Title=Label(miFrame2, text="Twitter Python Interface")
    Title.place(x=190,y=10)
    Title.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    #Crea las entradas
    Lable1=Label(miFrame2, text="Escribe el twit")
    Lable1.place(x=10,y=50)
    Lable1.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    Lable2=Label(miFrame2, text="ID Respuesta")
    Lable2.place(x=10,y=220)
    Lable2.config(bg='Light Blue',fg="black",font=("Arial",10),relief='raised')
    Lable2.config(width="15")

    #Crea los cuadros de texto para introducir las playlists
    cuadroTexto1=Text(miFrame2)
    cuadroTexto1.place(x=10,y=90)
    cuadroTexto1.config(width="78",height='7')

    cuadroTexto2=Text(miFrame2)
    cuadroTexto2.place(x=140,y=220)
    cuadroTexto2.config(width="62",height='1.45')

    #Crea el botón de Empezar
    start=Button(miFrame2, text="Twittear",command=TwitFancy)
    start.place(x=230,y=260)
    start.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    exit=Button(miFrame2, text="Exit",command=Exit)
    exit.place(x=350,y=260)
    exit.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    #Copyright
    copy=Label(miFrame2, text="Copyright 2022 Diego Cuenca Prieto, created using python, tweepy and tkinter. All rights reserved.")
    copy.place(x=10,y=320)
    copy.config(bg="Blue")

def TwitMedia():
    def BrowseFile():
        cuadroTexto2.delete("1.0",END)
        filename = filedialog.askopenfile(initialdir="..",title="Elige un Archivo")
        cuadroTexto2.insert(INSERT,filename.name)

    def Exit():
        miFrame2.pack_forget()
        miFrame.pack()
        return

    def TwitFancy():

        def restart():
            miFrame3.pack_forget()
            miFrame2.pack()
            cuadroTexto1.delete("1.0",END)
            cuadroTexto2.delete("1.0",END)
            return

        Twit = cuadroTexto1.get("1.0","end-1c")
        media = cuadroTexto2.get("1.0","end-1c")
        id_media = [api.media_upload(media).media_id]
        client.create_tweet(text=Twit,media_ids=id_media)

        miFrame3=Frame()
        miFrame3.pack()
        miFrame3.config(bg='Blue')
        miFrame3.config(width="650",height="350")
        miFrame2.pack_forget()

        Lable1=Label(miFrame3, text="Éxito")
        Lable1.place(x=275,y=100)
        Lable1.config(bg='Light Blue',fg="Blue",font=("Arial",34),relief='raised')

        start=Button(miFrame3, text="Escribir Otro Twit",command=restart)
        start.place(x=230,y=200)
        start.config(bg='Light Gray',fg="Blue",font=("Arial",18),relief='raised')

    miFrame2=Frame()
    miFrame2.pack()
    miFrame2.config(bg='Blue')
    miFrame2.config(width="650",height="350")
    miFrame.pack_forget()


    #Crea el título
    Title=Label(miFrame2, text="Twitter Python Interface")
    Title.place(x=190,y=10)
    Title.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    #Crea las entradas
    Lable1=Label(miFrame2, text="Escribe el twit")
    Lable1.place(x=10,y=50)
    Lable1.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    browser=Button(miFrame2, text="Explorar Archivos",command=BrowseFile)
    browser.place(x=10,y=220)
    browser.config(bg='Light Blue',fg="black",font=("Arial",10),relief='raised')
    browser.config(width="15")

    #Crea los cuadros de texto para introducir las playlists
    cuadroTexto1=Text(miFrame2)
    cuadroTexto1.place(x=10,y=90)
    cuadroTexto1.config(width="78",height='7')

    cuadroTexto2=Text(miFrame2)
    cuadroTexto2.place(x=140,y=220)
    cuadroTexto2.config(width="62",height='1.45')

    #Crea el botón de Empezar
    start=Button(miFrame2, text="Twittear",command=TwitFancy)
    start.place(x=230,y=260)
    start.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    exit=Button(miFrame2, text="Exit",command=Exit)
    exit.place(x=350,y=260)
    exit.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    #Copyright
    copy=Label(miFrame2, text="Copyright 2022 Diego Cuenca Prieto, created using python, tweepy and tkinter. All rights reserved.")
    copy.place(x=10,y=320)
    copy.config(bg="Blue")

def TwitMediaRespuesta():
    def BrowseFile():
        cuadroTexto2.delete("1.0",END)
        filename = filedialog.askopenfile(initialdir="..",title="Elige un Archivo")
        cuadroTexto2.insert(INSERT,filename.name)

    def Exit():
        miFrame2.pack_forget()
        miFrame.pack()
        return

    def TwitFancy():

        def restart():
            miFrame3.pack_forget()
            miFrame2.pack()
            cuadroTexto1.delete("1.0",END)
            cuadroTexto2.delete("1.0",END)
            cuadroTexto3.delete("1.0",END)
            return

        Twit = cuadroTexto1.get("1.0","end-1c")
        media = cuadroTexto2.get("1.0","end-1c")
        ID = cuadroTexto3.get("1.0","end-1c")
        id_media = [api.media_upload(media).media_id]
        client.create_tweet(text=Twit,media_ids=id_media,in_reply_to_tweet_id=ID)

        miFrame3=Frame()
        miFrame3.pack()
        miFrame3.config(bg='Blue')
        miFrame3.config(width="650",height="350")
        miFrame2.pack_forget()

        Lable1=Label(miFrame3, text="Éxito")
        Lable1.place(x=275,y=100)
        Lable1.config(bg='Light Blue',fg="Blue",font=("Arial",34),relief='raised')

        start=Button(miFrame3, text="Escribir Otro Twit",command=restart)
        start.place(x=230,y=200)
        start.config(bg='Light Gray',fg="Blue",font=("Arial",18),relief='raised')

    miFrame2=Frame()
    miFrame2.pack()
    miFrame2.config(bg='Blue')
    miFrame2.config(width="650",height="350")
    miFrame.pack_forget()


    #Crea el título
    Title=Label(miFrame2, text="Twitter Python Interface")
    Title.place(x=190,y=10)
    Title.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    #Crea las entradas
    Lable1=Label(miFrame2, text="Escribe el twit")
    Lable1.place(x=10,y=50)
    Lable1.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

    browser=Button(miFrame2, text="Explorar Archivos",command=BrowseFile)
    browser.place(x=10,y=215)
    browser.config(bg='Light Blue',fg="black",font=("Arial",10),relief='raised')
    browser.config(width="14",)

    Lable2=Label(miFrame2, text="Twit ID")
    Lable2.place(x=10,y=250)
    Lable2.config(bg='Light Blue',fg="black",font=("Arial",10),relief='raised')
    Lable2.config(width="15")

    #Crea los cuadros de texto para introducir las playlists
    cuadroTexto1=Text(miFrame2)
    cuadroTexto1.place(x=10,y=90)
    cuadroTexto1.config(width="78",height='7')

    cuadroTexto2=Text(miFrame2)
    cuadroTexto2.place(x=140,y=215)
    cuadroTexto2.config(width="62",height='1')

    cuadroTexto3=Text(miFrame2)
    cuadroTexto3.place(x=140,y=250)
    cuadroTexto3.config(width="62",height='1.45')

    #Crea el botón de Empezar
    start=Button(miFrame2, text="Twittear",command=TwitFancy)
    start.place(x=230,y=280)
    start.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    exit=Button(miFrame2, text="Exit",command=Exit)
    exit.place(x=350,y=280)
    exit.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

    #Copyright
    copy=Label(miFrame2, text="Copyright 2022 Diego Cuenca Prieto, created using python, tweepy and tkinter. All rights reserved.")
    copy.place(x=10,y=330)
    copy.config(bg="Blue")


#Main Screen
raiz=Tk()
raiz.title("Twitter Python Interface")
raiz.config(bg="Blue")
raiz.resizable(0,0)
raiz.iconbitmap("Twitter.ico")

#Crea el frame
miFrame=Frame()
miFrame.pack()
miFrame.config(bg='Blue')
miFrame.config(width="650",height="350")

#Crea el título
Title=Label(miFrame, text="Twitter Python Interface")
Title.place(x=190,y=10)
Title.config(bg='Light Blue',fg="black",font=("Arial",18),relief='raised')

#Crea el botón de Empezar
Simple=Button(miFrame, text="Twit Simple",command=TwitSimple)
Simple.place(x=50,y=100)
Simple.config(width="18")
Simple.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

Respuesta=Button(miFrame, text="Twit Respuesta",command=TwitRespuesta)
Respuesta.place(x=50,y=200)
Respuesta.config(width="18")
Respuesta.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

Media=Button(miFrame, text="Twit Media",command=TwitMedia)
Media.place(x=320,y=100)
Media.config(width="18")
Media.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

MediaRespuesta=Button(miFrame, text="Twit Media Respuesta",command=TwitMediaRespuesta)
MediaRespuesta.place(x=320,y=200)
MediaRespuesta.config(width="18")
MediaRespuesta.config(bg='Light Gray',fg="black",font=("Arial",18),relief='raised')

#Copyright
copy=Label(miFrame, text="Copyright 2022 Diego Cuenca Prieto, created using python, tweepy and tkinter. All rights reserved.")
copy.place(x=10,y=320)
copy.config(bg="Blue")


raiz.mainloop()