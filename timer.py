'''
timerApp
'''
import tkinter as tk


class Timer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('TimerApp')
        self.timer_config()
        self.create_widgets()
        self.pack()

    def timer_config(self):
        self.state = False
        self.minutes = 3
        self.seconds = 0
        self.mins = 3
        self.secs = 0

    def create_widgets(self):
        self.tokei = tk.Label(self, font=('Helvetica', 100), textvariable="")
        self.tokei.config(text="00:00")
        self.tokei.grid(row=0, column=0, columnspan=2)
        self.start_button = tk.Button(self, bg="Green", activebackground="Dark Green", text="開始", width=8, height=4, command=self.start)
        self.start_button.grid(row=1, column=0)
        self.pause_button = tk.Button(self, bg="Red", activebackground="Dark Red", width=8, height=4, command=self.pause)
        self.pause_button.config(text="一時停止")
        self.pause_button.grid(row=1, column=1)

    def countdown(self):
        if self.state:
            self.tokei.config(text="{}:{}".format(str(self.mins).zfill(2), str(self.secs).zfill(2)))

            if (self.mins == 0) and (self.secs == 0):
                self.tokei.config(text="Done!")
            else:
                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)

        elif not self.state:
            self.master.after(100, self.countdown)

    def start(self):
        if not self.state:
            self.state = True
            self.mins = self.minutes
            self.secs = self.seconds
            self.countdown()

    def pause(self):
        if self.state:
            self.state = False


if __name__ == "__main__":
    timer = Timer()
    timer.mainloop()
