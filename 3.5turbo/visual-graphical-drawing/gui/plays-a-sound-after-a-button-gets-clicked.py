import pygame
import tkinter as tk
from tkinter import messagebox
import os

def play_sound():
    # Initialize Pygame mixer
    pygame.mixer.init()
    
    # Load sound file
    sound_file = pygame.mixer.Sound("sound_file.wav")
    
    # Play sound
    sound_file.play()

def button_click():
    play_sound()
    messagebox.showinfo("Button Clicked", "Sound played!")

def main():
    # Create a GUI window
    window = tk.Tk()
    window.title("Button Sound Player")

    # Create a button
    button = tk.Button(window, text="Click me", command=button_click)
    button.pack()

    # Run the GUI window
    window.mainloop()

if __name__ == "__main__":
    main()