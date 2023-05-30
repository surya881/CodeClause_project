import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile Music Player")
        self.root.geometry("400x300")
        self.root.configure(bg="#212121")

        self.song_list = []
        self.current_song_index = 0

        # Create and configure the buttons
        self.btn_choose_file = tk.Button(root, text="Choose Song", command=self.add_song, bg="#FF4081", fg="white", font=("Arial", 12))
        self.btn_play = tk.Button(root, text="▶ Play", command=self.play_music, bg="#FF4081", fg="white", font=("Arial", 12))
        self.btn_stop = tk.Button(root, text="■ Stop", command=self.stop_music, bg="#FF4081", fg="white", font=("Arial", 12))
        self.btn_next = tk.Button(root, text="→ Next", command=self.next_song, bg="#FF4081", fg="white", font=("Arial", 12))

        # Create and configure the song label
        self.lbl_song = tk.Label(root, text="", bg="#212121", fg="white", font=("Arial", 14))

        # Configure grid layout
        self.btn_choose_file.grid(row=0, column=0, columnspan=3, padx=10, pady=(50, 10))
        self.btn_play.grid(row=1, column=0, padx=10, pady=10, sticky="n")
        self.btn_stop.grid(row=1, column=1, padx=10, pady=10, sticky="n")
        self.btn_next.grid(row=1, column=2, padx=10, pady=10, sticky="n")
        self.lbl_song.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Configure column weights to center buttons horizontally
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def play_music(self):
        if len(self.song_list) == 0:
            messagebox.showinfo("Error", "No songs added.")
            return

        song_path = self.song_list[self.current_song_index]
        song_name = os.path.basename(song_path)
        self.lbl_song.config(text=song_name)

    def stop_music(self):
        self.lbl_song.config(text="")

    def next_song(self):
        self.current_song_index = (self.current_song_index + 1) % len(self.song_list)
        song_path = self.song_list[self.current_song_index]
        song_name = os.path.basename(song_path)
        self.lbl_song.config(text=song_name)

    def add_song(self):
        filetypes = (("MP3 files", "*.mp3"), ("All files", "*.*"))
        song_path = filedialog.askopenfilename(filetypes=filetypes)
        if song_path:
            self.song_list.append(song_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#212121")
    player = MusicPlayer(root)
    root.mainloop()
