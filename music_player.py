"""Import Dependencies"""
from tkinter import *
import pygame
import os
"""Defining MusicPlayer Class"""
class MusicPlayer:
  def __init__(self,root):
    self.root = root
    self.root.title("Music Player")
    self.root.geometry("1000x200+200+200")
    pygame.init()
    pygame.mixer.init()
    self.flag = 0
    self.track = StringVar()
    self.status = StringVar()
    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=600,height=100)
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="black",fg="darkgreen").grid(row=0,column=0,padx=10,pady=5)
    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",24,"bold"),bg="black",fg="darkgreen").grid(row=0,column=1,padx=10,pady=5)
    buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)
    """Play Commands"""
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="white",bg="darkgreen").grid(row=0,column=0,padx=10,pady=5)
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="white",bg="darkgreen").grid(row=0,column=1,padx=10,pady=5)
    playbtn = Button(buttonframe,text="NEXT",command=self.nextsong,width=8,height=1,font=("times new roman",16,"bold"),fg="white",bg="darkgreen").grid(row=0,column=2,padx=10,pady=5)
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=10,height=1,font=("times new roman",16,"bold"),fg="white",bg="darkgreen").grid(row=0,column=3,padx=10,pady=5)
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="darkgreen",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="black",fg="darkgreen",bd=5,relief=GROOVE)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    os.chdir("C:/Users/Admin/Music")
    songtracks = os.listdir()
    self.songlist = []
    for track in songtracks:
      self.playlist.insert(END,track)
      self.songlist.append(track)
  # Defining Play Song Function
  def playsong(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("-Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()
  def nextsong(self):
    k = self.playlist.get(ACTIVE)
    ind = self.songlist.index(k)
    self.playlist.activate((ind+1)%len(self.songlist))
    self.playsong()
  def stopsong(self):
    self.status.set("-Stopped")
    pygame.mixer.music.stop()
  def pausesong(self):
    if self.flag == 1:
        self.status.set("-Playing")
        pygame.mixer.music.unpause()
        self.flag -= 1
    else:
        self.flag += 1
        self.status.set("-Paused")
        pygame.mixer.music.pause()
# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()
