'''
timerApp
'''
import tkinter as tk


class Timer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('TimerApp')
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.tokei = tk.Label(self, text='00:00', font=('Helvetica', 100))
        self.tokei.pack()


if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    timer.mainloop()
