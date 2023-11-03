import tkinter as tk
import winsound as snd


def sound_decorator(function):
    def wrapped_function(*args, **kwargs):
        print("I am here")
        snd.PlaySound("Sound.wav", snd.SND_FILENAME)
        return function(*args, **kwargs)

    return wrapped_function


@sound_decorator
def cmd():
    print("command")


root = tk.Tk()
button = tk.Button(root, text="Play", command=cmd)
button.pack()
root.mainloop()
