from tkinter import *
import pygame
import os

class MusicPlayer():

    
    def __init__ (self, Player):
        self.Player = Player
        self.Player.title("themaytrix Player")

        pygame.init()
        pygame.mixer.init()

        self.Player.geometry("500x150+10+10")

        trackframe = LabelFrame(self.Player, text = "soundTrack", font = ("times new roman", 15, "bold"), bg = "grey",fg ="black", relief = GROOVE)
        trackframe.place(x = 0 , y = 0, height = 100 ,width = 300)

        self.soundtrackValue = StringVar()
        soundtrack = Label(trackframe, textvariable = self.soundtrackValue, width = 20, font = ("times new roman", 13, "bold"), fg = "white", bg = "grey")
        soundtrack.grid(column = 0, row = 0)
        self.stat = StringVar()
        status = Label(trackframe, textvariable = self.stat, font= ("times new roman", 15, "bold"), fg ="gold", bg = "grey")
        status.grid(column = 1, row = 0)

        buttonframe = LabelFrame(self.Player, bg = "grey" , fg="white")
        buttonframe.place(x=0,y=100, height =50 , width =300)

        playbutton = Button(buttonframe, text = "PLAY", width = 8, height = 1, command = self.playsong)
        playbutton.grid(column = 0, row =0)

        playbutton = Button(buttonframe, text="PAUSE", width=8, height=1,command =self.pausesong)
        playbutton.grid(column=2, row=0,padx = 10, pady= 5)

        playbutton = Button(buttonframe, text="STOP", width=8, height=1)
        playbutton.grid(column=4, row=0)

        Playlistframe = LabelFrame(self.Player, text = "Songs" , bg = "white" , fg= "black")
        Playlistframe.place(x= 350, y =0 , width =150 , height =150)

        scroll_y = Scrollbar(Playlistframe, orient = VERTICAL)
        self.playlist = Listbox(Playlistframe, yscrollcommand=scroll_y.set, selectbackground="grey", selectmode=SINGLE, font=(
            "times new roman", 11, "bold"), fg="black", relief=GROOVE)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=Y)

        os.chdir("./music/")
        tracks = os.listdir()

        for songs in tracks:
            self.playlist.insert(END,songs)
    

    def playsong(self):
        
        #displaying selected song
        if self.pausesong():
            pygame.mixer.music.unpause()
        
        else:
            self.soundtrackValue.set(self.playlist.get(ACTIVE))
                #load song
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
                # Playing Selected Song
            pygame.mixer.music.play()

    def pausesong(self):
        pygame.mixer.music.pause()
        return True
        





Player = Tk()
MusicPlayer(Player)
Player.mainloop()
