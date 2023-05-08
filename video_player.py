
import tkinter, tkVideoPlayer

Tela = tkinter.Tk()

#Tela

Tela.title("Ain Zé da Manga")

Tela.geometry("480x450+600+200")

Tela.config(background="gray")

Tela.resizable(0, 0)

#Funções

def play():
    video.play()


def pause():
    video.pause()

def stop():
    video.stop()


#Botôes

btPlay = tkinter.Button(Tela, text="Play", relief="flat", width=10, borderwidth=5, command=play).grid(row=1, column=0, padx=55, pady=50)

btPause = tkinter.Button(Tela, text="Pause", relief="flat", width=10, borderwidth=5, command=pause).grid(row=1, column=1)

btStop = tkinter.Button(Tela, text="Stop", relief="flat", width=10, borderwidth=5, command=stop).grid(row=1, column=2, padx=55, pady=50)

#Video

video = tkVideoPlayer.TkinterVideo(Tela, scaled=True)

video.load("Messi.mp4")

video.grid(row=0, columnspan=10, sticky="we",padx=30, pady=30, ipady=90)


#Saída

Tela.mainloop()