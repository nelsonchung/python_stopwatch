import tkinter as tk
from tkinter import ttk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.start_time = None
        self.elapsed_pause_time = 0
        self.running = False

        self.time_label = ttk.Label(root, text="00:00:00.000", font=("Helvetica", 48))
        self.time_label.pack()

        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=(20, 10))

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = ttk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        if not self.running:
            if self.start_time is None:
                self.start_time = time.time()
            else:
                self.start_time = time.time() - self.elapsed_pause_time
            self.running = True
            self.update_display()

    def stop(self):
        if self.running:
            self.running = False

    def pause(self):
        if self.running:
            self.elapsed_pause_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.start_time = None
        self.elapsed_pause_time = 0
        self.running = False
        self.time_label.config(text="00:00:00.000")

    def elapsed_time(self):
        if self.start_time is None:
            return "00:00:00.000"
        if self.running:
            elapsed = time.time() - self.start_time
        else:
            elapsed = self.elapsed_pause_time
        millis = int((elapsed - int(elapsed)) * 1000)
        seconds = int(elapsed) % 60
        minutes = (int(elapsed) // 60) % 60
        hours = (int(elapsed) // 3600) % 24
        return f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}"

    def update_display(self):
        if self.running:
            self.time_label.config(text=self.elapsed_time())
            self.root.after(1, self.update_display)  # Update every 1 millisecond

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()

