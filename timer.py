'''
timerApp 00:00 to 99:59
'''
import tkinter as tk
import tkinter.ttk as ttk


class Timer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('TimerApp')
        self.timer_config()
        self.create_widgets()
        self.pack()
        self.countdown()

    def timer_config(self):
        self.state = False
        self.minutes = 3
        self.seconds = 0
        self.mins = 3
        self.secs = 0

    def create_widgets(self):
        self.spinbox_min = ttk.Spinbox(self, from_=0, to=99, command=self.spin_changed)
        self.spinbox_min.set(self.minutes)
        self.spinbox_min.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.spinbox_sec = ttk.Spinbox(self, from_=0, to=59, wrap=True, command=self.spin_changed)
        self.spinbox_sec.set(self.seconds)
        self.spinbox_sec.grid(row=0, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.tokei = tk.Label(self, font=('Helvetica', 100), textvariable="")
        self.tokei.config(text="00:00")
        self.tokei.grid(row=1, column=0, columnspan=3)
        self.start_button = tk.Button(self, bg="Red", activebackground="Dark Red", font=('Helvetica', 20), command=self.start)
        self.start_button.config(text="Start")
        self.start_button.grid(row=2, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.pause_button = tk.Button(self, bg="Green", activebackground="Dark Green", font=('Helvetica', 20), command=self.pause)
        self.pause_button.config(text="Pause")
        self.pause_button.grid(row=2, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        self.reset_button = tk.Button(self, bg="Blue", activebackground="Dark Blue", font=('Helvetica', 20), command=self.reset)
        self.reset_button.config(text="Reset")
        self.reset_button.grid(row=2, column=2, sticky=tk.W + tk.E + tk.N + tk.S)

    def spin_changed(self):
        self.minutes = int(self.spinbox_min.get())
        self.seconds = int(self.spinbox_sec.get())

    def countdown(self):
        if self.state:
            self.tokei.config(text="{}:{}".format(str(self.mins).zfill(2), str(self.secs).zfill(2)))

            if (self.mins == 0) and (self.secs == 0):
                self.tokei.config(text="Done!")
                self.state = False
            else:
                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1
                self.master.after(1000, self.countdown)

        else:
            self.tokei.config(text="{}:{}".format(str(self.mins).zfill(2), str(self.secs).zfill(2)))
            self.master.after(100, self.countdown)

    def start(self):
        if not self.state:
            self.state = True
            self.mins = self.minutes
            self.secs = self.seconds
            self.start_button.config(state=tk.DISABLED)

    def pause(self):
        if self.state:
            self.state = False
            self.pause_button.config(text="Resume")
            self.start_button.config(state=tk.NORMAL)

        else:
            self.state = True
            self.pause_button.config(text="Pause")

    def reset(self):
        self.mins = self.minutes
        self.secs = self.seconds


if __name__ == "__main__":
    timer = Timer()
    timer.mainloop()
